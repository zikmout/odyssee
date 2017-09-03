import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py
import plotly.graph_objs as go
import pandas_datareader.data as web
from datetime import datetime

import math
#hl Time, avg, max, min
#vol Time, price, volume

def test_run():
    df_vol = pd.read_csv('../data/bitcoinity_data_vol.csv', parse_dates=True)
    df_hl = pd.read_csv('../data/bitcoinity_data_hl.csv')
    df_ma5 = pd.read_csv('../data/bitcoinity_data_ma5.csv')
    df_ma10 = pd.read_csv('../data/bitcoinity_data_ma10.csv')
    df_ma20 = pd.read_csv('../data/bitcoinity_data_ma20.csv')
    #df[['max', 'min']].plot()


    # Time, price, volume, max, min
    print(df_hl.loc[:, 'max':'min'])

    df = pd.concat([df_vol, df_hl.loc[:, 'max':'min']], axis=1)
    df = df.reindex_axis(['Time', 'price', 'min', 'max', 'volume'], axis=1)
    #df['avg5'] = pd.rolling_std(df['price'], window=365) * math.sqrt(365)
    df['ma5'] = df.rolling(5).mean()['price']
    df['ma10'] = df.rolling(10).mean()['price']
    df['ma20'] = df.rolling(20).mean()['price']
    df['ma50'] = df.rolling(50).mean()['price']
    df['ma200'] = df.rolling(200).mean()['price']

    #df['return'] = df.std(axis=1)
    df['rstd7'] = pd.rolling_std(df['price'], 7, min_periods=1)
    df['rstd14'] = pd.rolling_std(df['price'], 14, min_periods=1)
    df['rstd28'] = pd.rolling_std(df['price'], 28, min_periods=1)

    df = np.round(df, decimals=1)
    #df = df.replace({' 00:00:00 UTC':''}, regex=True)
    df['Time'] = pd.to_datetime(df['Time'], yearfirst=True)

    #df = df.merge(df_ma20, left_index='Time', right_on='ron', left_on='lon', how='outer')
    #df2 = pd.concat([df, df_ma5], axis=1, join='inner')

    #df = pd.to_datetime(df['Time'])
    # Time, price, min, max, volume

    print(df)


    ax1=plt.subplot(2, 1, 1)
    df['price'].plot()

    ax1.plot(df['price'])

    ax2=plt.subplot(2, 1, 2)
    df['volume'].plot()
    plt.show()

    #df2 = df.set_index("Time")
    #df2 = np.round(df2, decimals=1)
    #print(df2.loc[:, 'avg':'min'])

    #df = df2
    #df[0:, 3:].astype(float, copy=True, erros='raise')
    #trace = go.Candlestick(x=df.index,
    #                        open=df.avg,
    #                        high=df.max,
    #                        low=df.min)
    #data = [trace]
    #print(df)

    #py.iplot(data, filename='simple_candlestick')
    #plt.show()

if __name__ == "__main__":
    test_run()
