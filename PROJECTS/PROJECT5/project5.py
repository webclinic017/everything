# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# generic modules
from datetime import date

import pandas as pd
import time
import sys

# local modules
from binance.client import Client
from binance.enums import *
from indicator import indicators

# local file
import secrets
from configparser import ConfigParser
import yfinance as yf
import numpy as np
import datetime as dt
import requests 
import json 
import pandas as pd 
import numpy as np  

# %%
config=ConfigParser()
config.read('keys.txt')
import telepot
bot = telepot.Bot('1715056219:AAGxytb3U1gIt1vlVn8Jf5b4za3E1HPuOd4')
bot.getMe()

# %%
client = Client(str(config['KEYS']['binance_api_key']), str(config['KEYS']['binance_api_secret_key']))


# %%
position=""


# %%
def candle(symbol, interval="5m"):


    root_url = 'https://api.binance.com/api/v1/klines'
    url = root_url + '?symbol=' + symbol + '&interval=' + interval
    data = json.loads(requests.get(url).text)
    df = pd.DataFrame(data)
    df.columns = ['Datetime',
                'Open', 'High', 'Low', 'Close', 'volume',
                'close_time', 'qav', 'num_trades',
                'taker_base_vol', 'taker_quote_vol', 'ignore']
    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
    
    df.drop(['close_time','qav','num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'],axis=1,inplace=True)
           
    
    df['Open']=pd.to_numeric(df["Open"], downcast="float")
    df["High"]=pd.to_numeric(df["High"], downcast="float")
    df["Low"]=pd.to_numeric(df["Low"], downcast="float")
    df["Close"]=pd.to_numeric(df["Close"], downcast="float")
    df["volume"]=pd.to_numeric(df["volume"], downcast="float")
    
    
    
    
    df1=pd.DataFrame()
    Open=[]
    
    df1['Close']=((df['Open'] + df['High'] + df['Low'] + df['Close'])/4)
    for i in range(len(df)):
        if i==0:
            Open.append(0)

        else:
            Open.append((df['Open'][i-1]+df['Close'][i-1])/2)
    df1['Open']=np.array(Open)
    df1['volume']=df['volume']
    High=[]
    Low=[]
    High.append(0)
    Low.append(0)
    for i in range(1,len(df)):

        High.append(max(df['High'][i],df1['Close'][i],df1['Open'][i]))
        Low.append(min(df['Low'][i],df1['Close'][i],df1['Open'][i]))

    df1['High']=np.array(High)
    df1['Low']=np.array(Low)



    new_df = indicators.SuperTrend(df1, int(config['INPUTS']['atr']), int(config['INPUTS']['factor']))

    return new_df


    



# %%
def ltp_price(instrument):
    prices = client.get_all_tickers()
    for i in range(len(prices)):
        if prices[i]['symbol']==str(instrument):
            
            return float(prices[i]['price'])

    


# %%

def market_order():
    global position,price1,l
    
    order = client.futures_create_order(
        symbol=str(config['INPUTS']['symbol_binance']),
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
       
        
        quantity=float(config['INPUTS']['quantity']))

    price1=ltp_price(config['INPUTS']['symbol_binance'])
    position='long'
    l=1
    



def market_order1():
    global position,price2,l
    
    order = client.futures_create_order(
        symbol=str(config['INPUTS']['symbol_binance']),
        side=Client.SIDE_SELL,
        type=Client.ORDER_TYPE_MARKET,

        
        quantity=float(config['INPUTS']['quantity']))
    price2=ltp_price(config['INPUTS']['symbol_binance'])
    position='short'
    l=1


# %%



# %%
def main():

    times1=time.time()
    config=ConfigParser()
    config.read('keys.txt')
    global quantity,df,position,price1,price2,l
    
    df=candle(config['INPUTS']['symbol_binance'],'5m')
    signal=""

    
    if l==0:
    
        if df.iloc[:,8][-1]!=df.iloc[:,8][-2] and position=="":
            if df.iloc[:,8][-1]=='down':
                signal='sell'
              

            if df.iloc[:,8][-1]=='up':
                signal='buy'
     
    ltp=ltp_price(config['INPUTS']['symbol_binance'])
    
    
    if l>0:
        if df.iloc[:,8][-1]!=df.iloc[:,8][-2] and position=="":
            if df.iloc[:,8][-1]=='down':
                signal='sell'

            if df.iloc[:,8][-1]=='up':
                signal='buy'
        
        if (position=="long" and ltp>price1+price1*(float(config['INPUTS']['take_profit_precentage']))/100/int(config['INPUTS']['binance_X'])) or(position=="long" and ltp<price1-price1*(float(config['INPUTS']['stop_loss_precentage']))/100/int(config['INPUTS']['binance_X'])):
            signal="squareoffsell"

        if (position=="short" and ltp<price2-price2*(float(config['INPUTS']['take_profit_precentage']))/100/int(config['INPUTS']['binance_X'])) or(position=="short" and ltp>price2+price2*(float(config['INPUTS']['stop_loss_precentage']))/100/int(config['INPUTS']['binance_X'])):
            signal="squareoffbuy"




    if signal=='buy':
        market_order()

        bot.sendMessage(1039725953,f"New long position initiated at {price1}")

    if signal=='sell':
        market_order1()

        bot.sendMessage(1039725953,f"New short position initiated at {price2}")
    
    if signal=="squareoffsell":
        market_order1()

        position=""
        bot.sendMessage(1039725953,f"long position squared of at {price2}")
        bot.sendMessage(1039725953,f" profit of {((price2-price1)/price1)*100*int(config['INPUTS']['binance_X'])}")
    if signal=="squareoffbuy":
        market_order()

        position=""
        bot.sendMessage(1039725953,f"short position squared of at {price2}")
        bot.sendMessage(1039725953,f" profit of {((price2-price1)/price1)*100*int(config['INPUTS']['binance_X'])}")
    # while True:
    #     if time.time()>=times1+300:
    #         break
        
    #     ltp=ltp_price(config['INPUTS']['symbol_binance'])


    #     if (position=='long' and ltp>price1+price1*(float(config['INPUTS']['take_profit_precentage']))/100/20) or(position=='long' and ltp<price1-price1*(float(config['INPUTS']['stop_loss_precentage']))/100/20):
    #         market_order1()
    #         bot.sendMessage(1039725953,"long position squared off by 2.5/5 rule")
    #         bot.sendMessage(1039725953,f" profit of {((ltp-price1)/price1)*100*20}")


            
    #         position=""
    #     if (position=='short' and ltp<price2-price2*(float(config['INPUTS']['take_profit_precentage']))/100/20) or(position=='short' and ltp>price2+price2*(float(config['INPUTS']['stop_loss_precentage']))/100/20):
    #         market_order()
    #         position=""
    #         bot.sendMessage(1039725953,"short position squared off by 2.5/5 rule")
    #         bot.sendMessage(1039725953,f" profit of {((ltp-price2)/price2)*100*20}")
            
  



# %%

l=0
price1=0
price2=0


while True:
        
    try:
        main()
        print("hello")
    except Exception as e:
        botss=str(e)

        bot.sendMessage(1039725953,botss)
