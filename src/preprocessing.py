from data_loader import fetch_stock_data
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

def compute_log_returns(data):
    """
    Compute the log returns without modifying the original DataFrame.

    Args:
        - data: A DataFrame consisting of stock prices.
    
    Returns:
        - A new DataFrame with log returns.
    """
    log_returns = np.log(data["Close"] / data["Close"].shift(1))
    return log_returns.dropna().to_frame(name="Log Returns")


def preprocessing_data(data):
    """
        Standardize the log-returns to have mean 0 and variance 1 using sklearn StandardScaler.

        Args:
            - log_returns: Series consisting of log returns value.
        
        Returns:
            - DataFrame having standardize values.
    
    """
    log_returns=compute_log_returns(data)
    ## Checking for any null values if present and dropping the null values.

    log_returns = log_returns.dropna().copy()


    ## Standardizing the data.

    ss=StandardScaler()
    standardized_returns=ss.fit_transform(log_returns)

    return pd.DataFrame(standardized_returns)