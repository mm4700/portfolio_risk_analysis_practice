import pandas as pd
import pandas_datareader as pdr
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

def test():
    start = dt.datetime(2021, 8, 1)
    tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM']
    data = pdr.get_data_yahoo(tickers, start)

    portfolio = [.25, .15, .40, .20]
    data = data['Adj Close']
    # current value / prev value , in percentage
    np.log(data / data.shift())
    # this is the log change from end to begining
    np.sum(np.log(data/data.shift()), axis=1)

    log_return = np.sum(np.log(data/data.shift())*portfolio, axis=1)

    fig, ax = plt.subplots()
    log_return.hist(bins=50, ax=ax)

    # standard deviation
    std = log_return.std()

    # daily mean return
    log_return.mean()
    # sharpe ratio
    sharpe_ratio = log_return.mean()/std

    # 252 trading days per year , lift the power of **.5
    annualized_sharpe_ratio = sharpe_ratio*252**.5



if __name__ == '__main__':
    test()




