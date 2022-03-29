import requests
import pandas as pd


df = pd.read_csv(r'C:\Users\jwpow\data_science\Final Project\Data Dumps JSON\right_move_data_post_code.csv')
APP_KEY = 'd06158cae03945fc85ef0115cd660584'
STOP_TYPE = 'NaptanMetroStation'
RADIUS = 2000

nearest_station = []
number_of_stations = []

for i in range(5500, 6500):
    LONG = df['longitude'][i]
    LAT = df['latitude'][i]
    URL = f'https://api.tfl.gov.uk/StopPoint/?lat={LAT}&lon={LONG}&stopTypes={STOP_TYPE}&radius={RADIUS}&app_key={APP_KEY}'
    r = requests.get(URL).json()

    if len(r['stopPoints']) < 1:
        nearest_station.append('Nothing within a 2km radius')
        number_of_stations.append(0)
    else:
        nearest_station.append(r['stopPoints'][0]['distance'])
        number_of_stations.append(len(r['stopPoints']))

df_stops = pd.DataFrame({'nearest stattion': nearest_station, 'number of stops within 2kms': number_of_stations})
df_stops.to_csv(r'C:\Users\jwpow\data_science\Final Project\Data Dumps JSON\tfl_data_4.csv')

