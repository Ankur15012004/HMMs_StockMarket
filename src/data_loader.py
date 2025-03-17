import yfinance as yf
import pandas as pd
import numpy as np

def fetch_stock_data(ticker='^GSPC',start="2005-01-01",end="2025-01-01"):
    """
        Fetches 15 year stock data of S&P-500 starting from 2020-01-01 to 2025-01-01.

        Args:
            -ticker: Stock Symbol(default is S&P-500(^GSPC))
            -start: Start date of data fetching.
            -end: End date of data fetching.

        Returns:
            A dataframe consisting of S&P-500 features.

    """
    data =yf.download(tickers=ticker, start=start,end=end,multi_level_index=False)
    data=data.reset_index()
    return data

