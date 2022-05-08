import os
from datetime import date
from pprint import pprint

from dotenv import load_dotenv
load_dotenv()

from db import get_jobs
from gsheets import upload_dataframe

jobs = get_jobs()
upload_dataframe(jobs)
