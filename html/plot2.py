import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py
import plotly.graph_objs as go
import pandas_datareader.data as web
from datetime import datetime

import mpl_finance as mpf

import json

class FileItem(dict):
    def __init__(self, fname):
        dict.__init__(self, fname=fname)

#f = open('../data/bitcoinity_data.csv', 'r+')
#print(json.dumps(f))

#hl Time, avg, max, min
#vol Time, price, volume

def test_run():
    df_vol = pd.read_csv('../data/bitcoinity_data_vol.csv')
    df_hl = pd.read_csv('../data/bitcoinity_data_hl.csv')
    df_ma5 = pd.read_csv('../data/bitcoinity_data_ma5.csv')
    df_ma10 = pd.read_csv('../data/bitcoinity_data_ma10.csv')
    df_ma20 = pd.read_csv('../data/bitcoinity_data_ma20.csv')
    #df[['max', 'min']].plot()


    # Time, price, volume, max, min
    print(df_hl.loc[:, 'max':'min'])

    df = pd.concat([df_vol, df_hl.loc[:, 'max':'min']], axis=1)
    df = df.reindex_axis(['Time', 'price', 'min', 'max', 'volume'], axis=1)
    df = np.round(df, decimals=1)
    df = df.replace({' 00:00:00 UTC':''}, regex=True)
    df['Time'] = pd.to_datetime(df['Time'], yearfirst=True)
    #df2 = pd.concat([df, df_ma5], axis=0)
    #df = pd.to_datetime(df['Time'])
    # Time, price, min, max, volume

    print(df)

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
