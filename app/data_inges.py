import pandas as pd

# insert data from dataframe to MySQL database

def insert_to_db(data, table, engine):
    try:
        data.to_sql(name=table, con=engine, if_exists='append', index=False)
    except Exception as e:
        print(f"Falied to insert data to database : {e}!!!")
        raise

