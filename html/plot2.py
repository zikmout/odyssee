import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py
import plotly.graph_objs as go
import pandas_datareader.data as web
from datetime import datetime

import sys
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
    #df[['max', 'min']].plot()


    # Time, price, volume, max, min
    #print(df_hl.loc[:, 'max':'min'])

    df = pd.concat([df_vol, df_hl.loc[:, 'max':'min']], axis=1)
    df = df.reindex_axis(['Time', 'price', 'min', 'max', 'volume'], axis=1)
    # Time, price, min, max, volume

    df[['price', 'min', 'max']] = np.round(df[['price', 'min', 'max']], 1)
    #df['volume'] = df.volume.astype(long)


    #print(type(sys.maxsize+1))
    print(df.dtypes)
    #df['Time'] = pd.to_datetime(pd.Series(['2017-08-08']), format="%Y-%m-%d")
    #df['volume'] = pd.to_numeric(df['volume'], errors='coerce').fillna(0)
    #df = np.round(df.loc[:, 'price':'max'], decimals=1)
    #df = np.round(df.loc[:, 'volume'], decimals=1)

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
