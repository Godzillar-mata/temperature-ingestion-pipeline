
Project structure

Pipeline API to MySQL/
| main.py
| config.py
| api.py
| db.py
| data_mani.py
| data_inges.py
| database.db
| requirement.txt
| .env
| .gitignore

------------------------------------------

Project detail
- Get data from free API that have daily update data
- Load data as JSON
- use MySQL for database
- insert data to database
- use Apache Spark & Apache Airflow for alchestration
- deploy on local computer using Docker
- # CI/CD is optional

------------------------------------------

work flow

weather data 
↓
api request
↓
json format 
↓
pandas clean data
↓
insert to database
↓
Apache Spark to queue
↓
Apache Airflow to monitor
↓
Docker to deploy