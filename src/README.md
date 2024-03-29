# How to Work on This Project

## Description

Brief explanation of how to work on this project utilizing a virtual environment.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

# optional VScode extension:
- Rainbow csv
- markdown all in one
- vscode pdf
- gitblame
- coderunner

## Setting Up Your Development Environment

You can use whatever text editor or IDE you prefer. However, remember to pull from the main branch before you start working on the project.

### Creating a Virtual Environment

1. Open your terminal (Command Prompt, PowerShell, or Bash).
2. Navigate to the project's root directory:
   ```bash
   cd path/to/your/project
   ```
3. Create a virtual environment named `venv` (or any other name you prefer):
   ```bash
   python -m venv venv
   ```
   This command creates a new directory `venv` in your project directory, containing the virtual environment.

### Activating the Virtual Environment

To activate the virtual environment, run the following command in your terminal:

Make sure you are in the root directory of the project before running the following commands.

- **C:path/to/Assessment-Viz**

- **On Windows:**
  ```bash
  venv/Scripts/activate
  ```
- **On macOS and Linux:**
  ```bash
  source venv/bin/activate
  ```
  After activation, your command line will indicate the active environment by prefixing its name to your command line prompt.

### Installing Dependencies

Install the project dependencies using the following command:

```bash
pip install -r requirements.txt
```

This command installs all the packages listed in the `requirements.txt` file.

## Running the Project

To run the project, execute:

```bash
python main.py
```

Replace `main.py` with the script you use to run your project.

## Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment by running:

```bash
deactivate
```

---
## Resources For Python:
- [pandas](https://pandas-xlsxwriter-charts.readthedocs.io/)
- [myplotlib](https://www.geeksforgeeks.org/plot-data-from-excel-file-in-matplotlib-python/)
- [csvPlot](https://www.youtube.com/watch?v=y43_o2OnI68)
- [matplotForum](https://www.w3schools.com/python/matplotlib_plotting.asp)
- [pandasForum](https://www.w3schools.com/python/pandas/default.asp)

---