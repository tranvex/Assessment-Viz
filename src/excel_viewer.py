from PyQt6.QtWidgets import (
    QWidget,
    QTableWidget,
    QVBoxLayout,
    QTableWidgetItem,
    QComboBox,
)
import pandas as pd


# Define a class named Excel_Viewer which inherits from QWidget
class Excel_Viewer(QWidget):
    # Initialize the class
    def __init__(self, parent=None):
        # Call the parent class's __init__ method
        super().__init__(parent=parent)
        # Create a QVBoxLayout instance
        self.layout = QVBoxLayout(self)

        # Create a QComboBox instance for sheet selection
        self.sheet_selector = QComboBox()
        # Connect the currentIndexChanged signal to the on_sheet_selected method
        self.sheet_selector.currentIndexChanged.connect(self.on_sheet_selected)
        # Add the sheet_selector to the layout
        self.layout.addWidget(self.sheet_selector)

        # Create a QTableWidget instance for displaying data
        self.table = QTableWidget()
        # Add the table to the layout
        self.layout.addWidget(self.table)

        # Initialize the excel_loader attribute to None
        self.excel_loader = None

    # Define a method to load an Excel file
    def load_excel_file(self, excel_loader):
        # Store the ExcelLoader instance
        self.excel_loader = excel_loader
        # Clear the sheet_selector
        self.sheet_selector.clear()
        # Add the names of the sheets in the Excel file to the sheet_selector
        self.sheet_selector.addItems(excel_loader.get_sheet_names())

    # Define a method to handle sheet selection
    def on_sheet_selected(self, index):
        # Get the name of the selected sheet
        sheet_name = self.sheet_selector.itemText(index)
        # If an Excel file has been loaded
        if self.excel_loader:
            # Get the data from the selected sheet
            data_frame = self.excel_loader.get_sheet_data(sheet_name)
            # Display the data
            self.display_data(data_frame)

    # Define a method to display data in the table
    def display_data(self, data_frame):
        # Set the number of rows and columns in the table
        self.table.setRowCount(len(data_frame.index))
        self.table.setColumnCount(len(data_frame.columns))
        # Set the column headers
        self.table.setHorizontalHeaderLabels(data_frame.columns)

        # Iterate over the rows in the data frame
        for i, row in data_frame.iterrows():
            # Iterate over the values in the row
            for j, value in enumerate(row):
                # Format the value for display
                item = self.format_value_for_display(value)
                # Set the table item
                self.table.setItem(i, j, QTableWidgetItem(item))

        # Resize the columns to fit the contents
        self.table.resizeColumnsToContents()

    # Define a method to format a value for display
    def format_value_for_display(self, value):
        """Format the value for display purposes only, rounding percentages."""
        # If the value is null, return an empty string
        if pd.isnull(value):
            return ""
        # If the value is a float
        elif isinstance(value, float):
            # If the value is 1.0, return "100%"
            if value == 1.0:
                return "100%"
            # If the value is an integer, return the integer as a string
            elif value.is_integer():
                return str(int(value))
            else:
                # If the value is a percentage (between 0 and 1)
                if 0 < value < 1:
                    # Round the percentage to the nearest whole number and format as a percentage string
                    rounded_percentage = round(value * 100)
                    return f"{rounded_percentage}%"
                else:
                    # For non-percentage floats, display with a precision of 2 decimal places
                    return "{:.2f}".format(value)
        else:
            # If the value is not a float, return the value as a string
            return str(value)
