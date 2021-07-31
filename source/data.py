import pandas as pd
index = ['iso_code','continent','location','date']


world_csv = pd.read_csv('./source/owid_covid_data.csv', parse_dates=[3])
owid_covid_data_csv = world_csv

world_df = pd.DataFrame(world_csv)

world_df = world_df.set_index(index)

world_df = world_df.fillna(0)


thai_csv = pd.read_csv('./source/THA_covid_data.csv', parse_dates=[2])
thailand_covid_csv = thai_csv

thai_df = pd.DataFrame(thai_csv)

thai_df = thai_df.set_index(index[1:])

thai_df = thai_df.fillna(0)


