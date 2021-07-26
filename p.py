import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

from data import thai_df, world_df
df = world_df

# df = df.set_index(['iso_code','continent','location','date'])
df = df.set_index(['iso_code'])
df = df[:]
# df = df.T
print(df)