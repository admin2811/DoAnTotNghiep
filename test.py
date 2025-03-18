import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

plt.ion()

url =  "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-04-01&end_date=2023-04-30&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url2 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-03-01&end_date=2023-03-31&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url3 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-02-01&end_date=2023-02-28&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
#url4 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-11-01&end_date=2023-12-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
#url5 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-10-01&end_date=2023-11-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
#url6 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-09-01&end_date=2023-10-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
#url7 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-08-01&end_date=2023-09-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
#url8 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-07-01&end_date=2023-08-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
#url9 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-06-01&end_date=2023-07-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
#url10 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-05-01&end_date=2023-06-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
#url11 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-03-01&end_date=2023-04-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
#url12 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2023-01-01&end_date=2023-02-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"

#Parse JSON data from 08/02/2024 to 08/03/2024
data = requests.get(url)
results = json.loads(data.text)
#Parse JSON data from 08/01/2024 to 08/02/2024
data2 = requests.get(url2)
results2 = json.loads(data2.text)
#Parse JSON data from 08/12/2023 to 08/01/2024
data3 = requests.get(url3)
results3 = json.loads(data3.text)
#Parse JSON data from 08/11/2023 to 08/12/2023
#data4 = requests.get(url4)
#results4 = json.loads(data4.text)
#Parse JSON data from 08/10/2023 to 08/11/2023
#data5 = requests.get(url5)
#results5 = json.loads(data5.text)
#Parse JSON data from 08/09/2023 to 08/10/2023
#data6 = requests.get(url6)
#results6 = json.loads(data6.text)
#Parse JSON data from 08/08/2023 to 08/09/2023
#data7 = requests.get(url7)
#results7 = json.loads(data7.text)
#Parse JSON data from 08/07/2023 to 08/08/2023
#data8 = requests.get(url8)
#results8 = json.loads(data8.text)
#Parse JSON data from 08/06/2023 to 08/07/2023
#data9 = requests.get(url9)
#results9 = json.loads(data9.text)
#Parse JSON data from 08/05/2023 to 08/06/2023
#data10 = requests.get(url10)
#results10 = json.loads(data10.text)
#Parse JSON data from 08/04/2023 to 08/05/2023
#data11 = requests.get(url11)
#results11 = json.loads(data11.text)
#Parse JSON data from 08/03/2023 to 08/04/2023
#data12 = requests.get(url12)
#results12 = json.loads(data12.text)
results['city_name']
results['country_code']
#First element in "data" key
results['data'][0]
#Last element in "data" key
results['data'][-1]
print("Response 1:", results)
print("Response 2:", results2)
print("Response 3:", results3)

# Joining the 'data' keys from variables 
#joined_data = results['data'] + results2['data'] + results3['data'] + results4['data'] + results5['data'] + results6['data'] + results7['data'] + results8['data'] + results9['data'] + results10['data'] + results11['data'] + results12['data']
joined_data = results['data'] + results2['data'] + results3['data']
# Creating a new dictionary with the joined data
joined_results = {
    'city_name': results['city_name'],
    'country_code': results['country_code'],
    'lat': results['lat'],
    'lon': results['lon'],
    'timezone': results['timezone'],
    'data': joined_data
}
#First element in "data" key
joined_results['data'][0]
#Last element in "data" key
joined_results['data'][-1]
# Creating DataFrame
df = pd.DataFrame(joined_results)
# Renaming columns
df.columns = ['City', 'Country code', 'Lat', 'Lon', 'timezone', 'Data']
# Splitting 'Data' column into individual columns
df[['AQI', 'CO', 'Date Time', 'NO2', 'O3', 'PM10', 'PM25', 'SO2', 'Local Time', 'UTC Time', 'TS']] = pd.DataFrame(df['Data'].tolist())
# Dropping uneccessary columns
df.drop(columns=['Data', 'Lat', 'Lon', 'TS', 'Date Time'], inplace=True)
# Dropping duplicate columns
df = df.drop_duplicates()
# Sort local time 
df = df.sort_values(by='Local Time')
# Convert 'Local Time' column to datetime object
df['Local Time'] = pd.to_datetime(df['Local Time'])
# Set 'Local Time' column as index
df.set_index('Local Time', inplace=True)
df.head()
df.info()
print(df)
print(data.text)
df.to_csv("air_quality_hanoi_3.csv", index=True, encoding="utf-8-sig")


# urlweath = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-02-08&end_date=2024-03-09&tz=local&key=a17ac515f9b6411393c923e7abd376f5"
# urlweath2 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-01-08&end_date=2024-02-08&tz=local&key=a17ac515f9b6411393c923e7abd376f5"
# urlweath3 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2023-12-08&end_date=2024-01-08&tz=local&key=a17ac515f9b6411393c923e7abd376f5"
# urlweath4 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2023-11-08&end_date=2023-12-08&tz=local&key=a17ac515f9b6411393c923e7abd376f5"
# urlweath5 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2023-10-08&end_date=2023-11-08&tz=local&key=a17ac515f9b6411393c923e7abd376f5"
# urlweath6 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2023-09-08&end_date=2023-10-08&tz=local&key=a17ac515f9b6411393c923e7abd376f5"
# urlweath7 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2023-08-08&end_date=2023-09-08&tz=local&key=a17ac515f9b6411393c923e7abd376f5"
# urlweath8 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2023-07-08&end_date=2023-08-08&tz=local&key=a17ac515f9b6411393c923e7abd376f5"
# urlweath9 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2023-06-08&end_date=2023-07-08&tz=local&key=a17ac515f9b6411393c923e7abd376f5"
# urlweath10 = "https://api.weatherbit.io/v2.0/history/hourlyy?city=Hanoi&start_date=2023-05-08&end_date=2023-06-08&tz=local&key=a17ac515f9b6411393c923e7abd376f5"
# urlweath11 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2023-04-08&end_date=2023-05-08&tz=local&key=a17ac515f9b6411393c923e7abd376f5"
# urlweath12 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2023-03-08&end_date=2023-04-08&tz=local&key=a17ac515f9b6411393c923e7abd376f5"

# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w = requests.get(urlweath)
# results_w = json.loads(data_w.text)
# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w2 = requests.get(urlweath2)
# results_w2 = json.loads(data_w2.text)
# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w3 = requests.get(urlweath3)
# results_w3 = json.loads(data_w3.text)
# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w4 = requests.get(urlweath4)
# results_w4 = json.loads(data_w4.text)
# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w5 = requests.get(urlweath5)
# results_w5 = json.loads(data_w5.text)
# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w6 = requests.get(urlweath6)
# results_w6 = json.loads(data_w6.text)
# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w7 = requests.get(urlweath7)
# results_w7 = json.loads(data_w7.text)
# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w8 = requests.get(urlweath8)
# results_w8 = json.loads(data_w8.text)
# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w9 = requests.get(urlweath9)
# results_w9 = json.loads(data_w9.text)
# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w10 = requests.get(urlweath10)
# results_w10 = json.loads(data_w10.text)
# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w11 = requests.get(urlweath11)
# results_w11 = json.loads(data_w11.text)
# # Make an HTTP GET request to the specified URL and store the response in the data variable.
# data_w12 = requests.get(urlweath12)
# results_w12 = json.loads(data_w12.text)
# # Joining the 'data' lists from results and results2
# joined_data_weather = results_w['data'] + results_w2['data'] + results_w3['data'] + results_w4['data'] + results_w5['data'] + results_w6['data'] + results_w7['data'] + results_w8['data'] + results_w9['data'] + results_w10['data'] + results_w11['data'] + results_w12['data']
# # Creating a new dictionary with the joined data
# joined_results_weather = {
#     'city_name': results_w['city_name'],
#     'country_code': results_w['country_code'],
#     'lat': results_w['lat'],
#     'lon': results_w['lon'],
#     'timezone': results_w['timezone'],
#     'data': joined_data_weather
# }
# # Creating DataFrame
# df_weather = pd.DataFrame(joined_results_weather)

# # Renaming columns
# df_weather.columns = ['City', 'Country code', 'Lat', 'Lon', 'timezone', 'Data']

# # Splitting 'Data' column into individual columns
# df_weather[['Apparent Temperature', 'Azimuth', 'Clouds', 'Datetime', 'Dew Point', 'DHI', 'DNI', 'Elevation Angle', 'GHI',
#             'H Angle', 'Pod', 'Precipitation', 'Pressure', 'Status', 'Relative Humidity', 'Sea Level Pressure', 'Snow',
#             'Solar Radiation', 'Temperature', 'Local Time', 'UTC Time', 'Timestamp', 'UV Index', 'Visibility', 'Weather',
#             'Wind Direction', 'Wind Gust Speed', 'Wind Speed']] = pd.DataFrame(df_weather['Data'].tolist())
# # Dropping uneeded columns
# df_weather.drop(columns=['Data', 'Lat', 'Lon', 'Apparent Temperature', 'Azimuth','Datetime', 'Dew Point', 'DHI', 'DNI',
#                          'Elevation Angle', 'GHI', 'H Angle', 'Pod', 'Status', 'Sea Level Pressure', 'Snow',
#                          'Solar Radiation', 'Timestamp', 'Visibility', 'Wind Direction', 'Wind Gust Speed', 'Weather'], inplace=True)
# # Dropping duplicate columns
# df_weather = df_weather.drop_duplicates()
# # Sort local time 
# df_weather = df_weather.sort_values(by='Local Time')
# # Convert 'Local Time' column to datetime object
# df_weather['Local Time'] = pd.to_datetime(df_weather['Local Time'])
# # Set 'Local Time' column as index
# df_weather.set_index('Local Time', inplace=True)
# # Delete 23 bottom rows so that number of rows in weather dataframe is equal to number of rows in aqi dataframe
# df_weather = df_weather[:-23]
# df_weather
# #df.head()
# df_weather.info()

# #Merge two dataframes keeping the local datetime index
# merged_df = pd.merge(df, df_weather, left_index=True, right_index=True)
# #Drop duplicated columns
# merged_df.drop(columns=['City_y', 'Country code_y', 'timezone_y', 'UTC Time_y'], inplace=True)
# #Put UTC time column to the first column in the dataframe
# utc_time_column = merged_df.pop('UTC Time_x')
# merged_df.insert(0, 'UTC Time', utc_time_column)
# #Rename 4 columns
# merged_df = merged_df.rename(columns={'City_x': 'City', 'Country code_x': 'Country Code', 'timezone_x':'Timezone'})
# merged_df
# merged_df.info()
# merged_df.to_csv('hanoi-aqi-weather-data.csv')
