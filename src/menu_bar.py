from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MenuBar(QMenuBar):
    homeRequested = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = parent

        # Ensure the parent window has a status bar
        if self.window:
            self.window.statusBar().showMessage("Ready")

        # Home menu
        self.add_home_menu()

        # File menu with open and exit actions
        self.add_file_menu()
        
        # Graph menu 
        self.add_graph_menu()
        
    def add_file_menu(self):
        file_menu = self.addMenu("File")
        
        # Add 'Open' action
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.window.open_file_dialog)
        open_action.setStatusTip("Open a new file..")  # Use status tip for information
        file_menu.addAction(open_action)
        
        # Add 'Exit' action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.window.close_application)
        exit_action.setStatusTip("Exit the application..")  # Use status tip for information
        file_menu.addAction(exit_action)
        
    def add_graph_menu(self):
        graph_menu = self.addMenu("Graph")

        graph_action = QAction("Show Graph", self)
        graph_action.triggered.connect(self.window.open_graph_dialog)
        graph_action.setStatusTip("Opens Graph GUI..")  # Use status tip
        graph_menu.addAction(graph_action)

    def add_home_menu(self):
        # Add 'Home' action
        home_action = QAction("Home",self)
        home_action.triggered.connect(self.homeRequested.emit)
        home_action.setStatusTip("Return to the home page..")  # Use status tip
        self.addAction(home_action)
