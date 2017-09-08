This is the official toolbox for the [Quant Quest Competition](http://quant-quest.auquan.com) hosted by Auquan.

# Trading Problem Overview
This problem requires a mix of statistics and data analysis skills to create a predictive model using financial data. We will provide you with a toolbox and historical data to develop and test your strategy for the competition.

 1. [Installation](https://github.com/Auquan/quant-quest-toolbox#1-installation)
 2. [Problem 2](https://github.com/Auquan/quant-quest-toolbox#2-problem-2)
 3. [Problem 3](https://github.com/Auquan/quant-quest-toolbox#3-problem-3)
 4. [Data Format](https://github.com/Auquan/quant-quest-toolbox#4-data-format) 
 5. [Execution](https://github.com/Auquan/quant-quest-toolbox#5-execution) 
 6. [Backtesting and Debugging](https://github.com/Auquan/quant-quest-toolbox#6-backtesting-and-debugging) 

# 1. Installation
### Python 2.7
You need Python 2.7 (Python 3 will be supported later) to run this toolbox. There are several distributions of Python 2.7 that can be used. For an easy installation process, we recommend Anaconda since it will reliably install all the necessary dependencies. Download [Anaconda](http://continuum.io/downloads) and follow the instructions on the [installation page](http://docs.continuum.io/anaconda/install). Once you have Python, you can then install the toolbox.

### Quant Quest Toolbox
There are multiple ways to install the toolbox for the competition.

The easiest way and the most recommended way is via pip. Just run the following command:
`pip install -U quantquestToolbox`
It will also install all the dependencies including [auquanToolbox](https://github.com/Auquan/auquan-toolbox-python). After that follow the templates provided in [Problem2.py](https://github.com/Auquan/quant-quest-toolbox/blob/master/problem2.py) and [Problem3.py](https://github.com/Auquan/quant-quest-toolbox/blob/master/problem3.py) to get started. If we publish any updates to the toolbox, the same command `pip install -U quantquestToolbox` will also automatically get the new version of the toolbox. 

If you want to download this manually, you need to first get [auquanToolbox as instructed here](https://github.com/Auquan/auquan-toolbox-python#installation). After that clone or download this repo. After you do that, navigate to the root folder of this project and run `python setup.py install`. This will also install all the dependencies, and you are good to run an existing strategy or create a new one. You would have to redownload the toolbox code, if we published any changes to the toolbox.

# 2. Problem 2
You are given a list of securities to trade.  Create a prediction model that uses the daily price data provided and returns a daily signal for every security: +1 for buy, -1 for sell or 0 for no opinion.
Use file [problem2.py](https://github.com/Auquan/quant-quest-toolbox/blob/master/problem2.py) provided with the toolbox for this problem and complete the function trading_strategy().

### Input: 
You are given 5 years of daily price and volume data of 50 random stocks.To help you get started with the challenge, we will also provide you with a set of features. (The list of features only serve as an introduction and are not exhaustive, you can create new features from the given price data). Read more about the data format [here](https://github.com/Auquan/quant-quest-toolbox#4-data-format).

### Output format:
Your code’s final output should be pandas dataframe with security symbol as rows and *SIGNAL* as columns:

| Security | SIGNAL | 
| --------- | ------------- |
|AAPL | 1   |      
|GOOG | -1 |    

### Scoring:
The objective of this problem is to maximize prediction efficiency.  A prediction is correct if you label a security as buy on day t and open price on day t+1 is greater than previous day’s open price. Similarly, if you label a security as sell, it is correct if open price on day t+1 is lower than previous day’s open price
Your final score will be:

Score = Sum(Signal (t) (Open Price (t+1) - Open Price(t))


To discourage overfitting, you are provided only a subset of the data for backtesting.  Your final score will be calculated over complete data set ( performance over backtested data and test data which is not available for download).

Final points for this problem are relative. i.e. the contestant with highest score gets 40 points. 

**40 points**

# 3. Problem 3
You are now given $1,000,000 as starting funds and the same list of securities to trade. Use the prediction model from problem 2a  to develop a trading strategy which decides how to allocate funds to each security. For every security, you have to return a trading signal and it’s weight in the portfolio.
Use file problem2b.py provided with the toolbox for this problem and complete the function trading_strategy().

### Input:
You are given the same input as problem 2a,  5 years of daily price and volume data of 50 stocks and a set of features. (The list of features only serve as an introduction and are not exhaustive, you can create new features from the given price data). Read more about the data format [here](https://github.com/Auquan/quant-quest-toolbox#4-data-format).

Order executions happen at OPEN price every day. The toolbox applies a commision of 10 cents per trade. Read more about execution and backtesting [here](https://github.com/Auquan/quant-quest-toolbox#5-execution).

### Output format:
Your code’s final output should be pandas dataframe with security symbol as rows and *SIGNAL* and *WEIGHTS* as columns. The weights, which are a number between 0 to 1, define percentage allocation of portfolio value to that security:

| Security | SIGNAL | WEIGHTS |
| --------- | ------------- | ----------- |
|AAPL | 1   |      55%
|GOOG | -1 |     45%

Here, if we have $1,000,000 in funds, we buy $550,000 worth of AAPL shares and sell $450,000 worth of GOOG shares.

The weights don’t have to sum to 1. If they sum to < 1, the remaining funds are available as cash. If they sum to > 1, the weights are renormalized so that they sum to 1.

At any given time t, your model should only use data from time T=0 to T=t. Our toolbox is designed to prevent you from accessing data beyond the timestamp for which you are predicting.

If  you run out of available funds, you will stop trading (i.e. total losses > initial budget).

### Scoring:
The objective of this problem is to maximize risk adjusted Profits. For this problem, we will score you on the Sharpe Ratio of your strategy i.e.:

Score: Sharpe Ratio = Annualized Return/ Annualized Volatility

To discourage overfitting, you are provided a subset of data for backtesting.  Your final score will be calculated over complete data set ( performance over backtested data and test data which is not available for download).

If two strategies tie, we will use the profit factor as a tie breaker, which is
Profit Factor: Sum of Profits/Sum of Losses

Final points for this problem are relative. I.e. the contestant with highest score gets 45 points. 

**45 points**

## Other information:

# 4. Data Format:

Securities are labeled as a1,a2...b1,b2....j1,j2.. Full list of securities is available [here](https://github.com/Auquan/auquan-historical-data/blob/master/abcd/abcd.txt)

The names and dates for all securities are scrambled. A group of securities starting with the same alphabet denote that they belong to the same sector(i.e. energy, utilities, technology etc).

Date| OPEN|HIGH|LOW|CLOSE|VOLUME|F1|F2|F3|F4...

1. Date: Trading Date

2. OPEN: Opening price on the day

3. HIGH: Highest traded price of the day

4. LOW: Lowest traded price of the day

5. CLOSE: Closing price of the day

6. VOLUME: Total Volume traded on the day (number of contracts)

The next 29 columns provide a list of features derived from the price data. These are included to help you get started and you are advised to create your own features as well. These features are:

1. SMA: Simple moving average over periods 30,90,120 days

2. EMA: Exponentially weighted moving average over periods 30,90,120 days

3. SDev: Rolling Standard Deviation over 30,90,120 days

4. MOM: Momentum indicator, defined as price now - price n periods before

5. MACD : Moving Average Convergence Divergence, difference of Fast SMA(shorter period) - Slow SMA(longer period)

6. BBand_low, BBand_high: Bollinger Bands, SMA +/- Rolling SDev 

7. RSI: Relative Strength Indicator, momentum indicator with value between 0 and 100. RSI is considered overbought when above 70 and oversold when below 30

8. PVT: Price Volume Trend, used to measure flow of dollar volume. Calculated as [Volume * (CurrentClose - PreviousClose) / PreviousClose] + PreviousPVT

9. ATR: Average True Range, volatility indicator. Measure as the moving average of max[(high - low), abs(high - previous close), abs (low - previous close)]

10. STOCH: Stochastic Oscillator, another momentum indicator measured as moving average of 100 * (Current Close - Lowest Low)/(Highest High - Lowest Low) 

 
# 5. Execution:
An execution is the completion of a buy or sell order for a security. Once you provide your list of trades, our code will trade them for you. You may treat the execution code as a black box.

Trade executions happen at next day’s open price. It will calculate the quantity of each security you will trade based on portfolio weights  and available funds net of trading costs. For every trade, there will be a commission charge of 10 cents. 

Example, you want to buy a security and keep portfolio weight of 50%. The open price is 99. If your portfolio value before this trade is 1000$, you buy 5 lots at 99$ and are charged 5*0.1 = 0.50$ for it. Your new portfolio value is 999.50 and available funds will be 1000-5*99 - 5*0.1 = 504.5$.

The toolbox will automatically rebalance the portfolio for you daily. In the above example, if the value of security rises to $139 and you make a profit so that your portfolio value is $1199.50 the system sells one share at 139 to maintain ~50% portfolio weight.  Your new portfolio value is $1199.40 and your available funds are 504.5+139-0.1 = 643.40

# 6. Backtesting and Debugging:
Backtesting is the process of evaluating a trading strategy’s performance on historical data. You can use the backtesting tool provided by us to evaluate the performance of your code on historical data and examine how your model’s performance changes as you make changes to any model parameters.

The toolbox charts your performance and provides detailed logs in a csv file. You can visualize the performance of your strategy over different time periods, compare it with the performance of a benchmark index, inspect your daily trades and positions in each security and analyze how your model performs on some key metrics. Our backtesting tool will display the following metrics.

1. Total Return: The Total Profit (or Loss) from the model in the given time period, specified as a percentage of the initial available funds.

2. Annualized Return: The average % Profit(or Loss) from the model in a year.

3. Annualized Volatility: The standard deviation of daily returns of the model in a year. Volatility is used as a measure of risk, therefore higher vol implies riskier model.

4. Sharpe Ratio: Risk adjusted Returns, calculated as Annualized Return/Annualized Volatility

5. Sortino Ratio: Returns adjusted for downside risk, calculated as Annualized Return/Annualized  Volatility of Negative Returns

6. Max Drawdown: Maximum negative difference in Total Portfolio Value. It is calculated as the maximum high to subsequent low difference before a new high is reached 

7. Profit Factor: Sum of Profits from trades that results in profits/Sum of losses from trades that results in losses

8. % Profitability = Sum of Profits from trades that results in profits/Total PnL
