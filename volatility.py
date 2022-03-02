import pandas as pd
import pandas_datareader as pdr
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt


def test():
    start = dt.datetime(2022, 1, 1)
    data = pdr.get_data_yahoo('NFLX', start)

    high_low = data['High'] - data['Low']
    # calculate the absolute value for high - prev close
    high_cp = np.abs(data['High'] - data['Close'].shift())
    # calculate the absolute value for low - prev close
    low_cp = np.abs(data['Low'] - data['Close'].shift())

    # calculat the TR(True Range) for max
    # align with column
    df = pd.concat([high_low, high_cp, low_cp], axis=1)
    true_range = np.max(df, axis=1)
    # default 14 days average
    average_true_range = true_range.rolling(14).mean()

    fig, ax = plt.subplots()
    average_true_range.plot(ax=ax)
    ax2 = data['Adj Close'].plot(ax=ax, secondary_y=True, alpha=.3)


def volatility():
    start = dt.datetime(2021, 8, 1)
    tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM']
    data = pdr.get_data_yahoo(tickers, start)

    portfolio = [.25, .15, .40, .20]

    data = data['Adj Close']

    returns = np.log(data).diff()
    returns.dropna(inplace=True)

    std = np.sqrt(returns.var() * 252)

    cov = returns.cov() * 252
    vol = np.sqrt(np.dot(portfolio, np.dot(cov, portfolio)))

    np.square()

    return vol







if __name__ == '__main__':
    volatility()


