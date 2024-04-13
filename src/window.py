'''MIGHT DELETE LATER?????

SICKO MODE PT 2 AS IN I REMOVED REDUNDANT CODE 
PROBABLY ADDED BY ME.... ANYWAYS THIS NEEDS SOME TWEAKING TOO

#SAYNOTODRUGS

'''

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import os
from excel_viewer import Excel_Viewer
from excel_loader import ExcelLoader
from tool_bar import ToolBar
from second_page import SecondPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wisdom Waves")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "assets", "s_logo.ico")))
        self.initUI()

    def initUI(self):
        self.setStyleSheet("QMainWindow { background-color: #FFF8DC; }")
        self.tool_bar = ToolBar(self)
        self.addToolBar(self.tool_bar)

        self.stacked_widget = QStackedWidget(self)
        self.excel_viewer = Excel_Viewer(self)
        self.excel_viewer.setStyleSheet("background-color: white;")

        self.main_interface = QWidget()
        main_interface_layout = QVBoxLayout(self.main_interface)
        main_interface_layout.addWidget(self.excel_viewer)

        self.file_page_view = QWidget()
        self.stacked_widget.addWidget(self.main_interface)
        self.stacked_widget.addWidget(self.file_page_view)
        self.setCentralWidget(self.stacked_widget)

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xls *.xlsx)")
        if file_name:
            self.load_excel_file(file_name)

    def new_file(self):
        response = QMessageBox.question(self, "New File",
                                        "Are you sure you want to open a new file and clear existing data?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if response == QMessageBox.StandardButton.Yes:
            self.excel_viewer.clear_data()
            self.open_file_dialog()

    def load_excel_file(self, file_path):
        excel_loader = ExcelLoader(file_path)
        excel_loader.load_excel()
        self.excel_viewer.load_excel_file(excel_loader)

    def close_application(self):
        self.close()

    def show_file_page(self):
        # Switch to the 'File' page view
        self.stacked_widget.setCurrentIndex(1)

    def show_main_interface(self):
        # Switch back to the main interface
        self.stacked_widget.setCurrentIndex(0)
        
    def show_second_page(self):
        # Create the second page if it doesn't exist yet
        if not hasattr(self, 'customSecpage'):
            self.customSecpage = SecondPage(self)
            self.stacked_widget.addWidget(self.customSecpage)
        
        # Find the index of the second page and switch to it
        index = self.stacked_widget.indexOf(self.customSecpage)
        self.stacked_widget.setCurrentIndex(index)
        
    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        self.centralWidget().resize(self.size())
        self.centralWidget().update()
