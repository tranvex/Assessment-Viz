from PyQt6.QtWidgets import *

class GraphDialog(QDialog):
    def __init__(self, graph, parent=None):
        super().__init__(parent)
        self.graph = graph  # Assuming graph is an instance of Graph which contains a DataLoader.
        self.setWindowTitle('Graph Options')
        self.initUI()
        self.adjustWindowSize()

    def initUI(self):
        layout = QVBoxLayout(self)
        
        # Create combo boxes for parameter selection
        self.year_combobox = QComboBox()
        years = self.graph.loader.get_years()  # Debugging: Check what is being returned
        print("Loaded years:", years)  # This should show the list of years in the console
        self.year_combobox.addItems(years)
        
        self.measure_combobox = QComboBox()
        measures = self.graph.loader.get_measures()  # Debugging: Check what is being returned
        print("Loaded measures:", measures)  # This should show the list of measures in the console
        self.measure_combobox.addItems(measures)

        # Create a plot button
        self.plot_button = QPushButton('Plot')
        self.plot_button.clicked.connect(self.on_plot)

        # Arrange widgets in the layout
        layout.addWidget(self.year_combobox)
        layout.addWidget(self.measure_combobox)
        layout.addWidget(self.plot_button)

        self.setLayout(layout)

    def adjustWindowSize(self):
        # Get the screen resolution of the user's primary monitor
        screen = QApplication.primaryScreen()
        size = screen.size()
        width = int(size.width() * 0.8)  # Convert to integer
        height = int(size.height() * 0.8)  # Convert to integer
        self.resize(width, height)  # Resize the window to these dimensions
            
    def on_plot(self):
        # Get the selected parameters from the combo boxes
        selected_year = self.year_combobox.currentText()
        selected_measure = self.measure_combobox.currentText()

        # Assuming Graph class has a method called plot_data which takes these parameters
        try:
            self.graph.plot_data(selected_year, selected_year, selected_measure)  # Call plot for the selected year and measure.
        except Exception as e:
            QMessageBox.critical(self, 'Error', f"Failed to plot graph: {e}")

