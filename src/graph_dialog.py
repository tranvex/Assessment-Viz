from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

class GraphDialog(QDialog):
    def __init__(self, graph, parent=None):
        super().__init__(parent)
        self.graph = graph
        self.initUI()
        self.selected_sheets = []
        self.max_selected = 2  # Maximum number of checkboxes that can be selected

    def initUI(self):
        layout = QVBoxLayout(self)
        self.canvas = FigureCanvas(Figure(figsize=(12,15)))  # Ensure the figure is attached to the canvas

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
        
        export_button = QPushButton("Export Graph")
        export_button.clicked.connect(self.export_graph)
        
        layout.addWidget(self.canvas)
        layout.addWidget(scroll_area)
        layout.addWidget(export_button)
        self.setLayout(layout)
        
    def export_graph(self):
        options = QFileDialog.Option.DontUseNativeDialog
        file_filter = "PNG Files (*.png);;JPEG Files (*.jpg);;PDF Files (*.pdf)"
        fileName, selectedFilter = QFileDialog.getSaveFileName(self, "Save Graph", "", file_filter, options=options)

        if fileName:
            # Ensure the file name ends with the correct extension based on filter
            extension_map = {
                "JPEG Files (*.jpg)": '.jpg',
                "PNG Files (*.png)": '.png',
                "PDF Files (*.pdf)": '.pdf'
            }
            extension = extension_map.get(selectedFilter)
            if extension and not fileName.lower().endswith(extension):
                fileName += extension

            try:
                # Attempt to save the figure
                self.canvas.figure.savefig(fileName)
                QMessageBox.information(self, "Export Success", f"Graph successfully exported as {os.path.basename(fileName)}")
            except Exception as e:
                QMessageBox.critical(self, "Export Failed", f"Failed to save graph: {str(e)}")


    def update_plot(self):
        self.selected_sheets = [name for name, cb in self.checkboxes.items() if cb.isChecked()]

        self.canvas.figure.clf()  # Clear the entire figure to ensure no overlays
        if not self.selected_sheets:
            self.canvas.draw()  # Clear the graph if no sheets are selected
            QMessageBox.critical(self, "Error", "No sheets selected for graphing.")
            return

        if len(self.selected_sheets) > self.max_selected:
            QMessageBox.warning(self, "Warning", f"Please select only {self.max_selected} sheets.")
            # Uncheck the last checked checkbox to maintain the limit
            sender = self.sender()
            if sender:
                sender.setChecked(False)
            return
        
        ax = self.canvas.figure.add_subplot(111)  # Create a new subplot
        colors = plt.cm.get_cmap('viridis', len(self.selected_sheets) + 1)  # Ensure red is reserved

        for i, sheet_name in enumerate(self.selected_sheets):
            df = self.graph.data_frames.get(sheet_name)
            if df is not None and not df.empty and '# students' in df.columns and 'Measures' in df.columns:
                if '% students met target' in df.columns and 'Target' in df.columns:
                    # Check if both "% students met target" and "# students meeting target" are empty
                    if df['% students met target'].empty and df['# students meeting target'].empty:
                        QMessageBox.warning(self, "Warning", f"No data available for {sheet_name}.")
                        continue  # Skip plotting if both are empty
                    # Check if "% students met target" is empty
                    elif df['% students met target'].empty:
                        # Perform the division
                        df['% students met target'] = df['# students meeting target'] / df['# students'] * 100
                    
                    # Check if the target value is different from the previous sheet
                    if i > 0 and not np.array_equal(df['Target'], self.graph.data_frames[self.selected_sheets[i-1]]['Target']):
                        target_marker = 'x'  # Use 'x' symbol for target if it's different
                    else:
                        target_marker = '_'  # Use '_' symbol for target if it's the same
                    
                    ax.scatter(df['Measures'], df['% students met target'], label=f"{sheet_name} - Met", color=colors(i))
                    if 'Measures' in df.columns:  # Check if 'Measures' column exists
                        ax.scatter(df['Measures'], df['Target'], label=f"{sheet_name} - Target", color='red', marker=target_marker)
                    else:
                        QMessageBox.warning(self, "Warning", f"No 'Measures' column found for {sheet_name}.")
                else:
                    QMessageBox.warning(self, "Warning", f"No complete data available for {sheet_name}.")
            else:
                QMessageBox.warning(self, "Warning", f"No suitable data available for {sheet_name}.")

        if 'Measures' in df.columns:  # Check if 'Measures' column exists
            ax.set_xticks(range(len(df['Measures'])))  # Set x-ticks position
            ax.set_xticklabels(df['Measures'], rotation=45, ha='right')  # Set x-tick labels to show measures
            
        ax.legend()
        ax.set_title("Student Performance Overview")
        ax.set_xlabel('Measures')
        ax.set_ylabel('Percentage of Students Meeting Target / Target')
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y*100)}%')) # Format y-axis labels as percentages
        self.canvas.draw()