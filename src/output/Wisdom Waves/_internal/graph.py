import pandas as pd
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QMessageBox

class Graph:
    def __init__(self, data_loader):
        self.loader = data_loader
        if self.loader.data:
            self.years = self.loader.get_sheet_names()
            self.data_frames = {year: self.loader.get_sheet_data(year) for year in self.years}
        else:
            print("Graph class was initialized without data.")

    def get_measures(self):
        measures = set()
        for df in self.data_frames.values():
            if df is not None and 'Measures' in df.columns:
                measures.update(df['Measures'].dropna().unique())
        return list(measures)
