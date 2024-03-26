from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon
import os
from menu_bar import Menu_Bar
from excel_viewer import Excel_Viewer
from excel_loader import ExcelLoader


# Define a class named MainWindow which inherits from QMainWindow
class MainWindow(QMainWindow):
    # Initialize the class
    def __init__(self):
        # Call the parent class's __init__ method
        super().__init__()
        # Set the window title
        self.setWindowTitle("WisdomWaves")
        # Set the window geometry: x, y, width, height
        self.setGeometry(100, 100, 800, 600)
        # Set the window icon, the path is relative to this file's location
        self.setWindowIcon(
            QIcon(os.path.join(os.path.dirname(__file__), "assets", "s_logo.ico"))
        )
        # Call the initUI method to initialize the user interface
        self.initUI()

    # Define a method to initialize the user interface
    def initUI(self):
        # Set the menu bar of the window to a new instance of Menu_Bar
        self.setMenuBar(Menu_Bar(self))
        # Create an Excel_Viewer instance
        self.excel_viewer = Excel_Viewer(self)
        # Set the central widget of the window to the Excel_Viewer instance
        self.setCentralWidget(self.excel_viewer)

    # Define a method to open a file dialog for selecting Excel files
    def open_file_dialog(self):
        # Open a file dialog and get the selected file name
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Excel File", "", "Excel Files (*.xls *.xlsx)"
        )
        # If a file was selected, load it
        if file_name:
            self.load_excel_file(file_name)

    # Define a method to create a new file
    def new_file(self):
        # Ask the user for confirmation before creating a new file
        response = QMessageBox.question(
            self,
            "New File",
            "Are you sure you want to open a new file and clear existing data?",
        )
        # If the user confirmed, clear the existing data and open the file dialog
        if response == QMessageBox.StandardButton.Yes:
            self.excel_viewer.clear_data()
            self.open_file_dialog()

    # Define a method to load an Excel file
    def load_excel_file(self, file_path):
        # Create an ExcelLoader instance with the selected file path
        excel_loader = ExcelLoader(file_path)
        # Load the Excel file
        excel_loader.load_excel()
        # Load the Excel file into the Excel_Viewer
        self.excel_viewer.load_excel_file(excel_loader)

    # Define a method to close the application
    def close_application(self):
        # Close the window
        self.close()
