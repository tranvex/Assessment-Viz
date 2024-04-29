import pandas as pd
from PyQt6.QtWidgets import *

class DataLoader:
    def __init__(self, file_name=None):
        """
        Initializes the DataLoader with an optional file name.
        """
        self.file_name = file_name
        self.data = None

    def load_data(self):
        """
        Loads data from the specified file, handling both Excel and CSV files.
        Checks the file extension to apply the correct pandas function.
        """
        if not self.file_name:
            return
        
        if self.file_name.endswith('.xlsx'):
            try:
                # Load all sheets if it's an Excel file
                self.data = pd.read_excel(self.file_name, sheet_name=None)
            except Exception as e:
                self.error_message(f"An error occurred while loading the Excel file: {e}")
        elif self.file_name.endswith('.csv'):
            try:
                # Load a single sheet if it's a CSV file
                self.data = {'Sheet1': pd.read_csv(self.file_name)}
            except Exception as e:
                self.error_message(f"An error occurred while loading the CSV file: {e}")
        else:
            self.error_message("Unsupported file format. Please load an Excel or CSV file.")

    def get_sheet_names(self):
        """
        Returns the names of sheets available in the loaded data.
        """
        if self.data:
            return list(self.data.keys())
        else:
            return []

    def get_sheet_data(self, sheet_name):
        """
        Retrieves the data for the specified sheet.
        """
        try:
            return self.data[sheet_name]
        except KeyError:
            self.error_message(f"Sheet named '{sheet_name}' does not exist.")
        except Exception as e:
            self.error_message(f"An error occurred while accessing the sheet: {e}")

    def error_message(self, message):
        """
        Displays an error message in a dialog box.
        """
        QMessageBox.critical(None, 'Error', message)