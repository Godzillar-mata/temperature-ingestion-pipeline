from datetime import datetime, timedelta
from airflow.decorators import task, dag
from airflow.operators.bash import BashOperator

# ## import project root
# import sys
# import os
# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(PROJECT_ROOT)

# import project configurations
from app.config import api_url, host_name , user_name, user_password, db_name, port, table

# import project function
from app.api import fetch_api_data
from app.db import mysql_connection
from app.data_mani import tranfrom_api_data_weather
from app.data_inges import insert_to_db

default_args = {
    'owner': 'matasit',
    'depends_on_past': False,
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=3),
    'schedule': '@daily',
}


# task1 - connect to api
@task()
def run_pipeline():
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
        raise
    finally:
        try:
            conn.close()
            print("MySQL connection closed")
        except:
            pass


# DAG
@dag(
    dag_id = "my_testing_dag",
    default_args=default_args, 
    schedule='@once', 
    start_date=datetime(2025,12,12), 
    tags=["workshop"]
)

def project_pipeline():
    t1 = run_pipeline()

    t1

project_pipeline()