# Importing libraries
import pandas as pd
import kaggle
import zipfile

# Extracting dataset from zip file
zipfile_name = "london-bike-sharing-dataset.zip"
with zipfile.ZipFile(zipfile_name, "r") as file:
    file.extractall()

london_bike_df = pd.read_csv("london_merged.csv")

# Identifying the structure and info in the dataset
print(london_bike_df.head())
print(london_bike_df.info())
print(london_bike_df.shape)

# Counting unique values in relevant columns
print(london_bike_df.weather_code.value_counts())
print(london_bike_df.is_weekend.value_counts())
print(london_bike_df.is_holiday.value_counts())
print(london_bike_df.season.value_counts())

# Defining new column names for clearer description
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

# Renamed columns using the dictionary above
london_bike_df.rename(col_dict, axis=1, inplace=True)

# Mapping integer values of specified columns to string values
weather_dict = {"1.0": "clear", "2.0": "scattered clouds",
    "3.0": "broken clouds",
    "4.0": "cloudy",
    "7.0": "rain",
    "10.0": "rain with thunderstorm",
    "26.0": "snowfall"
    }
season_dict = {
    "0.0": "spring", 
    "1.0": "summer", 
    "2.0": "autumn", 
    "3.0": "winter"
    }
holiday_dict = {"0.0": "no", "1.0": "yes"}
weekend_dict = {"0.0": "no", "1.0": "yes"}

# Changing column data type and mapping the key:values of dictionaries above
london_bike_df.weather = london_bike_df.weather.astype("str")
london_bike_df.weather = london_bike_df.weather.map(weather_dict)

london_bike_df.season = london_bike_df.season.astype("str")
london_bike_df.season = london_bike_df.season.map(season_dict)

london_bike_df.holiday = london_bike_df.holiday.astype("str")
london_bike_df.holiday = london_bike_df.holiday.map(holiday_dict)

london_bike_df.weekend = london_bike_df.weekend.astype("str")
london_bike_df.weekend = london_bike_df.weekend.map(weekend_dict)

print(london_bike_df.head())




