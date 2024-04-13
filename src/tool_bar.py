from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__("Main Toolbar", parent)
        self.window = parent

        # Add 'File' section to take us back to the starter page
        self.add_file_section()

        # Add 'Home' section with actions for manipulating or editing the Excel data
        # self.add_home_section()

    def add_file_section(self):
        # Add a 'File' action that takes the user back to the starter page
        file_action = QAction("File", self)
        file_action.triggered.connect(self.window.show_second_page)
        self.addAction(file_action)

    # def add_home_section(self):
    #     # Add actions for the 'Home' section
    #     home_action = QAction("Home", self)
    #     home_action.triggered.connect(self.window.show_starter_page)
    #     self.addAction(home_action)
    #     self.addSeparator()

    def custom_sec(self):
        self.window.show_second_page()
        
'''IGNORE THE COMMENTED STUFF I WAS TESTING BUT NEEDED "IMPLEMENTATION"
OF THE ADD HOME SECTION ANYWAYS THIS IS HIGHLY UNFINISHED BUT WILL HAVE MORE SOON!!!!
'''