#!/usr/bin/env python
# coding: utf-8

# # In this assignment program we will import stocks data from Yahoo Finance using Parsing and Cleaning the data, we will create a program that can calculate each and every individual stock returns, variance/co-variance matrix

# In[1]:


# Import all the library you need in order to run your portfolio optimization project
# importing pandas and numpy helps you manipulate data the best

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import pandas_datareader.data as source
import seaborn as sns
 # matplotlib is good for plotting but not as good as seaborn because its object oriented
import datetime as dt 
#Importing datetime helps with using start date and end dates for our data reader function
import yfinance as yf
#Imporing yfinance above allows us to avoid making a loop and storing all 10 tickers on a monthly basis for their stock return in one dataframe


# # 1) Download monthly stock return data for the following companies from any data provider (for 10 years). Along with that download the S&P 500 data as well as Risk Free Rate with the SPY ticker and ^IRX  ticker.

# In[2]:


#below now we defined a variable called tickers to call later with all the 10 stocks we want in our dataframe
tickers = ['AAPL','BAC','BA','BBY','HOG','HD','RTX','IHG','SBUX','XOM', '^GSPC', '^IRX']

#now we created a dataframe where we are feeding the data from yahoo finance
dataframe = yf.download('AAPL BAC BA BBY HOG HD RTX IHG SBUX XOM ^GSPC ^IRX', start = "2012-10-06", end = dt.datetime.today(), interval = '1mo')
print(dataframe)


# # We need to clean the data form above and redefine our dataframe so that we don't use null values for our calculations

# In[3]:


# based on how stocks are calculated on a daily basis, we only do care about the adjusted close value.
# lets retrive that for our dataframe and just use the Adjusted Close Value

dataframe = dataframe['Adj Close']

# some of the values we get above have null values, therefore now we will clean our data to just use the montly Adjusted close values for the tickers

dataframe = dataframe.dropna()
dataframe = dataframe.rename(columns ={'^IRX':'Rf', '^GSPC':'S&P-500'})
# with that code above we now go from a array that was (444 rows x 60 columns) to (120 rows x 10 columns) for our data by taking away the null values

print(dataframe)


# ## 2) Now we will calculate expected return for each company and store it in a new dataframe

# In[4]:


# now that we have our cleaned data and we have everything ready we will start doing calculations
# first lets define our funcitons to call them later and make our program efficient

# lets start with the first funciton for percentage change on a monthly basis from the previous month and store it on its own dataframe for later use

dataframe_expected_return = dataframe.pct_change(1)
print(dataframe_expected_return)


# In[5]:


# we now calculate the log of stock price return ( for log to give normal distribution of returns)
dataframe_log_returns = np.log(dataframe/dataframe.shift())
print(dataframe_log_returns)


# In[6]:


# now we need to do the variance function for each company and store it on its own dataframe for later use

dataframe_variance = dataframe_log_returns['S&P-500'].var()
print(dataframe_variance)


# now we need to do the covariance function for each company and store it on its own dataframe for later use
# when we talk about covariance in finance we are talking about covariance of your expected returns for the stocks

dataframe_covariance = dataframe_log_returns.cov()
print(dataframe_covariance)


# In[15]:


# here we create the list of just the stocks for our stocks portfolio
stocks_portfolio = ['AAPL','BAC','BA','BBY','HOG','HD','RTX','IHG','SBUX','XOM']

# now we create an empty dataframe for beta values to store our final results
dataframe_betas = pd.DataFrame()

x = 0
for i in stocks_portfolio:
    dataframe_betas[stocks_portfolio[x]]=stocks_portfolio[x]
    x = x + 1

# now we calculate the beta of each stock (cov of stock and market/variance of market)
# beta can be calculated in many ways (with the CAPM equation as well as the slope of the SML)
# here we calculate beta with (cov of stock and market/variance of market)

AAPL = dataframe_covariance.loc['AAPL', 'S&P-500']/dataframe_variance

BAC = dataframe_covariance.loc['BAC', 'S&P-500']/dataframe_variance

BA = dataframe_covariance.loc['BA', 'S&P-500']/dataframe_variance

BBY = dataframe_covariance.loc['BBY', 'S&P-500']/dataframe_variance

HOG = dataframe_covariance.loc['HOG', 'S&P-500']/dataframe_variance

HD = dataframe_covariance.loc['HD', 'S&P-500']/dataframe_variance

RTX = dataframe_covariance.loc['RTX', 'S&P-500']/dataframe_variance

IHG = dataframe_covariance.loc['IHG', 'S&P-500']/dataframe_variance

SBUX = dataframe_covariance.loc['SBUX', 'S&P-500']/dataframe_variance

XOM = dataframe_covariance.loc['XOM', 'S&P-500']/dataframe_variance

# now lets input all betas into a list

betas = [AAPL, BAC, BA, BBY, HOG, HD, RTX, IHG, SBUX, XOM]


# here below we append betas to dataframe_betas 
dataframe_betas.loc[0] = betas
# now we are going to transpose results to allow for renaming
dataframe_betas = dataframe_betas.T
# now we are going to rename the created column to betas
dataframe_betas = dataframe_betas.rename(columns = {0:'Betas'})

# now here we Transpose again back to our original format
dataframe_betas = dataframe_betas.T
print(dataframe_betas)


# In[ ]:




