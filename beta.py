import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt

def beta():
    start = dt.datetime(2017, 1, 23)
    tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM', '^GSPC']
    data = pdr.get_data_yahoo(tickers, start, interval='m')

    data = data['Adj Close']
    log_returns = np.log(data/data.shift())

    cov = log_returns.cov()
    var = log_returns['^GSPC'].var()

    beta_appl = cov.loc['AAPL', '^GSPC']/var

    beta_all = cov.loc['^GSPC']/var

    X = log_returns['^GSPC'].iloc[1:].to_numpy().reshape(-1, 1)
    Y = log_returns['AAPL'].iloc[1:].to_numpy().reshape(-1, 1)

    lin_regr = LinearRegression()
    lin_regr.fit(X, Y)

    beta_appl = lin_regr.coef_[0, 0]

    print(beta_appl)
    print(beta_appl)





if __name__ == '__main__':
    beta()