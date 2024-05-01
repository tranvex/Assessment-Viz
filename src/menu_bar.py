from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MenuBar(QMenuBar):
    homeRequested = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = parent
        
        # File menu with open and exit actions
        self.add_file_menu()
        #Graph menu 
        self.add_graph_menu()
        # Home menu
        self.add_home_menu()

    def add_file_menu(self):
        file_menu = self.addMenu("File")
        
        # Add 'Open' action
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.window.open_file_dialog)
        file_menu.addAction(open_action)
        
        # Add 'Exit' action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.window.close_application)
        file_menu.addAction(exit_action)
        
    def add_graph_menu(self):
        graph_menu = self.addMenu("Graph")
        graph_action = QAction("Show Graph", self)
        graph_action.triggered.connect(self.window.open_graph_dialog)
        graph_menu.addAction(graph_action)

    def add_home_menu(self):
        # Add 'Home' action
        home_action = QAction("Home",self)
        home_action.triggered.connect(self.homeRequested.emit)
        self.addAction(home_action)
