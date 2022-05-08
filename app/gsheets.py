from os import getenv

import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

def upload_dataframe(df):
    gc = gspread.service_account(filename=getenv('SERVICE_ACCOUNT_FILEPATH'))
    gsheet = gc.open_by_key(getenv('GSHEET_ID'))
    worksheet = gsheet.worksheet(getenv('GSHEET_WORKSHEET'))

    worksheet.clear()
    set_with_dataframe(worksheet=worksheet, dataframe=df, include_index=False, include_column_header=True, resize=True)
    return True

