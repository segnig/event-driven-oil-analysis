import numpy as np
import pymc as pm


def detect_change_points(log_returns):
    """Detect changes in mean and volatility using PyMC."""
    returns = log_returns.values
    n = len(returns)
    
    with pm.Model() as model:
        # Priors for change point locations (constrained to middle 80% of data)
        tau_mean = pm.DiscreteUniform("tau_mean", lower=int(n*0.1), upper=int(n*0.9))
        tau_vol = pm.DiscreteUniform("tau_vol", lower=int(n*0.1), upper=int(n*0.9))
        
        # Wider priors for mean and volatility
        mu1 = pm.Normal("mu1", mu=0, sigma=0.5)
        mu2 = pm.Normal("mu2", mu=0, sigma=0.5)
        sigma1 = pm.HalfNormal("sigma1", sigma=0.5)
        sigma2 = pm.HalfNormal("sigma2", sigma=0.5)
        
        # Mean and volatility switches
        mean = pm.math.switch(pm.math.lt(np.arange(n), tau_mean), mu1, mu2)
        sigma = pm.math.switch(pm.math.lt(np.arange(n), tau_vol), sigma1, sigma2)
        
        # Robust likelihood (StudentT handles outliers better than Normal)
        obs = pm.StudentT("obs", nu=4, mu=mean, sigma=sigma, observed=returns)
        
        # Sampling with improved settings
        trace = pm.sample(
            draws=3000,
            tune=2000,
            chains=4,
            target_accept=0.95,
            random_seed=42,
            cores=1,
            # Removed incorrect step specification
        )
    
    return trace