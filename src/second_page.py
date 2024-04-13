'''NEED I SAY MORE??
TWEAAAAAAKS NEEDED
'''

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class SecondPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Sidebar setup
        self.sidebar = QWidget()  # Changed from self.sidebarLayout to self.sidebar
        self.sidebar.setStyleSheet("background-color: #555; color: white;")
        self.sidebar.setFixedWidth(150)
        sidebarLayout = QVBoxLayout(self.sidebar)  # Attach layout directly to the widget

        # Styling sidebar buttons
        sidebarButtonStyle = """
            QPushButton {
                font-family: 'Arians';
                color: white;
                font-size: 18px;
                text-align: left;
                padding: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #666;
            }
        """

        # Create buttons for the sidebar
        btnHome = QPushButton(self.recolor_icon("Icons/home.png", 'white'), " Home")
        btnNew = QPushButton(self.recolor_icon("Icons/new.png", 'white'), " New")
        btnOpen = QPushButton(self.recolor_icon("Icons/open.png", 'white')," Open")
        btnHelp = QPushButton(self.recolor_icon("Icons/help.png", 'white'), " Help")
        btnSave = QPushButton(" Save")
        btnSaveAs = QPushButton(" Save as")
        btnExport = QPushButton(" Export")
        btnClose = QPushButton(" Close")
        
        buttonList = [btnHome,btnNew,btnOpen, btnSave, 
                      btnSaveAs, btnExport, btnClose, btnHelp]
        
        for btn in buttonList:
            btn.setIconSize(QSize(25, 25))
            btn.setStyleSheet(sidebarButtonStyle)
            if sidebarLayout.addWidget(btn) == 'btnHelp':
                sidebarLayout.addStretch(1)
            else:
                sidebarLayout.addWidget(btn)  # Add buttons to the sidebar layout

        # Connect button signals to their respective slots
        btnSave.clicked.connect(self.save)
        btnSaveAs.clicked.connect(self.save_as)
        btnExport.clicked.connect(self.export)
        btnClose.clicked.connect(self.close)

        # Main content area setup
        mainContent = QLabel("Main content goes here")

        # Main layout setup
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.sidebar)
        mainLayout.addWidget(mainContent)
        
        # Set the layout for the widget
        self.setLayout(mainLayout)

    def save(self):
        # Logic to save the current document
        pass

    def save_as(self):
        # Logic for "Save as" action
        pass

    def export(self):
        # Logic for exporting the document
        pass

    def close(self):
        # Confirm close operation
        user_reply = QMessageBox.question(
            self, 'Exit Application', 'Are you sure you want to quit the application?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if user_reply == QMessageBox.StandardButton.Yes:
            QApplication.quit()
        else:
            pass  # Do nothing

    def recolor_icon(self, icon_path, color):
        pixmap = QPixmap(icon_path)
        mask = pixmap.createMaskFromColor(QColor('black'), Qt.MaskMode.MaskOutColor)
        colored_pixmap = QPixmap(pixmap.size())
        colored_pixmap.fill(QColor(color))
        colored_pixmap.setMask(mask)
        return QIcon(colored_pixmap)
