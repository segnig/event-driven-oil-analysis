import pandas as pd
import numpy as np

def prepare_data(data):
    """Convert prices to log returns and handle missing dates."""
    # Ensure datetime index
    data.index = pd.to_datetime(data.index)
    data = data.sort_index()
    
    # Fill missing dates and interpolate prices
    full_date_range = pd.date_range(start=data.index.min(), end=data.index.max(), freq='D')
    data = data.reindex(full_date_range)
    data['Price'] = data['Price'].interpolate(method='time')
    
    # Calculate log returns (stationary series)
    data['Log_Return'] = np.log(data['Price']).diff()
    return data.dropna(subset=['Log_Return'])