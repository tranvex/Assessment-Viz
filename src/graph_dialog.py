from PyQt6.QtWidgets import *

class GraphDialog(QDialog):
    def __init__(self, graph, parent=None):
        super().__init__(parent)
        self.graph = graph
        self.setWindowTitle('Graph Options')
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.year_combobox = QComboBox()
        self.year_combobox.addItems(self.graph.years)

        self.measure_combobox = QComboBox()
        self.measure_combobox.addItems(self.graph.measures)

        self.plot_button = QPushButton('Plot')
        self.plot_button.clicked.connect(self.on_plot)
        layout.addWidget(self.year_combobox)
        layout.addWidget(self.measure_combobox)
        layout.addWidget(self.plot_button)
        self.setLayout(layout)

    # def on_plot(self):
    #     selected_year = self.year_combobox.currentText()
    #     selected_measure = self.measure_combobox.currentText()
    #     try:
    #         # Call plot_data with the appropriate arguments
    #         self.graph.plot_data(selected_year, selected_measure)
    #     except Exception as e:
    #         QMessageBox.critical(self, 'Plotting Error', f"Failed to plot graph: {str(e)}")
    def on_plot(self):
        selected_year = self.year_combobox.currentText()
        selected_measure = self.measure_combobox.currentText()
        self.graph.plot_data(selected_year, selected_measure)



