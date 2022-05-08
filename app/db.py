import os

import pandas as pd
import pymysql
from sqlalchemy import create_engine

host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
port = os.getenv('MYSQL_PORT')
passwd = os.getenv('MYSQL_PW')
database = os.getenv('MYSQL_DATABASE')
connection = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}")    

def get_jobs():
    with open(os.getenv('MYSQL_QUERY_FILEPATH')) as file:
        return pd.read_sql(file.read(), connection)