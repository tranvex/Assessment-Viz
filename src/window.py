from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon
import os
from menu_bar import Menu_Bar
from excel_viewer import Excel_Viewer
from excel_loader import ExcelLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Application")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "assets", "s_logo.ico")))
        self.initUI()

    def initUI(self):
        self.setMenuBar(Menu_Bar(self))
        self.excel_viewer = Excel_Viewer(self)
        self.setCentralWidget(self.excel_viewer)

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xls *.xlsx)")
        if file_name:
            self.load_excel_file(file_name)

    def new_file(self):
        response = QMessageBox.question(self, "New File", "Are you sure you want to open a new file and clear existing data?")
        if response == QMessageBox.StandardButton.Yes:
            self.excel_viewer.clear_data()
            self.open_file_dialog()

    def load_excel_file(self, file_path):
        excel_loader = ExcelLoader(file_path)
        excel_loader.load_excel()
        self.excel_viewer.load_excel_file(excel_loader)

    def close_application(self):
        self.close()