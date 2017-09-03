import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def test_run():
    df = pd.read_csv('../data/bitcoinity_data.csv')
    df[['max', 'min']].plot()
    plt.show()

if __name__ == "__main__":
    test_run()
