import pandas as pd
import requests
import io

# Downloading the csv file from your GitHub account

# Make sure the url is the raw version of the file on GitHub
owid_covid_data_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'


#get and save csv file form online source. must use raw-csv url path.
#return pd data frame.
def pull_file(url):
    
    # get content from url.
    download = requests.get(url).content
    # Reading the downloaded content and turning it into csv 
    csv = io.StringIO(download.decode('utf-8'))
    df = pd.read_csv(csv, index_col=0, parse_dates=[3])
    return df

#split file by country and save as a new file. use isocode(uppercase) of country toget file only that country.
def get_by_country(isocode:str = 'THA' ):
    index = ['iso_code','continent','location','date']
    _df = pd.read_csv('./source/owid_covid_data.csv')
    _df = _df.set_index(index)
    _df = _df.loc[isocode]
    return _df, isocode

    
#save world csv file.
pull_file(owid_covid_data_url).to_csv('./source/owid_covid_data.csv')  

#save thai csv file.
df ,_isocode = get_by_country('THA')
df.to_csv('./source/{}_covid_data.csv'.format(_isocode))

df ,_isocode = get_by_country('IND')
df.to_csv('./source/{}_covid_data.csv'.format(_isocode))
