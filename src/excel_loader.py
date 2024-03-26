import pandas as pd

class ExcelLoader:
    
    def __init__(self, file_name):

        self.file_name = file_name  # Store the file path
        self.all_sheets = {}  # Prepare a dictionary to hold data from all sheets

    def load_excel(self):
        try:
            self.all_sheets = pd.read_excel(self.file_name, sheet_name=None)
            print(f"All sheets loaded successfully from '{self.file_name}'.")
        except Exception as e:
            # If there's an error (e.g., file not found), print an error message.
            print(f"An error occurred while loading the file: {e}")

    def get_sheet_names(self):
        # Return the keys of the all_sheets dictionary, which are the sheet names.
        return list(self.all_sheets.keys())

    def get_sheet_data(self, sheet_name):
        try:
            df = self.all_sheets[sheet_name]
            return df
        except Exception as e:
            # Print error message if sheet not found
            print(f"An error occurred while accessing the sheet: {e}")
