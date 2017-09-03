import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py
import plotly.graph_objs as go
import pandas_datareader.data as web
from datetime import datetime

import math
from matplotlib import style
#hl Time, avg, max, min
#vol Time, price, volume

style.use('ggplot')

def test_run():
    df_vol = pd.read_csv('../data/bitcoinity_data_vol.csv')
    df_hl = pd.read_csv('../data/bitcoinity_data_hl.csv')
    df_ma5 = pd.read_csv('../data/bitcoinity_data_ma5.csv')
    df_ma10 = pd.read_csv('../data/bitcoinity_data_ma10.csv')
    df_ma20 = pd.read_csv('../data/bitcoinity_data_ma20.csv')

    # Time, price, volume, max, min
    print(df_hl.loc[:, 'max':'min'])

    df = pd.concat([df_vol, df_hl.loc[:, 'max':'min']], axis=1)
    df = df.reindex_axis(['Time', 'price', 'min', 'max', 'volume'], axis=1)
    df['ma5'] = df.rolling(5).mean()['price']
    df['ma10'] = df.rolling(10).mean()['price']
    df['ma20'] = df.rolling(20).mean()['price']
    df['ma50'] = df.rolling(50).mean()['price']
    df['ma200'] = df.rolling(200).mean()['price']
    df['rstd7'] = pd.rolling_std(df['price'], 7, min_periods=1)
    df['rstd14'] = pd.rolling_std(df['price'], 14, min_periods=1)
    df['rstd28'] = pd.rolling_std(df['price'], 28, min_periods=1)
    df['volume'] = df['volume'] / 1000
    df = np.round(df, decimals=1)
    #df = df.replace({' 00:00:00 UTC':''}, regex=True)
    df['Time'] = pd.to_datetime(df['Time'], yearfirst=True)
    print(df)

    #Ploting data
    ax1=plt.subplot(2, 1, 1)
    plt.plot(df['Time'], df['price'], label='price')
    plt.plot(df['Time'], df['ma5'], label='ma5')
    plt.plot(df['Time'], df['ma10'], label='ma10')
    plt.legend(loc="upper left", bbox_to_anchor=[0, 1],
                       ncol=2, shadow=True, title="Legend", fancybox=True)
    ax1.get_legend().get_title().set_color("blue")

    plt.gcf().autofmt_xdate()
    plt.title('Price')
    plt.ylabel('E')

    #ax1.plot(df['price'])

    ax2=plt.subplot(2, 1, 2, sharex = ax1)
    plt.plot(df['Time'], df['volume'])
    plt.gcf().autofmt_xdate()

    plt.title('Volumes')
    plt.ylabel('kBTC')
    plt.xlabel('time')
    plt.show()

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
