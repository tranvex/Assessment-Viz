from PyQt5.QtWidgets import QMenuBar, QMenu, QAction


def create_menu(window):
    # Menu bar
    menu_bar = QMenuBar()  # Get the menu bar

    menu_bar.setStyleSheet("font-size: 14px;")
    
    file_menu = QMenu("File", menu_bar)  # Create a "File" menu
    menu_bar.addMenu(file_menu)  # Add the "File" menu to the menu bar

    # Input file action
    input_action = QAction("Select File", window)  # Create a QAction
    input_action.triggered.connect(
        window.open_file_dialog
    )  # Connect the action's triggered signal to the open_file_dialog slot
    file_menu.addAction(input_action)  # Add the action to the file menu

    return menu_bar
