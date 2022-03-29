import requests
import pandas as pd

df = pd.read_csv(r'C:\Users\jwpow\data_science\Final Project\Data Dumps JSON\right_move_data_wip.csv')
postcode = []
for i in range(0, 5):

    LONG = df['longitude'][i]
    LAT = df['latitude'][i]
    API = f'https://api.postcodes.io/postcodes?lon={LONG}&lat={LAT}'

    r = requests.get(API)
    # x = r.json()
    if r.json()['result'] != None:
        postcode.append([r.json()['result'][0]['postcode']])
    # elif r.status_code == 200 & [r.json()['result'] is not None:
    #     postcode.append([r.json()['result'][0]['postcode']])
    else:
        postcode.append('Not available')
postcode = pd.DataFrame(postcode, columns='postcode')
df1 = pd.DataFrame({'postcode': postcode})
df1.to_csv(r'C:\Users\jwpow\data_science\Final Project\Data Dumps JSON\postcodes.csv')
df.reindex()
df_postcode = pd.concat([df, df1], axis=1)
df_postcode.to_csv(r'C:\Users\jwpow\data_science\Final Project\Data Dumps JSON\right_move_data_wip.csv')
