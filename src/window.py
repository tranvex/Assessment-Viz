from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import os
from display_data import DataDisplay
from data_loader import DataLoader
from menu_bar import MenuBar
from graph_dialog import GraphDialog
from PyQt6.QtCore import *
from graph import Graph

class MainWindow(QMainWindow):
    dataLoaded = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wisdom Waves")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "assets", "WisdomWaves.svg")))
        self.graph = None
        self.initUI()
        self.initStatusBar()
        
    def initUI(self):
        self.setStyleSheet("QMainWindow { background-color: gray; }")
        
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Main content area including data display and file page view
        self.stacked_widget = QStackedWidget(self)
        self.data_display = DataDisplay(self) 
        self.data_display.setStyleSheet("background-color: white;")
        self.main_interface = QWidget()
        main_interface_layout = QVBoxLayout()
        main_interface_layout.addWidget(self.data_display, 1)
        self.main_interface.setLayout(main_interface_layout)

        self.file_page_view = QWidget()
        self.stacked_widget.addWidget(self.main_interface)
        self.stacked_widget.addWidget(self.file_page_view)
        self.setCentralWidget(self.stacked_widget)
        
        self.menu_bar.homeRequested.connect(self.go_to_home)
    
    
    def initStatusBar(self):
        # This method initializes the status bar
        self.statusBar().showMessage("Ready")
        
    def go_to_home(self):
        from start_page import StartPage
        # Method to switch back to the StartPage
        self.start_page = StartPage()
        self.start_page.show()
        self.close()
  
    def open_file_dialog(self):
        # File dialog to handle Excel and CSV files properly
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

    def close_application(self):
        reply = QMessageBox.question(self, 'Exit Confirmation', 
                                    "Are you sure you want to exit?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                    QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.close()

    def show_file_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_main_interface(self):
        self.stacked_widget.setCurrentIndex(0)

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        self.centralWidget().resize(self.size())
        self.centralWidget().update()

    def load_data(self, file_path):
        data_loader = DataLoader(file_path)
        data_loader.load_data()
        if data_loader.data:
            self.data_display.load_data(data_loader)
            self.graph = Graph(data_loader)  # Initialize Graph here after data is loaded
            self.dataLoaded.emit()
        else:
            QMessageBox.critical(self, "Error", "Failed to load data from the file. Please check the file and try again.")

    def open_graph_dialog(self):
        if self.graph and self.graph.data_frames:  # Assuming `data_frames` is the correct attribute
            try:
                graph_dialog = GraphDialog(self.graph, self)
                graph_dialog.exec()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to set up graph dialog: {e}")
        else:
            QMessageBox.critical(self, "Error", "No data loaded. Load data before graphing.")

    def show_sheet_data(self, sheet_name):
        sheet_data = self.data_loader.get_sheet_data(sheet_name)
        if sheet_data is not None:
            self.data_display.load_data(sheet_data)
        else:   
            QMessageBox.critical(self, "Error", "Failed to load data for the selected sheet.")