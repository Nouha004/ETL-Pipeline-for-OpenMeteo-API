#packages to import 
import json
import requests
import pandas as pd
from datetime import datetime
import psycopg2
from sqlalchemy import create_engine


#EXTRACT
#get info from the API (open meteo)
url = "https://archive-api.open-meteo.com/v1/era5?latitude=34.0123&longitude=-6.8326&start_date=2021-01-01&end_date=2021-12-31&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=auto"


response= requests.get(url)
data = response.json()

#TRANSFROM

def to_fr(temp):
  return temp * 9/5 + 32

weather_data = []

for i in range(len(data['hourly']['time'])):
# two date types for further use
    if isinstance(data['hourly']['time'][i], int):  # For integer timestamps (unix)
        date_time = datetime.utcfromtimestamp(data['hourly']['time'][i])
    else:  # For string dates in ISO8601 format (this is what is used here)
        date_time = datetime.strptime(data['hourly']['time'][i], '%Y-%m-%dT%H:%M')

    day = date_time.strftime('%d-%m-%Y')
    time = date_time.strftime('%H:%M:%S')

    temp_f = to_fr(data['hourly']['temperature_2m'][i])
    temp = data['hourly']['temperature_2m'][i]
    humidity = data['hourly']['relative_humidity_2m'][i]
    wind_speed = data['hourly']['wind_speed_10m'][i]

    temp_f=round(temp_f,2)
    temp=round(temp,2)
    humidity=round(humidity,2)
    wind_speed=round(wind_speed,2)

    # Append to the weather_data 
    weather_data.append({
        "DayofYear":day,
        "Time":time,
        "Temp_C": temp,
        "Temp_F": temp_f,
        "Humidity": humidity,
        "WindSpeed(Km/h)": wind_speed

    })
    df = pd.DataFrame(weather_data)
print(df)

#LOAD TO POSTGRES DB

user='postgres'
password='######'
host= 'localhost'
port='5432'
database='postgres'

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}', echo=True)

df.to_sql('Weather', engine, if_exists='replace', index=False)

engine.dispose()




