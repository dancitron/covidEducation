import requests
import pandas as pd
from pandas import json_normalize




responseJson = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations?source=csbs')
response = (responseJson.json())

df = json_normalize(response["locations"])

df['county'] = df['county'] + ' County, ' + df['province'] 
print(df)
        

df.to_csv('../extracts/coronaCases.csv')
