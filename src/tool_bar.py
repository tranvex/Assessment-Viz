from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__("Main Toolbar", parent)
        self.window = parent

        # Add 'File' section to take us back to the starter page
        self.add_file_section()
        
        self.add_graph_section()

    def add_file_section(self):
        # Add a 'File' action that takes the user back to the starter page
        file_action = QAction("File", self)
        file_action.triggered.connect(self.window.show_second_page)
        self.addAction(file_action)
        
    def add_graph_section(self):
        # Add a 'Graph' action to open the graph dialog or view
        graph_action = QAction("Graph", self)
        graph_action.triggered.connect(self.open_graph)
        self.addAction(graph_action)

    def open_graph(self):
        self.window.open_graph_dialog()

    def custom_sec(self):
        self.window.show_second_page()