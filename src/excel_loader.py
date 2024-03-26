import pandas as pd


# Define a class named ExcelLoader
class ExcelLoader:

    # Initialize the class with a file name
    def __init__(self, file_name):
        # Store the file path
        self.file_name = file_name
        # Prepare a dictionary to hold data from all sheets
        self.all_sheets = {}

    # Define a method to load the Excel file
    def load_excel(self):
        try:
            # Use pandas to read the Excel file. sheet_name=None loads all sheets.
            self.all_sheets = pd.read_excel(self.file_name, sheet_name=None)
            # Print a success message
            print(f"All sheets loaded successfully from '{self.file_name}'.")
        except Exception as e:
            # If there's an error (e.g., file not found), print an error message.
            print(f"An error occurred while loading the file: {e}")

    # Define a method to get the names of all sheets in the Excel file
    def get_sheet_names(self):
        # Return the keys of the all_sheets dictionary, which are the sheet names.
        return list(self.all_sheets.keys())

    # Define a method to get the data from a specific sheet
    def get_sheet_data(self, sheet_name):
        try:
            # Access the data for the specified sheet
            df = self.all_sheets[sheet_name]
            # Return the data
            return df
        except Exception as e:
            # Print error message if sheet not found
            print(f"An error occurred while accessing the sheet: {e}")
