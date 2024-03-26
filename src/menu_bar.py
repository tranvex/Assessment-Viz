# menu_bar.py
from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction

class Menu_Bar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = parent
        self.setStyleSheet("font-size: 14px;")
        self.init_ui()
        self.menu_actions()

    def init_ui(self):
        self.file_menu = self.addMenu("File")
        
    def menu_actions(self):
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.window.open_file_dialog)
        self.file_menu.addAction(open_action)

        new_action = QAction("New", self)
        new_action.triggered.connect(self.window.new_file)
        self.file_menu.addAction(new_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.window.close_application)  # Assuming a custom close method
        self.file_menu.addAction(exit_action)
