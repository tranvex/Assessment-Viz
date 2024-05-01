import pandas as pd
from PyQt6.QtWidgets import QMessageBox

class DataLoader:
    def __init__(self, file_name=None):
        """
        Initializes the DataLoader with an optional file name.
        """
        self.file_name = file_name
        self.data = None

    def load_data(self):
        """
        Loads data from the specified file, handling Excel files by reading all sheets.
        """
        if not self.file_name:
            self.error_message("Filename not provided.")
            return

        try:
            if self.file_name.endswith('.xlsx'):
                # Load all sheets if it's an Excel file
                self.data = pd.read_excel(self.file_name, sheet_name=None)  # Load all sheets
                self.convert_sheets_to_csv()  # Optionally convert all sheets to CSV
            elif self.file_name.endswith('.csv'):
                # Assuming there is only one sheet in CSV
                self.data = {'Sheet1': pd.read_csv(self.file_name)}
                if self.data['Sheet1'].empty:
                    self.error_message("CSV file is empty or formatted incorrectly.")
                else:
                    print("CSV file loaded successfully.")
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
        """
        Returns the list of measures from the loaded data.
        Assumes 'Measures' is a column in the DataFrame.
        """
        if self.data:
            sheet_data = self.data['Sheet1']
            if 'Measures' in sheet_data.columns:
                return sheet_data['Measures'].tolist()
            else:
                self.error_message("No 'Measures' column found in the data.")
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