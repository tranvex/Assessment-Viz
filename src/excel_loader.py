import pandas as pd

class ExcelLoader:
    """
    Class to load and access data from an Excel file.
    """
    def __init__(self, file_name):
        """
        Initializes the ExcelLoader with the path to the Excel file.
        """
        self.file_name = file_name  # Store the file path
        self.all_sheets = {}  # Prepare a dictionary to hold data from all sheets
        
    def load_excel(self):
        """
        Loads all sheets from the Excel file into the all_sheets dictionary.
        """
        try:
            # Use pandas to read the Excel file. This function returns a dictionary
            # where each key is a sheet name and its value is a DataFrame of the sheet's data.
            self.all_sheets = pd.read_excel(self.file_name, sheet_name=None)
            print(f"All sheets loaded successfully from '{self.file_name}'.")
        except Exception as e:
            # If there's an error (e.g., file not found), print an error message.
            print(f"An error occurred while loading the file: {e}")
            
    def get_sheet_names(self):
        """
        Returns a list of sheet names from the loaded Excel file.
        """
        # Return the keys of the all_sheets dictionary, which are the sheet names.
        return list(self.all_sheets.keys())
    
    def get_sheet_data(self, sheet_name):
        """
        Returns the data for a specified sheet as a DataFrame.
        """
        try:
            # Check if sheet_name is in all_sheets dictionary
            # Returns DataFrame for corresponding sheet if present in dictionary
            df = self.all_sheets[sheet_name]
            return df
        except Exception as e:
            # Print error message if sheet not found
            print(f"An error occurred while accessing the sheet: {e}")