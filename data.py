import pandas as pd

thai_csv = pd.read_csv('./source/thailand_covid.csv')
thailand_covid_csv = thai_csv
world_csv = pd.read_csv('./source/owid_covid_data.csv')
owid_covid_data_csv = world_csv

thai_df = pd.DataFrame(thai_csv)
thailand_covid_df = thai_df
world_df = pd.DataFrame(world_csv)
owid_covid_data_df = world_df


index = ['iso_code','continent','location','date']
thai_df = thai_df.set_index(index)
world_df = world_df.set_index(index)

thai_df = thai_df.fillna(0)
world_df = world_df.fillna(0)


# NOTE: useless.
def get(isocode:str):
    global world_df
    return world_df.loc[isocode] 