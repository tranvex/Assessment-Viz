import pandas as pd
import os


def xls_to_csv(file_name, output_directory=""):
    try:
        # Read all sheets from the Excel file
        all_sheets = pd.read_excel(file_name, sheet_name=None)

        # Iterate through each sheet and write to a separate CSV file
        for sheet_name, data in all_sheets.items():
            csv_filename = os.path.join(output_directory, f'{os.path.splitext(os.path.basename(file_name))[0]}_{sheet_name}.csv')
            data.to_csv(csv_filename, index=False)
            print(f"CSV file '{csv_filename}' created successfully for sheet '{sheet_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

'''original code'''
# def xls_to_csv(file_name):
#     # Read the excel file
#    data = pd.read_excel(file_name)
#    csv_filename = os.path.splitext(file_name)[0] + '.csv'
#    data.to_csv(csv_filename, index=False)