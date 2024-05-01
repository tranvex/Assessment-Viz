# from data_loader import DataLoader
# import matplotlib.pyplot as plt
# from pandas import isna

# # Class for Graphing Data
# class Graph:
    
#     # Initialize with name of the Excel File
#     def __init__(self, file_name):
#         # Create instance of ExcelLoader with file name and load its data
#         self.loader = DataLoader(file_name)
#         self.loader.load_data()
        
#         # Declare lists to hold years(sheet names), dataframes, and measures
#         self.years = self.loader.get_sheet_names()
#         self.all_dfs = []
#         self.measures = []
        
#         # Call get_data method to store necessary data in lists
#         self.get_data()
        
#     # Define a method for retrieving dataframes and measures from ExcelLoader
#     def get_data(self):
#         for sheet_name in self.loader.data:
#             self.all_dfs.append(self.loader.get_sheet_data(sheet_name))
            
#         self.measures = list(self.all_dfs[0]['Measures'])
        
#     # Define a method for graphing data onto a scatter plot
#     def plot_data(self, start_year, end_year, msr):
#         try:
#             # Store indices for selected years and measure for later indexing
#             self.start_yr_index = self.years.index(start_year)
#             self.end_yr_index = self.years.index(end_year)
#             self.msr_index = self.measures.index(msr)
#             # Create a pyplot figure
#             plt.figure(figsize=(10,8))
#             # Declare a list to hold certain data that will be used for the y axis
#             y_axis = []
            
#             # Loop through selected dataframes
#             for dfs in self.all_dfs[self.start_yr_index:(self.end_yr_index + 1)]:
#                 # Check if value in '% students met target' is NaN
#                 if isna(dfs['% students met target'][self.msr_index]):
#                     # If so, check if value in '#students meeting target' is NaN
#                     if isna(dfs['#students meeting target'][self.msr_index]):
#                         # If both values are missing append 0 to y_axis[]
#                         y_axis.append(0)
#                     else:
#                         # Calculate % if '#students meeting target' is present and append value to y_axis
#                         y_axis.append(round(((dfs['#students meeting target'][self.msr_index]) / (dfs['# students'][self.msr_index])) * 100))
#                 else:
#                     # Append value to y_axis if no calculation is needed
#                     y_axis.append(round((dfs['% students met target'][self.msr_index]) * 100))
            
#             # Graph data into a scatter plot w/ horizontal line representing target %
#             plt.scatter(self.years[self.start_yr_index:(self.end_yr_index + 1)], y_axis)
#             plt.axhline(((self.all_dfs[0])['Target'][self.msr_index]) * 100, c='red')
            
#             # Title X and Y axes, the graph, and measure description
#             plt.xlabel("School Year")
#             plt.ylabel("% Students Met Target")
#             plt.suptitle(f"Graph for Measure {self.measures[self.msr_index]}")
#             plt.title(f"Measure Description: {(self.all_dfs[0])['Description'][self.msr_index]}")
            
#             # Get current axes, set labels for X ticks, set Y axis limit
#             ax = plt.gca()
#             ax.set_xticklabels(self.years[self.start_yr_index:(self.end_yr_index + 1)])
#             ax.set_ylim([0,105])
#             plt.ylim(bottom = 1)
            
#             # Rotate and align X tick labels and show horizontal grid
#             plt.xticks(rotation = 25, ha = 'center')
#             plt.grid(axis = 'y')
            
#             # Display graph
#             plt.show()
            
#         except Exception as e:
#             # Print error if problem occurred during graphing process
#             print(f"An error occurred while generating the graph: {e}")

# from data_loader import DataLoader
# import matplotlib.pyplot as plt
# from pandas import isna

# class Graph:
#     def __init__(self, file_name):
#         self.loader = DataLoader(file_name)
#         self.loader.load_data()

#         if self.loader.data:
#             self.years = self.loader.get_sheet_names()
#             self.all_dfs = []
#             self.measures = []
#             self.get_data()
#         else:
#             print("No data loaded. Please check the file path and format.")
#             self.years = []
#             self.all_dfs = []
#             self.measures = []

#     def get_data(self):
#         if self.loader.data:
#             for sheet_name in self.loader.data:
#                 df = self.loader.get_sheet_data(sheet_name)
#                 if df is not None:
#                     self.all_dfs.append(df)
            
#             if self.all_dfs:
#                 self.measures = list(self.all_dfs[0]['Measures'])

#     def plot_data(self, start_year, end_year, msr):
#         if not self.all_dfs or not self.measures:
#             print("No data or measures available to plot.")
#             return

#         try:
#             self.start_yr_index = self.years.index(start_year)
#             self.end_yr_index = self.years.index(end_year)
#             self.msr_index = self.measures.index(msr)
#             plt.figure(figsize=(10, 8))
#             y_axis = []

#             for dfs in self.all_dfs[self.start_yr_index:(self.end_yr_index + 1)]:
#                 value = 0
#                 if not isna(dfs['% students met target'][self.msr_index]):
#                     value = round((dfs['% students met target'][self.msr_index]) * 100)
#                 elif not isna(dfs['#students meeting target'][self.msr_index]):
#                     value = round(((dfs['#students meeting target'][self.msr_index]) / 
#                                    (dfs['# students'][self.msr_index])) * 100)
#                 y_axis.append(value)

#             plt.scatter(self.years[self.start_yr_index:(self.end_yr_index + 1)], y_axis)
#             plt.axhline(((self.all_dfs[0])['Target'][self.msr_index]) * 100, c='red')
#             plt.xlabel("School Year")
#             plt.ylabel("% Students Met Target")
#             plt.suptitle(f"Graph for Measure {self.measures[self.msr_index]}")
#             plt.title(f"Measure Description: {(self.all_dfs[0])['Description'][self.msr_index]}")
#             ax = plt.gca()
#             ax.set_xticklabels(self.years[self.start_yr_index:(self.end_yr_index + 1)], rotation=25, ha='center')
#             ax.set_ylim([0, 105])
#             plt.ylim(bottom=1)
#             plt.grid(axis='y')
#             plt.show()
#         except Exception as e:
#             print(f"An error occurred while generating the graph: {e}")

from data_loader import DataLoader
import matplotlib.pyplot as plt
from pandas import isna

class Graph:
    def __init__(self, file_name):
        self.loader = DataLoader(file_name)
        self.loader.load_data()

        if self.loader.data:
            self.years = self.loader.get_sheet_names()
            self.all_dfs = []
            self.measures = []
            self.get_data()
        else:
            print("No data loaded. Please check the file path and format.")
            self.years = []
            self.all_dfs = []
            self.measures = []

    def get_data(self):
        if self.loader.data:
            for sheet_name in self.loader.data:
                df = self.loader.get_sheet_data(sheet_name)
                if df is not None:
                    self.all_dfs.append(df)
            
            if self.all_dfs:
                self.measures = list(self.all_dfs[0]['Measures'])

    def plot_data(self, start_year, end_year, msr):
        if not self.all_dfs or not self.measures:
            print("No data or measures available to plot.")
            return

        try:
            self.start_yr_index = self.years.index(start_year)
            self.end_yr_index = self.years.index(end_year)
            self.msr_index = self.measures.index(msr)
            
            # Loop through each year in the selected range
            for year_idx in range(self.start_yr_index, self.end_yr_index + 1):
                year = self.years[year_idx]
                dfs = self.all_dfs[year_idx]
                value = None

                # Only plot if data exists
                if not isna(dfs['% students met target'][self.msr_index]):
                    value = round((dfs['% students met target'][self.msr_index]) * 100)
                elif not isna(dfs['#students meeting target'][self.msr_index]):
                    value = round(((dfs['#students meeting target'][self.msr_index]) / 
                                   (dfs['# students'][self.msr_index])) * 100)

                if value is not None:
                    plt.figure(figsize=(5, 4))
                    plt.scatter(year, value)
                    plt.axhline(((dfs)['Target'][self.msr_index]) * 100, c='red')
                    plt.xlabel("School Year")
                    plt.ylabel("% Students Met Target")
                    plt.title(f"{year} - Measure: {self.measures[self.msr_index]}")
                    plt.ylim(0, 105)
                    plt.grid(True)
                    plt.show()
        except Exception as e:
            print(f"An error occurred while generating the graph: {e}")
