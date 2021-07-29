
# Libraries needed for the tutorial

import pandas as pd
import requests
import io

# Downloading the csv file from your GitHub account

# Make sure the url is the raw version of the file on GitHub
owid_covid_data_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'

def save_as(csv, path:str):
    #save csv file.
    pd.read_csv(csv, index_col=0, parse_dates=[3]).to_csv(path)


def pull_csv(url, path = None):
    
    # get content from url.
    download = requests.get(url).content
    # Reading the downloaded content and turning it into csv 
    csv = io.StringIO(download.decode('utf-8'))
    if path is not None:
        save_as(csv, path)


def pull_thai_csv():
    import data 
    pass 

pull_csv(owid_covid_data_url, './source/owid_covid_data.csv')  
