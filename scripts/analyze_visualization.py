import matplotlib.pyplot as plt
import pandas as pd
import arviz as az


def analyze_results(trace, log_returns, events=None):
    """Analyze and visualize change points."""
    # Get most probable change points
    tau_mean = int(az.summary(trace, var_names=["tau_mean"])["mean"].values[0])
    tau_vol = int(az.summary(trace, var_names=["tau_vol"])["mean"].values[0])
    
    # Get dates
    date_mean = log_returns.index[tau_mean]
    date_vol = log_returns.index[tau_vol]
    
    # Plot results
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(18, 12), sharex=True)
    
    # Plot log returns with change points
    ax1.plot(log_returns.index, log_returns, label='Log Returns', color='blue', alpha=0.7)
    ax1.axvline(date_mean, color='red', linestyle='--', 
                label=f'Mean Change: {date_mean.strftime("%Y-%m-%d")}')
    ax1.axvline(date_vol, color='green', linestyle='--', 
                label=f'Volatility Change: {date_vol.strftime("%Y-%m-%d")}')
    
    # Add events if provided
    if events is not None:
        for event_date, event_desc in events.items():
            ax1.axvline(pd.to_datetime(event_date), color='orange', alpha=0.5, 
                        linestyle=':', label=f'Event: {event_desc}')
    
    ax1.set_title('Brent Oil Log Returns with Detected Change Points')
    ax1.set_ylabel('Log Return')
    ax1.legend()
    ax1.grid(True)
    
    # Plot posterior distributions
    az.plot_posterior(trace, var_names=["tau_mean", "tau_vol"], 
                     ax=ax2, hdi_prob=0.95)
    ax2.set_title('Posterior Distributions of Change Points')
    
    plt.tight_layout()
    plt.show()
    
    # Quantify changes
    summary = az.summary(trace, var_names=["mu1", "mu2", "sigma1", "sigma2"])
    print("\nQuantitative Impact Analysis:")
    print(f"1. Mean changed from {summary.loc['mu1']['mean']:.4f} (95% CI: {summary.loc['mu1']['hdi_3%']:.4f}-{summary.loc['mu1']['hdi_97%']:.4f})")
    print(f"   to {summary.loc['mu2']['mean']:.4f} (95% CI: {summary.loc['mu2']['hdi_3%']:.4f}-{summary.loc['mu2']['hdi_97%']:.4f})")
    print(f"2. Volatility changed from {summary.loc['sigma1']['mean']:.4f} (95% CI: {summary.loc['sigma1']['hdi_3%']:.4f}-{summary.loc['sigma1']['hdi_97%']:.4f})")
    print(f"   to {summary.loc['sigma2']['mean']:.4f} (95% CI: {summary.loc['sigma2']['hdi_3%']:.4f}-{summary.loc['sigma2']['hdi_97%']:.4f})")
    
    return date_mean, date_vol, summary