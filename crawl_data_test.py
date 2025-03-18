
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import plotly.express as px

url =  "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2024-06-30&end_date=2024-07-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url2 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2024-06-01&end_date=2024-06-30&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url3 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2024-05-31&end_date=2024-06-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url4 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2024-05-01&end_date=2024-05-31&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url5 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2024-04-30&end_date=2024-05-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url6 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2024-04-01&end_date=2024-04-30&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url7 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2024-03-031&end_date=2024-04-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url8 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2024-02-28&end_date=2024-03-31&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url9 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2024-02-01&end_date=2024-02-28&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url10 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2024-01-31&end_date=2024-02-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
url11 = "https://api.weatherbit.io/v2.0/history/airquality?city=Hanoi&start_date=2024-01-01&end_date=2024-01-31&tz=local&key=59db8247551b4dad8cdb799e349d7f32"

data = requests.get(url)
results = json.loads(data.text)
data2 = requests.get(url2)
results2 = json.loads(data2.text)
data3 = requests.get(url3)
results3 = json.loads(data3.text)
data4 = requests.get(url4)
results4 = json.loads(data4.text)
data5 = requests.get(url5)
results5 = json.loads(data5.text)
data6 = requests.get(url6)
results6 = json.loads(data6.text)
data7 = requests.get(url7)
results7 = json.loads(data7.text)
data8 = requests.get(url8)
results8 = json.loads(data8.text)
data9 = requests.get(url9)
results9 = json.loads(data9.text)
data10 = requests.get(url10)
results10 = json.loads(data10.text)
data11 = requests.get(url11)
results11 = json.loads(data11.text)
results['city_name']
results['country_code']
results['data'][0]
results['data'][-1]
joined_data = results['data'] + results2['data'] + results3['data'] + results4['data'] + results5['data'] + results6['data'] + results7['data'] + results8['data'] + results9['data'] + results10['data'] + results11['data']
joined_results = {
    'city_name': results['city_name'],
    'country_code': results['country_code'],
    'lat': results['lat'],
    'lon': results['lon'],
    'timezone': results['timezone'],
    'data': joined_data
}
joined_results['data'][0]
joined_results['data'][-1]
df = pd.DataFrame(joined_results)
df.columns = ['City', 'Country code', 'Lat', 'Lon', 'timezone', 'Data']
df[['AQI', 'CO', 'Date Time', 'NO2', 'O3', 'PM10', 'PM25', 'SO2', 'Local Time', 'UTC Time', 'TS']] = pd.DataFrame(df['Data'].tolist())
df.drop(columns=['Data', 'Lat', 'Lon', 'TS', 'Date Time'], inplace=True)
df = df.drop_duplicates()
df = df.sort_values(by='Local Time')
df['Local Time'] = pd.to_datetime(df['Local Time'])
df.set_index('Local Time', inplace=True)
df.head()
df.info()

urlweath =  "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-06-30&end_date=2024-07-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
urlweath2 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-06-01&end_date=2024-06-30&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
urlweath3 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-05-31&end_date=2024-06-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
urlweath4 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-05-01&end_date=2024-05-31&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
urlweath5 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-04-30&end_date=2024-05-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
urlweath6 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-04-01&end_date=2024-04-30&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
urlweath7 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-03-031&end_date=2024-04-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
urlweath8 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-02-28&end_date=2024-03-31&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
urlweath9 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-02-01&end_date=2024-02-28&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
urlweath10 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-01-31&end_date=2024-02-01&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
urlweath11 = "https://api.weatherbit.io/v2.0/history/hourly?city=Hanoi&start_date=2024-01-01&end_date=2024-01-31&tz=local&key=59db8247551b4dad8cdb799e349d7f32"
data_w = requests.get(urlweath)
results_w = json.loads(data_w.text)
data_w2 = requests.get(urlweath2)
results_w2 = json.loads(data_w2.text)
data_w3 = requests.get(urlweath3)
results_w3 = json.loads(data_w3.text)
data_w4 = requests.get(urlweath4)
results_w4 = json.loads(data_w4.text)
data_w5 = requests.get(urlweath5)
results_w5 = json.loads(data_w5.text)
data_w6 = requests.get(urlweath6)
results_w6 = json.loads(data_w6.text)
data_w7 = requests.get(urlweath7)
results_w7 = json.loads(data_w7.text)
data_w8 = requests.get(urlweath8)
results_w8 = json.loads(data_w8.text)
data_w9 = requests.get(urlweath9)
results_w9 = json.loads(data_w9.text)
data_w10 = requests.get(urlweath10)
results_w10 = json.loads(data_w10.text)
data_w11 = requests.get(urlweath11)
results_w11 = json.loads(data_w11.text)
joined_data_weather = results_w['data'] + results_w2['data'] + results_w3['data'] + results_w4['data'] + results_w5['data'] + results_w6['data'] + results_w7['data'] + results_w8['data'] + results_w9['data'] + results_w10['data'] + results_w11['data'] 
joined_results_weather = {
    'city_name': results_w['city_name'],
    'country_code': results_w['country_code'],
    'lat': results_w['lat'],
    'lon': results_w['lon'],
    'timezone': results_w['timezone'],
    'data': joined_data_weather
}
df_weather = pd.DataFrame(joined_results_weather)
df_weather.columns = ['City', 'Country code', 'Lat', 'Lon', 'timezone', 'Data']
df_weather[['Apparent Temperature', 'Azimuth', 'Clouds', 'Datetime', 'Dew Point', 'DHI', 'DNI', 'Elevation Angle', 'GHI',
            'H Angle', 'Pod', 'Precipitation', 'Pressure', 'Status', 'Relative Humidity', 'Sea Level Pressure', 'Snow',
            'Solar Radiation', 'Temperature', 'Local Time', 'UTC Time', 'Timestamp', 'UV Index', 'Visibility', 'Weather',
            'Wind Direction', 'Wind Gust Speed', 'Wind Speed']] = pd.DataFrame(df_weather['Data'].tolist())
df_weather.drop(columns=['Data', 'Lat', 'Lon', 'Apparent Temperature', 'Azimuth','Datetime', 'Dew Point', 'DHI', 'DNI',
                         'Elevation Angle', 'GHI', 'H Angle', 'Pod', 'Status', 'Sea Level Pressure', 'Snow',
                         'Solar Radiation', 'Timestamp', 'Visibility', 'Wind Direction', 'Wind Gust Speed', 'Weather'], inplace=True)
df_weather = df_weather.drop_duplicates()
df_weather = df_weather.sort_values(by='Local Time')
df_weather['Local Time'] = pd.to_datetime(df_weather['Local Time'])
df_weather.set_index('Local Time', inplace=True)
df_weather = df_weather[:-23]
merged_df = pd.merge(df, df_weather, left_index=True, right_index=True)
merged_df.drop(columns=['City_y', 'Country code_y', 'timezone_y', 'UTC Time_y'], inplace=True)
utc_time_column = merged_df.pop('UTC Time_x')
merged_df.insert(0, 'UTC Time', utc_time_column)
merged_df = merged_df.rename(columns={'City_x': 'City', 'Country code_x': 'Country Code', 'timezone_x':'Timezone'})
merged_df
merged_df.to_csv('hanoi-aqi-weather-data_2024_1.csv')
