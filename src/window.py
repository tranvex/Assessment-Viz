from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QSpacerItem,
    QSizePolicy,
    QMenuBar,
    QMenu,
    QAction,
    QLabel,
    QFileDialog,
)
import os
from converter import xls_to_csv


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualization of Assessment Data")
        self.setGeometry(100, 100, 600, 400)

        # set window icon
        icon_path = os.path.join("assets", "logo.png")  # NOT WORKING
        self.setWindowIcon(QIcon(icon_path))  # NOT WORKING

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Add a vertical spacer
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Toggle button
        toggle_button = QPushButton("Toggle Night Mode", self)
        toggle_button.setFixedHeight(20)
        toggle_button.clicked.connect(self.toggle_night_mode)
        layout.addWidget(toggle_button)

        # Menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        # input file action
        input_action = QAction("Select File", self)
        input_action.triggered.connect(self.open_file_dialog)
        file_menu.addAction(input_action)

        self.night_mode = False
        self.update_style()

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "Excel Files (*.xls *.xlsx)",
            options=options,
        )
        if file_name:
            xls_to_csv(file_name)  # Call the function

    def toggle_night_mode(self):
        self.night_mode = not self.night_mode
        self.update_style()

    def update_style(self):
        if self.night_mode:
            # Apply night mode stylesheet
            self.setStyleSheet(
                """
                QMainWindow { background-color: #2c3e50; }
                QPushButton { background-color: #34495e; color: #ecf0f1; border-radius: 5px; }
                QMenuBar { background-color: #34495e; }  # Less dark color for the menu bar
                QMenuBar::item { color: #ecf0f1; }  # White color for the menu items
                """
            )
        else:
            # Apply day mode stylesheet
            self.setStyleSheet(
                """
                QMainWindow { background-color: #ecf0f1; }
                QPushButton { background-color: #bdc3c7; color: #2c3e50; border-radius: 5px;}
                QMenuBar { background-color: #c0c0c0; }  # Darker color for the menu bar
                QMenuBar::item { color: #2c3e50; }  # Dark color for the menu items
                """
            )
