# Database connection using mysql.connector
import mysql.connector
from mysql.connector import Error

def create_mysql_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connect to database successfully")
    except Error as e:
        print(f"Failed to connect database : {e}!!!")
        raise
    
    return connection


# Database connection using sqlalchemy
from sqlalchemy import create_engine

def mysql_connection(user, pwd, host,port, database):
    try:
        engine = create_engine(f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{database}")
        return engine
    except Exception as e:
        print(f"Failed to connect MySQL database : {e} !!!")
        raise