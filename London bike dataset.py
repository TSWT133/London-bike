import pandas as pd
import kaggle
import zipfile

zipfile_name = "london-bike-sharing-dataset.zip"
with zipfile.ZipFile(zipfile_name, "r") as file:
    file.extractall()

london_bike_df = pd.read_csv("london_merged.csv")

print(london_bike_df.head())
print(london_bike_df.info())
print(london_bike_df.shape)

print(london_bike_df.weather_code.value_counts())
print(london_bike_df.wind_speed.value_counts())
print(london_bike_df.is_weekend.value_counts())
print(london_bike_df.season.value_counts())

col_dict = {
    "timestamp": "time",
     "cnt": "count",
     "t1": "real_temp",
     "t2": "temp_feels_like",
     "hum": "humidity_%",
     "wind_speed": "wind_kph",
     "weather_code": "weather",
     "is_holiday": "holiday",
     "is_weekend": "weekend",
     "season": "season"
     }

