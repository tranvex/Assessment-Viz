from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import pandas as pd
from pandas import isna

class DataDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget, 1)
        self.setLayout(layout)
        
    def load_data(self, data_loader):
        """
        Loads and displays data from the DataLoader instance.
        Assumes that 'data_loader.data' contains a dictionary with sheet names as keys and DataFrames as values.
        """
        self.tab_widget.clear()  # Clear existing tabs if any
        if data_loader.data:
            for sheet_name, data_frame in data_loader.data.items():
                self.create_data_tab(sheet_name, data_frame)

    def create_data_tab(self, name, data_frame):
        """
        Creates a tab for a given DataFrame.
        """
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)
        table_view = QTableView(tab)
        model = self.create_model_from_dataframe(data_frame)
        table_view.setModel(model)

        # Set the horizontal header to stretch and fill the available space
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        tab_layout.addWidget(table_view)
        self.tab_widget.addTab(tab, name)

    def create_model_from_dataframe(self, data_frame):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(data_frame.columns.tolist())

        for index, row in data_frame.iterrows():
            items = []
            for col_index, cell in enumerate(row):
                item = QStandardItem()

                if pd.isna(cell):
                    item.setText('')
                elif isinstance(cell, float) and 0 <= cell <= 1:
                    # If the float value is between 0 and 1, format it as a percentage
                    percentage_value = cell * 100  # Convert to percentage
                    item.setText(f"{percentage_value:.0f}%")
                else:
                    item.setText(str(cell))

                # Align numeric data to the right and others to the left
                alignment = Qt.AlignmentFlag.AlignRight if isinstance(cell, (int, float)) else Qt.AlignmentFlag.AlignLeft
                item.setTextAlignment(alignment | Qt.AlignmentFlag.AlignVCenter)
                items.append(item)
            model.appendRow(items)

        return model

    def clear_data(self):
        """
        Clears all data displayed in the viewer.
        """
        self.tab_widget.clear()