# 50.034 – Introduction to Probability and Statistics: 1D Project

# Objective  
Explore one real-world example of a triple (X, Y, Z) of random variables, such that ρ(X, Y ) > 0 and ρ(Y, Z) > 0, but ρ(X, Z) < 0.


# Introduction 
We took a look at the correlations in stocks with through an initial hypothesis that people will tend to buy the safer bonds instead of the riskier stocks in a bad economy and vice versa in a good economy. 
 
## Assumptions
In order to simulate the daily volume of trades, we will use the NYSE composite which tracks the prices of all US common stocks.

## Code 
We analysed the Yahoo Finance data from the period of 10th Feb 2019 to 28th Feb 2019 and found that for our R.Vs 
- Let X be the price of the product of the US Treasury Yield 10 years (^TNX)
- Let Y be the price of the product of Tesla Stocks (TSLA) 
- Let Z be the price of the NYSE Composite (^NYA)

There was a positive correlation 0.21 for X and Z. 
There was a positive correlation 0.51 for Y and Z. 
A negative correlation -0.53 for X and Y. 

## Analysis 
Much of these findings made intuitive sense as naturally increases in prices of bonds or equities would increase the total volume of trades.

Additionally, our hypothesis seems to prove substantial as there seemed to be a strong linear correlation which are seldom in the stock market. 

Investment products all have a degree of a positive relation due to the believe of inflation whereby prices will raise. As such, strong negative correlations are uncommon.



# References
https://sg.finance.yahoo.com/
https://www.investopedia.com/ask/answers/040115/does-negative-correlation-between-two-stocks-mean-anything.asp#:~:text=A%20negative%20correlation%20is%20observed,to%20some%20degree%20in%20another
https://www.investopedia.com/articles/investing/100814/why-10-year-us-treasury-rates-matter.asp#citation-6
