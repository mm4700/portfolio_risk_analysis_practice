import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt


def test1():
    start = dt.datetime(2021, 8, 1)
    tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM', '^GSPC']
    data = pdr.get_data_yahoo(tickers, start)

    data = data['Adj Close']
    data.head()

    log_returns = np.log(data/data.shift())

    ticker_a = 'AAPL'
    ticker_b = '^GSPC'

    linear_regression(log_returns, ticker_a, ticker_b)


def linear_regression(log_returns, ticker_a, ticker_b):
    # remove nan in the first row and reshape to one column numpy arr
    X = log_returns[ticker_a].iloc[1:].to_numpy().reshape(-1, 1)
    Y = log_returns[ticker_b].iloc[1:].to_numpy().reshape(-1, 1)
    lin_regr = LinearRegression()
    lin_regr.fit(X, Y)
    Y_pred = lin_regr.predict(X)

    alpha = lin_regr.intercept_[0]
    beta = lin_regr.coef_[0, 0]

    fig, ax = plt.subplots()
    ax.set_title('Alpha: ' + str(round(alpha, 5)) + ", Beta: " + str(round(beta, 3)))
    ax.scatter(X, Y)
    ax.plot(X, Y_pred, c='r')


def test():
    X = np.random.randn(5000)
    Y = np.random.randn(5000)

    fig, ax = plt.subplots()
    ax.scatter(X, Y, alpha=.2)





if __name__ == '__main__':
    test1()


