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
    QDesktopWidget,
)
import os
from converter import (
    xls_to_csv,
)  # Importing the xls_to_csv function from converter module


# MainWindow class inherits from QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Get screen size
        primary_screen = QApplication.screens()[0]
        screen_resolution = primary_screen.geometry()
        screen_width, screen_height = (
            screen_resolution.width(),
            screen_resolution.height(),
        )

        # Set window size to 80% of the screen size
        self.setGeometry(0, 0, int(screen_width * 0.6), int(screen_height * 0.6))

        # Center the window on the screen
        self.move(
            (screen_width - self.width()) // 2, (screen_height - self.height()) // 2
        )

        # Set window icon
        script_dir = os.path.dirname(
            os.path.abspath(__file__)
        )  # Get the directory of the current script
        icon_path = os.path.join(
            script_dir, "assets", "s_logo.png"
        )  # Get the path to the icon
        self.setWindowIcon(QIcon(icon_path))  # Set the window icon

        # Central widget and layout
        central_widget = QWidget()  # Create a QWidget
        self.setCentralWidget(central_widget)  # Set the central widget
        layout = QVBoxLayout()  # Create a QVBoxLayout
        central_widget.setLayout(layout)  # Set the layout of the central widget

        # Add a vertical spacer
        spacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )  # Create a QSpacerItem
        layout.addItem(spacer)  # Add the spacer to the layout

        # Toggle button
        toggle_button = QPushButton("Toggle Night Mode", self)  # Create a QPushButton
        toggle_button.setFixedHeight(20)  # Set the height of the button
        toggle_button.clicked.connect(
            self.toggle_night_mode
        )  # Connect the button's clicked signal to the toggle_night_mode slot
        layout.addWidget(toggle_button)  # Add the button to the layout

        # Menu bar
        menu_bar = self.menuBar()  # Get the menu bar
        file_menu = menu_bar.addMenu("File")  # Add a "File" menu to the menu bar

        # Input file action
        input_action = QAction("Select File", self)  # Create a QAction
        input_action.triggered.connect(
            self.open_file_dialog
        )  # Connect the action's triggered signal to the open_file_dialog slot
        file_menu.addAction(input_action)  # Add the action to the file menu

        self.night_mode = False  # Initialize night_mode to False
        self.update_style()  # Call the update_style method

    # Method to open a file dialog
    def open_file_dialog(self):
        options = QFileDialog.Options()  # Create a QFileDialog.Options object
        options |= QFileDialog.ReadOnly  # Set the options to read only
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "Excel Files (*.xls *.xlsx)",
            options=options,
        )  # Open a file dialog
        if file_name:  # If a file was selected
            xls_to_csv(file_name)  # Call the xls_to_csv function with the selected file

    # Method to toggle night mode
    def toggle_night_mode(self):
        self.night_mode = not self.night_mode  # Toggle the value of night_mode
        self.update_style()  # Call the update_style method

    # Method to update the style
    def update_style(self):
        if self.night_mode:  # If night_mode is True
            # Apply night mode stylesheet
            self.setStyleSheet(
                """
                QMainWindow { background-color: #2c3e50; }
                QPushButton { background-color: #34495e; color: #ecf0f1; border-radius: 5px; }
                QMenuBar { background-color: #34495e; }  # Less dark color for the menu bar
                QMenuBar::item { color: #ecf0f1; }  # White color for the menu items
                """
            )
        else:  # If night_mode is False
            # Apply day mode stylesheet
            self.setStyleSheet(
                """
                QMainWindow { background-color: #ecf0f1; }
                QPushButton { background-color: #bdc3c7; color: #2c3e50; border-radius: 5px;}
                QMenuBar { background-color: #c0c0c0; }  # Darker color for the menu bar
                QMenuBar::item { color: #2c3e50; }  # Dark color for the menu items
                """
            )
