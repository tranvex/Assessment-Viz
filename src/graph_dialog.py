from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import matplotlib.pyplot as plt
import pandas as pd

class GraphDialog(QDialog):
    def __init__(self, graph, parent=None):
        super().__init__(parent)
        self.graph = graph
        self.initUI()
        self.selected_sheets = []

    def initUI(self):
        layout = QVBoxLayout(self)
        self.canvas = FigureCanvas(Figure(figsize=(10, 8)))
        
        scroll_area = QScrollArea(self)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        
        self.checkboxes = {}
        for sheet_name in self.graph.years:
            cb = QCheckBox(sheet_name)
            cb.stateChanged.connect(self.update_plot)
            scroll_layout.addWidget(cb)
            self.checkboxes[sheet_name] = cb
        
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        
        layout.addWidget(self.canvas)
        layout.addWidget(scroll_area)
        self.setLayout(layout)
        
    def update_plot(self):
        self.selected_sheets = [name for name, cb in self.checkboxes.items() if cb.isChecked()]

        self.canvas.figure.clf()  # Clear the entire figure to ensure no overlays
        if not self.selected_sheets:
            self.canvas.draw()  # Clear the graph if no sheets are selected
            QMessageBox.critical(self, "Error", "No sheets selected for graphing.")
            return

        ax = self.canvas.figure.add_subplot(111)  # Create a new subplot
        colors = plt.cm.get_cmap('viridis', len(self.selected_sheets) + 1)  # Ensure red is reserved

        for i, sheet_name in enumerate(self.selected_sheets):
            df = self.graph.data_frames.get(sheet_name)
            if df is not None and '# students' in df.columns and 'Measures' in df.columns:
                if '% students met target' in df.columns and 'Target' in df.columns:
                    ax.scatter(df['Measures'], df['% students met target'], label=f"{sheet_name} - Met", color=colors(i))
                    ax.scatter(df['Measures'], df['Target'], label=f"{sheet_name} - Target", color='red', marker='_')  # Red color for Target
                else:
                    QMessageBox.warning(self, "Warning", f"No complete data available for {sheet_name}.")
            else:
                QMessageBox.warning(self, "Warning", f"No suitable data available for {sheet_name}.")

        ax.set_xticks(range(len(df['Measures'])))  # Set x-ticks position
        ax.set_xticklabels(df['Measures'], rotation=45, ha='right')  # Set x-tick labels to show measures
        ax.legend()
        ax.set_title("Student Performance Overview")
        ax.set_xlabel('Measures')
        ax.set_ylabel('Percentage of Students Meeting Target / Target')
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y*100)}%'))  # Format y-axis labels as percentages
        self.canvas.draw()