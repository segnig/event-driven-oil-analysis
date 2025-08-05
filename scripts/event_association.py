import pandas as pd

def associate_events(change_dates, events):
    """Associate change points with historical events."""
    mean_date, vol_date = change_dates
    print("\nSuggested Event Associations:")
    
    for event_date, desc in events.items():
        event_date = pd.to_datetime(event_date)
        if abs((event_date - mean_date).days) < 30:
            print(f"- Mean change on {mean_date.strftime('%Y-%m-%d')} may relate to: {desc} ({(event_date - mean_date).days} days apart)")
        if abs((event_date - vol_date).days) < 30:
            print(f"- Volatility change on {vol_date.strftime('%Y-%m-%d')} may relate to: {desc} ({(event_date - vol_date).days} days apart)")
