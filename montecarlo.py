import pandas as pd
import pandas_datareader as pdr
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

def test():

    start = dt.datetime(2021, 8, 1)
    tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM']
    data = pdr.get_data_yahoo(tickers, start)

    data = data['Adj Close']
    # current value / prev value , in percentage natrual logarithm
    log_return = np.log(data / data.shift())

    weight = np.random.random(4)
    weight /= weight.sum()

    # expected yearly retrun *252
    exp_rtn = np.sum(log_return.mean()*weight)*252

    # expected volatility
    exp_vol = np.sqrt(np.dot(weight, np.dot(log_return.cov()*252, weight)))

    sharpe_ratio = exp_rtn / exp_vol

    monte_carlo_return(data)

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


def monte_carlo_return(data):
    log_return = np.log(data / data.shift())
    # Monte Carlo Simulation
    n = 5000
    weights = np.zeros((n, 4))
    exp_rtns = np.zeros(n)
    exp_vols = np.zeros(n)
    sharpe_ratios = np.zeros(n)
    for i in range(n):
        weight = np.random.random(4)
        weight /= weight.sum()
        weights[i] = weight
        exp_rtns[i] = np.sum(log_return.mean() * weight) * 252
        exp_vols[i] = np.sqrt(np.dot(weight, np.dot(log_return.cov() * 252, weight)))
        sharpe_ratios[i] = exp_rtns[i] / exp_vols[i]

    sharpe_ratios.max()
    sharpe_ratios.argmax()
    weights[sharpe_ratios.argmax()]

    fig, ax = plt.subplots()
    ax.scatter(exp_vols, exp_rtns, c=sharpe_ratios)
    ax.scatter(exp_vols[sharpe_ratios.argmax()], exp_rtns[sharpe_ratios.argmax()], c='r')
    ax.set_xlabel('Expected Volatility')
    ax.set_ylabel('Expected Return')

def roll_dice():
    # get the sum of rolling 2 dice 1-6
    return np.sum(np.random.randint(1, 7, 2))

def monte_carlo_simulation(runs=1000):
    results = np.zeros(2)
    for _ in range(runs):
        if roll_dice() == 7:
            results[0] += 1
        else:
            results[1] += 1
    return results

def sharpe_ratio_monte_carlo():
    start = dt.datetime(2021, 8, 1)
    tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM']
    data = pdr.get_data_yahoo(tickers, start)

    data = data['Adj Close']
    monte_carlo_return(data)

if __name__ == '__main__':
    #result = monte_carlo_simulation()

    # result = np.zeros(1000)
    # for i in range(1000):
    #     result[i] = monte_carlo_simulation()[0]
    #
    # print(result)
    #
    # d1 = np.arrange(1, 7)
    # d2 = np.arrange(1, 7)
    # mat = np.add.outer(d1, d2)
    # # 36 possibility
    # mat.size
    #
    # mat[mat == 7].size / mat.size

    sharpe_ratio_monte_carlo()













if __name__ == '__main__':
    test()


