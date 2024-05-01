import pandas as pd
from PyQt6.QtWidgets import QMessageBox

class DataLoader:
    def __init__(self, file_name=None):
        self.file_name = file_name
        self.data = None

    def load_data(self):
        if not self.file_name:
            self.error_message("Filename not provided.")
            return

        try:
            self.data = pd.read_excel(self.file_name, sheet_name=None)
            print(f"Loaded sheets: {list(self.data.keys())}")
        except Exception as e:
            self.error_message(f"An error occurred while loading the file: {e}")

    def load_csv_data(self):
        """
        Loads data from a CSV file.
        """
        try:
            self.data = {'Sheet1': pd.read_csv(self.file_name)}
            if self.data['Sheet1'].empty:
                self.error_message("CSV file is empty or formatted incorrectly.")
            else:
                print("CSV file loaded successfully.")
        except Exception as e:
            self.error_message(f"An error occurred while loading the CSV file: {e}")

    def get_measures(self):
        # Assuming 'Sheet1' is not hardcoded
        if self.data:
            first_sheet_name = next(iter(self.data.keys()))
            sheet_data = self.data[first_sheet_name]
            if 'Measures' in sheet_data.columns:
                return sheet_data['Measures'].dropna().unique().tolist()
        return []

    def error_message(self, message):
        """
        Displays an error message in a dialog box.
        """
        QMessageBox.critical(None, 'Data Loading Error', message)

    def convert_sheets_to_csv(self):
        if not self.data:
            self.error_message("No data loaded to convert.")
            return
        
        base_path = self.file_name.rsplit('.', 1)[0]
        for sheet_name, df in self.data.items():
            csv_file_name = f"{base_path}_{sheet_name}.csv"
            df.to_csv(csv_file_name, index=False)
            print(f"Converted {sheet_name} to CSV file at {csv_file_name}.")
            
    def get_sheet_names(self):
        if self.data:
            return list(self.data.keys())
        return []
    
    def get_sheet_data(self, sheet_name):
        """
        Returns the data for a specified sheet.
        """
        if self.data and sheet_name in self.data:
            return self.data[sheet_name]
        else:
            self.error_message(f"No data found for sheet: {sheet_name}")
            return None  # Or handle differently based on your error management strategy
        
    def error_message(self, message):
        QMessageBox.critical(None, 'Data Loading Error', message)