
# Libraries needed for the tutorial

import pandas as pd
import requests
import io
    
# Downloading the csv file from your GitHub account

url = "https://github.com/owid/covid-19-data/blob/6d183fb60cefeaf4ba36986e285217224bf69576/public/data/owid-covid-data.csv" # Make sure the url is the raw version of the file on GitHub
murl = 'https://github.com/owid/covid-19-data/blob/2542cc1ab51df8ecaa745c251daf79ee3912a10f/scripts/input/iso/iso.csv'
url = murl

download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Printing out the first 5 rows of the dataframe

print (df.head())