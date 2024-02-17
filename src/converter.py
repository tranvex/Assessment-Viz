import pandas as pd
import os

def xls_to_csv(file_name):
    # Read the excel file
   data = pd.read_excel(file_name)
   csv_filename = os.path.splitext(file_name)[0] + '.csv'
   data.to_csv(csv_filename, index=False)

