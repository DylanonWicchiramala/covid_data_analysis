import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

from source.data import thai_df, world_df
df = world_df.loc['IND']
Tdf = thai_df


def plot(isocode, col = 'new_cases'):
    df = world_df.loc[isocode]
    case = df[col].to_numpy()
    case = np.array(case)
    plt.plot(case)
    plt.bar(range(len(case)-1),np.diff(case))
    plt.show()

plt.figure()
plot('IND')
plt.figure()
plot('THA')
plt.figure()
plot('USA')
