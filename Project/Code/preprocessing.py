import pandas as pd 
import numpy as np


class PreProcessing:
    def __init__(self):
        pass

    def load_csv(self):
        dataset = pd.read_csv('../bakarydata/Feuil1-Table 1.csv')
        data = dataset.dropna(how='all').to_numpy()
        data = data[:-2]
        columns = dataset.columns.to_numpy()
        columns[-1] = 'Type de roche'
        df = pd.DataFrame(data[:, 2:], columns = columns[2:])
        df.to_csv('../bakarydata.csv', index=False)


preProcess = PreProcessing()
preProcess.load_csv()