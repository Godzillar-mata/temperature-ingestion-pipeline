import os
from dotenv import load_dotenv

# credentail details
load_dotenv()
api_url = os.getenv("api_key")
host_name = os.getenv("host_name")
user_name = os.getenv("user_name")
user_password = os.getenv("user_password")
db_name = os.getenv("db_name")
port = os.getenv("port")
table = os.getenv("table")