import pandas as pd
from app.api import fetch_api_data

# tranform columns from json format to structured data for weather data
def tranfrom_api_data_weather(data):
    try:
        df_weather = pd.DataFrame({
            "time": data["hourly"]["time"],
            "temp": data["hourly"]["temperature_2m"]
        })
        return df_weather
    except Exception as e:
        print(f"Failed to clean data : {e} !!!")
        raise

    
# def tranfrom_api_data_weather(url):
#     try:
#         data = fetch_api_data(url)
#         df_weather = pd.DataFrame({
#             "time": data["hourly"]["time"],
#             "temp": data["hourly"]["temperature_2m"]
#         })
#         return df_weather
#     except Exception as e:
#         print(f"Failed to clean data : {e} !!!")



    