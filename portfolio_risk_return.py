import pandas as pd
import pandas_datareader as pdr
import numpy as np
import datetime as dt


def test():
    start = dt.datetime(2022, 1, 1)
    data = pdr.get_data_yahoo('AAPL', start)

    arr = data.to_numpy()

    # calculate the percent change ln(prev value / after value)--Natural logarithm
    np.log(data/data.shift())

    # sum
    sum = np.sum(np.log(data/data.shift()))
    tail = np.log(data / data.iloc[0]).tail(1)

def test1():
    start = dt.datetime(2022, 1, 1)
    tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM']
    data = pdr.get_data_yahoo(tickers, start)
    data.head()

    close = data['Adj Close']

    portfolios = [.25, .15, .40, .20]
    np.sums(portfolios)

    # calculate the portfolio with 100000
    (data/data.iloc[0])*portfolios*100000

    weight = np.random.random(4)
    weight /= weight.sum()
    print(weight)





if __name__ == '__main__':
    test1()


