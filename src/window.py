from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import os
from display_data import DataDisplay
from data_loader import DataLoader
from tool_bar import ToolBar
from second_page import SecondPage
from graph import Graph

class MainWindow(QMainWindow):
    def __init__(self, file_name=None):
        super().__init__()
        self.setWindowTitle("Wisdom Waves")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "assets", "s_logo.ico")))
        self.initUI()
        self.graph = Graph(file_name)

    def initUI(self):
        self.setStyleSheet("QMainWindow { background-color: #FFF8DC; }")

        self.tool_bar = ToolBar(self)
        self.addToolBar(self.tool_bar)

        self.stacked_widget = QStackedWidget(self)
        self.data_display = DataDisplay(self) 
        self.data_display.setStyleSheet("background-color: white;")

        self.main_interface = QWidget()
        main_interface_layout = QVBoxLayout(self.main_interface)
        main_interface_layout.addWidget(self.data_display, 1)

        self.file_page_view = QWidget()
        self.stacked_widget.addWidget(self.main_interface)
        self.stacked_widget.addWidget(self.file_page_view)
        self.setCentralWidget(self.stacked_widget)

  
    def open_file_dialog(self):
        # Updated the file dialog to include both Excel and CSV file formats
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xls *.xlsx);;CSV Files (*.csv)")
        if file_name:
            self.load_data(file_name)

    def new_file(self):
        response = QMessageBox.question(self, "New File",
                                        "Are you sure you want to open a new file and clear existing data?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if response == QMessageBox.StandardButton.Yes:
            self.data_display.clear_data()
            self.open_file_dialog()

    def load_data(self, file_path):
        data_loader = DataLoader(file_path)
        data_loader.load_data()
        self.data_display.load_data(data_loader)

    def close_application(self):
        self.close()

    def show_file_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_main_interface(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_second_page(self):
        if not hasattr(self, 'customSecpage'):
            self.customSecpage = SecondPage(self)
            self.stacked_widget.addWidget(self.customSecpage)
        index = self.stacked_widget.indexOf(self.customSecpage)
        self.stacked_widget.setCurrentIndex(index)

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        self.centralWidget().resize(self.size())
        self.centralWidget().update()
    
    
    def createCustomTitleBar(self):
        self.titleBar = QWidget()
        self.titleBarLayout = QHBoxLayout()
        self.titleBar.setStyleSheet("background-color: #333; color: white;")
        self.titleBar.setFixedHeight(40)

        self.lblTitle = QLabel("Wisdom Waves")

        self.titleBarLayout.addWidget(self.lblTitle)

        self.titleBar.setLayout(self.titleBarLayout)
        
        # Add custom title bar to main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.titleBar)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)
        
    def open_graph_dialog(self):
        if self.graph.setup_graph_dialog():
            self.graph.dialog.exec()
        else:
            QMessageBox.critical(self, "Error", "Failed to set up graph dialog.")