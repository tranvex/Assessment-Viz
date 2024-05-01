from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = parent
        
        # File menu with open and exit actions
        self.add_file_menu()
        #Graph menu 
        self.add_graph_menu()

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
        # Add 'Graph' action
        graph_action = QAction("Graph", self)
        graph_action.triggered.connect(self.window.open_graph_dialog)
        self.addAction(graph_action)
