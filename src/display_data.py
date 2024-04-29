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

    # def create_model_from_dataframe(self, data_frame):
    #     """
    #     Converts a DataFrame to QStandardItemModel to be used in a QTableView.
    #     Converts 'nan' values to blank strings.
    #     """
    #     model = QStandardItemModel()
    #     model.setHorizontalHeaderLabels(data_frame.columns.tolist())
    #     for index, row in data_frame.iterrows():
    #         items = []
    #         for cell in row:
    #             text = "" if isna(cell) else str(cell)
    #             item = QStandardItem(text)
    #             items.append(item)
    #         model.appendRow(items)
    #     return model
    def create_model_from_dataframe(self, data_frame):
        """
        Converts a DataFrame to QStandardItemModel to be used in a QTableView.
        Formats floating-point numbers to a fixed number of decimal places.
        Converts 'nan' values to blank strings.
        """
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(data_frame.columns.tolist())

        for index, row in data_frame.iterrows():
            items = []
            for cell in row:
                if pd.isna(cell):
                    text = ""
                elif isinstance(cell, float):
                    text = "{:.2f}".format(cell)
                else:
                    text = str(cell)
                item = QStandardItem(text)
                items.append(item)
            model.appendRow(items)
        return model
    
    def clear_data(self):
        """
        Clears all data displayed in the viewer.
        """
        self.tab_widget.clear()
