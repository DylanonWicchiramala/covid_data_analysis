#this class for visualize covid data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import source.data as data

class plot():
    def main(self):
        self.ax.set_ylabel(self.col)
        self.ax.set_title(self.isocode)
        self.ax.plot(self.dat)
    
    def set_dat(isocode, col = 'new_cases'):
        arr = world_df.loc[isocode][col].to_numpy()
        return arr
    
    def __init__(self, X:np.array, index = None):
        # self.dat = np.array(self.dat)
        self.fig, self.ax = plt.subplots()
        self.main()
        plt.show()

    def diff(self):
        self.ax.bar(range(len(dat)-1),np.diff(dat))
    
    def rate(self):
        pass


from source.data import world_df
arr = world_df.loc['THA']['new_cases'].to_numpy()
plot(arr)