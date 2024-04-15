from excel_loader import ExcelLoader
import matplotlib.pyplot as plt

# Class for Graphing Data
class Graph:
    
    # Initialize with name of the Excel File
    def __init__(self, file_name):
        # Create instance of ExcelLoader with file name and load its data
        self.loader = ExcelLoader(file_name)
        self.loader.load_excel()
        # Declare lists to hold years(sheet names), dataframes, and measures
        self.years = self.loader.get_sheet_names()
        self.all_dfs = []
        self.measures = []
        # Call get_data method to store necessary data in lists
        self.get_data()
        
    # Define a method for retrieving dataframes and measures from ExcelLoader
    def get_data(self):
        for sheet_name in self.loader.all_sheets:
            self.all_dfs.append(self.loader.get_sheet_data(sheet_name))
            
        self.measures = self.all_dfs[0]['Measures']
        
    # Define a method for graphing data onto a scatter plot
    def plot_data(self):
        try:
            # Create a pyplot figure
            plt.figure(figsize=(8,6))
            # Declare a list to hold certain data that will be used for the y axis
            y_axis = []
            
            # Loop through selected dataframes
            for dfs in self.all_dfs[0:3]:
                # Append selected value from "% students met target" column to y_axis[]
                y_axis.append(round((dfs['% students met target'][6]) * 100))
                # Plot a horizontal line representing the "Target" value
                plt.axhline(((dfs['Target'][6]) * 100))
            
            # Graph data into a scatter plot
            plt.scatter(self.years[0:3], y_axis)
            
            # Title X and Y axes as well as the graph
            plt.xlabel("School Year")
            plt.ylabel("% Students Met Target")
            plt.title(f"Graph for Measure {self.measures[6]}")
            # Get current axes, set labels for X ticks, set Y axis limit
            ax = plt.gca()
            ax.set_xticklabels(self.years[0:3])
            ax.set_ylim([0,100])
            # Rotate and align X tick labels and show horizontal grid
            plt.xticks(rotation = 30, ha = 'center')
            plt.grid(axis = 'y')
            # Display graph
            plt.show()
            
        except Exception as e:
            # Print error if problem occurred during graphing process
            print(f"An error occurred while generating the graph: {e}")