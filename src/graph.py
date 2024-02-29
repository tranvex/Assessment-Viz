# import matplotlib.patches as patches
# graph.py
import pandas as pd
import matplotlib.pyplot as plt


def create_graph(sheet_name, csv_file):
    try:
        # Read the CSV file for the specified sheet
        data = pd.read_csv(csv_file)

        # Assuming the CSV file has columns "Category" and "Value"
        # You can customize this based on your actual data structure
        category_column = "Measures"
        value_column = "% students met target"

        # Plotting a bar graph
        plt.figure(figsize=(8, 6))
        plt.bar(data[category_column], data[value_column])
        plt.xlabel(category_column)
        plt.ylabel(value_column)
        plt.title(f"Graph for {sheet_name}")
        plt.xticks(rotation=45, ha="right")

        # Save the graph as PNG
        plt.savefig(f"{sheet_name}_graph.png", bbox_inches="tight")

        # Close the figure to free up resources
        plt.close()

        # Return the figure to be displayed
        return plt.gcf()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
