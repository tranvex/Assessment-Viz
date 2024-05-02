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
            if not self.data.keys():
                self.error_message("No sheets found in the file.")
            else:
                print(f"Data loaded successfully from {self.file_name} with sheets: {list(self.data.keys())}")
        except Exception as e:
            self.error_message(f"An error occurred while loading the file: {e}")

    def get_measures(self, sheet_name=None):
        if self.data:
            sheet_name = sheet_name or next(iter(self.data.keys()), None)
            if sheet_name and sheet_name in self.data:
                sheet_data = self.data[sheet_name]
                if 'Measures' in sheet_data.columns:
                    return sheet_data['Measures'].dropna().unique().tolist()
            else:
                self.error_message(f"No valid sheet found or specified: {sheet_name}")
        return []

    def error_message(self, message):
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
        return list(self.data.keys()) if self.data else []

    def get_sheet_data(self, sheet_name):
        if self.data and sheet_name in self.data:
            return self.data[sheet_name]
        else:
            self.error_message(f"No data found for sheet: {sheet_name}")
            return None