from app.config import api_url, host_name , user_name, user_password, db_name, port, table
from app.api import fetch_api_data
from app.db import mysql_connection
from app.data_mani import tranfrom_api_data_weather
from app.data_inges import insert_to_db

def run_pipeine():
    try:
        # fetch data from API
        raw_data = fetch_api_data(api_url)
        
        # Transform data from json form to structure data
        cleaned_data = tranfrom_api_data_weather(raw_data)

        # connect to MySQL database
        conn = mysql_connection(
            user=user_name,
            pwd=user_password,
            host=host_name,
            port=port,
            database=db_name
        )

        # insert data to MySQL database
        insert_to_db(cleaned_data, table, conn)

        print("Pipeline run successfully")
    except Exception as e:
        print(f"Pipeline failed : {e} !!!")

    finally:
        try:
            conn.close()
            print("MySQL connection closed")
        except:
            pass


if __name__ == "__main__":
    run_pipeine()
    