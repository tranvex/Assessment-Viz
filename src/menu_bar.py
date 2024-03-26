from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction


# Define a class named Menu_Bar which inherits from QMenuBar
class Menu_Bar(QMenuBar):
    # Initialize the class
    def __init__(self, parent=None):
        # Call the parent class's __init__ method
        super().__init__(parent)
        # Set the window attribute to the parent
        self.window = parent
        # Set the style of the menu bar
        self.setStyleSheet("font-size: 14px;")
        # Call the init_ui method to initialize the user interface
        self.init_ui()
        # Call the menu_actions method to set up the actions for the menu
        self.menu_actions()

    # Define a method to initialize the user interface
    def init_ui(self):
        # Add a "File" menu to the menu bar
        self.file_menu = self.addMenu("File")

    # Define a method to set up the actions for the menu
    def menu_actions(self):
        # Create an "Open" action
        open_action = QAction("Open", self)
        # Connect the action's triggered signal to the window's open_file_dialog method
        open_action.triggered.connect(self.window.open_file_dialog)
        # Add the action to the "File" menu
        self.file_menu.addAction(open_action)

        # Create a "New" action
        new_action = QAction("New", self)
        # Connect the action's triggered signal to the window's new_file method
        new_action.triggered.connect(self.window.new_file)
        # Add the action to the "File" menu
        self.file_menu.addAction(new_action)

        # Create an "Exit" action
        exit_action = QAction("Exit", self)
        # Connect the action's triggered signal to the window's close_application method
        exit_action.triggered.connect(
            self.window.close_application
        )  # Assuming a custom close method
        # Add the action to the "File" menu
        self.file_menu.addAction(exit_action)
