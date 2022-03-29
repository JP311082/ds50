import requests
from collections import Counter
import pandas as pd

df = pd.read_csv(r'C:\Users\jwpow\data_science\Final Project\Data Dumps JSON\right_move_data_wip.csv')
DATE = '2022-01'
crime_rates = []

for i in range(0, len(df)):
    LONG = df['longitude'][i]
    LAT = df['latitude'][i]
    URL = f'https://data.police.uk/api/crimes-street/all-crime?lat={LAT}&lng={LONG}&date={DATE}'
    r = requests.get(URL).json()
    crime_rates.append(Counter(player['category'] for player in r))
