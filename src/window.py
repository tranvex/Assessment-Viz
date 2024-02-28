# window.py
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
import pandas as pd
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from converter import xls_to_csv
from menu_bar import create_menu
from graph import create_graph
from styling import set_custom_palette, set_stylesheet

# MainWindow class inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Declare file_name and output_directory as class attributes
        self.file_name = None
        self.output_directory = None

        self.setWindowTitle("Assessment Data Visualization")  # Set the window title

        set_custom_palette(self)  # Set the custom palette
        set_stylesheet(self)  # Set the stylesheet

        self.layout = QVBoxLayout()

        # Button to exit the graph
        exit_button = QPushButton("Exit Graph", self)
        exit_button.setFixedHeight(20)
        exit_button.clicked.connect(self.exit_graph)
        self.layout.addWidget(exit_button)

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

        # Set window color
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(211, 211, 211))
        self.setPalette(palette)

        # Set window icon
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "assets", "s_logo.ico")
        self.setWindowIcon(QIcon(icon_path))

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Add a vertical spacer
        spacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )
        layout.addItem(spacer)

        # Toggle button
        toggle_button = QPushButton("Graph", self)
        toggle_button.setFixedHeight(20)
        toggle_button.clicked.connect(self.show_graph)
        layout.addWidget(toggle_button)

        menu_bar = create_menu(self)
        self.setMenuBar(menu_bar)

    def show_graph(self):
        if self.file_name and self.output_directory:
            try:
                all_sheets = pd.read_excel(self.file_name, sheet_name=None)
            except Exception as e:
                print(f"An error occurred while reading sheets: {e}")
                return

            # Create a new layout
            layout = QVBoxLayout()

            # Create a button for each sheet dynamically
            for sheet_name in all_sheets.keys():
                sheet_button = QPushButton(f"Graph for {sheet_name}", self)
                sheet_button.setFixedHeight(20)
                sheet_button.clicked.connect(
                    lambda checked, sheet=sheet_name: self.display_graph(sheet)
                )
                layout.addWidget(sheet_button)

            # Reset the central widget and set the new layout
            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            # Reset the window title
            self.setWindowTitle("Assessment Data Visualization")

    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def display_graph(self, sheet_name):
        # Create the graph for the specified sheet
        figure = create_graph(
            sheet_name,
            os.path.join(
                self.output_directory,
                f'{os.path.splitext(os.path.basename(self.file_name))[0]}_{sheet_name}.csv',
            ),
        )

        # Display the graph for the specified sheet
        self.display_graph_canvas(figure, sheet_name)

    def display_graph_canvas(self, figure, sheet_name):
        # Create a canvas to display the graph
        canvas = FigureCanvas(figure)

        # Create a layout and add the canvas to it
        layout = QVBoxLayout()
        layout.addWidget(canvas)

        # Create a widget, set its layout to the layout containing the canvas, and set it as the central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setWindowTitle(f"Graph for {sheet_name}")

    def exit_graph(self):
        # Clear the layout before going back to the main window
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        # Create the "Graph" button to go back to the main window
        toggle_button = QPushButton("Graph", self)
        toggle_button.setFixedHeight(20)
        toggle_button.clicked.connect(self.show_graph)
        self.layout.addWidget(toggle_button)

        # Reset the central widget to clear the previous graph
        self.setCentralWidget(None)
        self.setWindowTitle("Assessment Data Visualization")


    def open_file_dialog(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            file_name, _ = QFileDialog.getOpenFileName(
                self,
                'Select Excel File',
                '',
                'Excel Files (*.xls *.xlsx)',
                options=options,
            )
            # Specify file output directory
            project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            output_directory = project_directory

            # Print selected file name for debug
            print(f'Selected file: {file_name}')

            if file_name:
                xls_to_csv(file_name, output_directory)
                self.file_name = file_name
                self.output_directory = output_directory

            self.show_graph()
        except Exception as e:
            print(f'An error occurred: {e}')
