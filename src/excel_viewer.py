# excel_viewer.py
from PyQt6.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem, QComboBox
import pandas as pd

class Excel_Viewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QVBoxLayout(self)

        self.sheet_selector = QComboBox()
        self.sheet_selector.currentIndexChanged.connect(self.on_sheet_selected)
        self.layout.addWidget(self.sheet_selector)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.excel_loader = None

    def load_excel_file(self, excel_loader):
        self.excel_loader = excel_loader
        self.sheet_selector.clear()
        self.sheet_selector.addItems(excel_loader.get_sheet_names())

    def on_sheet_selected(self, index):
        sheet_name = self.sheet_selector.itemText(index)
        if self.excel_loader:
            data_frame = self.excel_loader.get_sheet_data(sheet_name)
            self.display_data(data_frame)

    def display_data(self, data_frame):
        self.table.setRowCount(len(data_frame.index))
        self.table.setColumnCount(len(data_frame.columns))
        self.table.setHorizontalHeaderLabels(data_frame.columns)

        for i, row in data_frame.iterrows():
            for j, value in enumerate(row):
                item = self.format_value_for_display(value)
                self.table.setItem(i, j, QTableWidgetItem(item))

        self.table.resizeColumnsToContents()

    def format_value_for_display(self, value):
        """Format the value for display purposes only, rounding percentages."""
        if pd.isnull(value):
            return ""
        elif isinstance(value, float):
            if value == 1.0:
                return "100%"
            elif value.is_integer():
                return str(int(value))
            else:
                # Check if the value represents a percentage (between 0 and 1)
                if 0 < value < 1:
                    # Round the percentage to the nearest whole number and format as a percentage string
                    rounded_percentage = round(value * 100)
                    return f"{rounded_percentage}%"
                else:
                    # For non-percentage floats, display with a precision of 2 decimal places
                    return "{:.2f}".format(value)
        else:
            return str(value)