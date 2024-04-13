'''ALMOST NEEDED THE PRESIDENT FOR THIS ONE
MINOR CHANGES IN DISPLAYING DATA AND RESIZING TABLEE

#LENNY
'''


from PyQt6.QtWidgets import *
import pandas as pd

class Excel_Viewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        self.sheet_selector = QComboBox()
        self.sheet_selector.currentIndexChanged.connect(self.on_sheet_selected)
        self.layout.addWidget(self.sheet_selector)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)
        
        # ensures the table expands both horizontally and vertically
        self.table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.excel_loader = None

        self.setLayout(self.layout)

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

        # Initialize all cells with empty strings
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                self.table.setItem(i, j, QTableWidgetItem(""))

        # Populate the cells with actual data
        for i, row in data_frame.iterrows():
            for j, value in enumerate(row):
                item = self.format_value_for_display(value)
                self.table.setItem(i, j, QTableWidgetItem(item))

        # Adjust columns to fit the content
        header = self.table.horizontalHeader()
        for col in range(self.table.columnCount() - 1):  # -1 to skip the last column
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.ResizeToContents)

        # For the last column, let it take the remaining space without stretching too much
        header.setSectionResizeMode(self.table.columnCount() - 1, QHeaderView.ResizeMode.Stretch)

    def format_value_for_display(self, value):
        if pd.isnull(value):
            return ""
        elif isinstance(value, float):
            if value == 1.0:
                return "100%"
            elif value.is_integer():
                return str(int(value))
            elif 0 < value < 1:
                return f"{round(value * 100)}%"
            else:
                return f"{value:.2f}"
        else:
            return str(value)