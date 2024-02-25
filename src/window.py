from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QSpacerItem,
    QSizePolicy,
    QFileDialog,
)
import os
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from converter import (
    xls_to_csv,
)  # Importing the xls_to_csv function from converter module
from menu_bar import (
    create_menu,
)  # Importing the create_menu function from menu_bar module
from graph import create_graph  # Importing the create_graph function from graph module
from styling import set_custom_palette, set_stylesheet  # Importing the set_custom_palette and set_stylesheet functions from styling module


# MainWindow class inherits from QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Assessment Data Visualization")  # Set the window title
        
        set_custom_palette(self)  # Set the custom palette
        set_stylesheet(self)  # Set the stylesheet

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
        
        #set window color
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(211, 211, 211))
        self.setPalette(palette)

        # Set window icon
        script_dir = os.path.dirname(
            os.path.abspath(__file__)
        )  # Get the directory of the current script
        icon_path = os.path.join(
            script_dir, "assets", "s_logo.ico"
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
        toggle_button = QPushButton("Graph", self)  # Create a QPushButton
        toggle_button.setFixedHeight(20)  # Set the height of the button
        toggle_button.clicked.connect(
            self.show_graph
        )  # Connect the button's clicked signal to the toggle_night_mode slot
        layout.addWidget(toggle_button)  # Add the button to the layout

        menu_bar = create_menu(self)  # Create the menu bar
        self.setMenuBar(menu_bar)  # Set the menu bar

    def show_graph(self):
        # Create the graph
        figure = create_graph()

        # Create a canvas to display the graph
        canvas = FigureCanvas(figure)

        # Create a layout and add the canvas to it
        layout = QVBoxLayout()
        layout.addWidget(canvas)

        # Create a widget, set its layout to the layout containing the canvas, and set it as the central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

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
