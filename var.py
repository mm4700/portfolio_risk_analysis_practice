import pandas as pd
import pandas_datareader as pdr
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt


def get_data(stocks, start, end):
    stockData = pdr.get_data_yahoo(stocks, start=start, end=end)
    stockData = stockData['Close']
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return returns, meanReturns, covMatrix

def test_var():
    stock_list = ['CBA', 'BHP', 'TLS', 'NAB', 'WBC', 'STO']
    stocks  = [stock + '.AX' for stock in stock_list ]
    end_date = dt.datetime.now()
    start_date = end_date - dt.timedelta(days=400)

    returns, meanReturns, covMatrix = get_data(stocks, start=start_date, end=end_date)

    returns.dropna(inplace=True)

    weights = np.random.random(len(returns.columns))
    weights /= np.sum(weights)

    returns['portfolio'] = returns.dot(weights)

    var = historicalVaR(returns['portfolio'], alpha=5)
    c_var = historicalCVaR(returns['portfolio'], alpha=5)




def historicalVaR(returns, alpha=5):
    """
    Read in a pandas dataframe of returns / a pandas series of returns
    Output the percentile of the distribution at the given alpha confidence level

    the required capital to guarantee your portfolio or position is above 0 to that confidence interval.
    """
    if isinstance(returns, pd.Series):
        return np.percentile(returns, alpha)

    # A passed user-defined-function will be passed a Series for evaluation.
    elif isinstance(returns, pd.DataFrame):
        return returns.aggregate(historicalVaR, alpha=alpha)

    else:
        raise TypeError("Expected returns to be dataframe or series")

def historicalCVaR(returns, alpha=5):
    """
    Read in a pandas dataframe of returns / a pandas series of returns
    Output the CVaR for dataframe / series
    """
    if isinstance(returns, pd.Series):
        belowVaR = returns <= historicalVaR(returns, alpha=alpha)
        return returns[belowVaR].mean()

    # A passed user-defined-function will be passed a Series for evaluation.
    elif isinstance(returns, pd.DataFrame):
        return returns.aggregate(historicalCVaR, alpha=alpha)

    else:
        raise TypeError("Expected returns to be dataframe or series")


# Portfolio Performance
def portfolioPerformance(weights, meanReturns, covMatrix, Time):
    returns = np.sum(meanReturns*weights)*Time
    std = np.sqrt( np.dot(weights.T, np.dot(covMatrix, weights)) ) * np.sqrt(Time)
    return returns, std

if __name__ == '__main__':
    test_var()