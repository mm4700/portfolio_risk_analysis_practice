import pandas as pd
import pandas_datareader as pdr
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt


def test():
    start = dt.datetime(2021, 8, 1)
    tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM']
    data = pdr.get_data_yahoo(tickers, start)

    sp500 = pdr.get_data_yahoo('^GSPC', start)
    sp500 = sp500['Adj Close']

    data = data['Adj Close']
    data.head()

    log_returns = np.log(data/data.shift())

    # calculate the corr with SPX500

    log_returns['SP500'] = np.log(sp500/sp500.shift())

    # calculate the correlation between stocks
    log_returns.corr()

    test_correlation('LQD', start, log_returns)

def test_correlation(ticker, start, log_returns):
    df = pdr.get_data_yahoo(ticker, start)
    df = df['Adj Close']
    lr = log_returns.copy()
    lr[ticker] = np.log(df/df.shift())

    return lr.corr()




if __name__ == '__main__':
    test()


