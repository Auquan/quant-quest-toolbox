from __future__ import absolute_import, division, print_function, unicode_literals
import pandas as pd
import numpy as np
import competitionToolbox as ct

def settings():
    markets = [] # Stocks to download data for. 
    # markets = [] Leave empty array to download all stocks for the exchange (~900 stocks)
    # To have a look at all possible stocks go here: 
    # 
    # Based on data avalaible, some markets might be dropped. Only the non dropped markets will appear
    # in lookback_data for trading_strategy

    lookback = 120               # Number of days you want historical data for. Max can be 300.

    """ To make a decision for day t, your algorithm will have historical data
    from t-lookback to t-1 days"""
    return [markets, lookback]

def trading_strategy(lookback_data):
    """
    :param lookback_data: Historical Data for the past "lookback" number of days as set in the main settings.
     It is a dictionary of features such as,
     'OPEN', 'CLOSE', 'HIGH', 'LOW', 'VOLUME', 'POSITION', 'ORDER',
     'FILLED_ORDER', 'DAILY_PNL', 'TOTAL_PNL', 'FUNDS', 'VALUE'
     Any feature data can be accessed as:lookback_data['OPEN']
     The output is a pandas dataframe with dates as the index (row)
     and markets as columns. 
    """"""""""""""""""""""""""
    """""""""""""""""""""""""" 
    To see a complete list of features, uncomment the line below"""
    #print(lookback_data.keys())
    
    """""""""""""""""""""""""""
    :return: A pandas dataframe with markets you are trading as index(row) and 
    signal, price and quantity as columns
    order['SIGNAL']:buy (+1), hold (0) or sell (-1) trading signals for all securities in markets[]
"""

    order = pd.DataFrame(0, index=lookback_data['POSITION'].columns, columns = ['SIGNAL'])

    ##YOUR CODE HERE

    return order

if __name__ == '__main__':
    [markets, lookback] = settings()
    # For testing you can change dates if you want.
    date_start = '01-01-2002' # Default date trading will start
    date_end = '31-12-2013' # Date trading will end. When you submit your solution, we will run with more data.
    ct.runSolution(markets, lookback, trading_strategy, date_start, date_end, ct.PROBLEM2_ID)#,verbose=True)
