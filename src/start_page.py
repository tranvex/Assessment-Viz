from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import json
import os
from window import MainWindow  # Ensure this correctly points to your MainWindow module

class StartPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wisdom Waves")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.oldPos = self.pos()
        self.initUI()

    def initUI(self):               
        # Custom title bar setup
        self.titleBar = QWidget()
        self.titleBarLayout = QHBoxLayout()
        self.titleBar.setStyleSheet("background-color: #333;")
        self.titleBar.setFixedHeight(40)
        self.titleBar.setLayout(self.titleBarLayout)
        
        # Window title label setup
        self.windowTitleLabel = QLabel("Wisdom Waves")
        self.windowTitleLabel.setStyleSheet("color: white; font-size: 16px; font-weight: bold; padding-left: 5px")
        self.windowTitleLabel.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Custom buttons for window controls
        self.minimizeButton = QPushButton(QIcon(self.recolor_icon("Icons/min.png", "white")), "")
        self.maximizeButton = QPushButton(QIcon(self.recolor_icon("Icons/max.png", "white")), "")
        self.closeButton = QPushButton(QIcon(self.recolor_icon("Icons/close.png", "white")), "")
        
        # Styling for the custom buttons
        buttonStyle = """
            QPushButton {
                border: none;
                background-color: #333;
                padding-top: 5px;
            }
            QPushButton:hover {
                background-color: #444;
            }
        """

        self.minimizeButton.setStyleSheet(buttonStyle)
        self.maximizeButton.setStyleSheet(buttonStyle)
        self.closeButton.setStyleSheet(buttonStyle)

        self.minimizeButton.setIconSize(QSize(16, 16))
        self.maximizeButton.setIconSize(QSize(16, 16))
        self.closeButton.setIconSize(QSize(16, 16))

        self.minimizeButton.setFixedSize(40, 40)
        self.maximizeButton.setFixedSize(40, 40)
        self.closeButton.setFixedSize(40, 40)
        
        self.minimizeButton.clicked.connect(self.showMinimized)
        self.maximizeButton.clicked.connect(self.toggleMaximize)
        self.closeButton.clicked.connect(self.close)
        
        # Title bar layout setup
        self.titleBarLayout.addWidget(self.windowTitleLabel)
        self.titleBarLayout.addStretch(1)
        self.titleBarLayout.addWidget(self.minimizeButton)
        self.titleBarLayout.addWidget(self.maximizeButton)
        self.titleBarLayout.addWidget(self.closeButton)
        self.titleBarLayout.setContentsMargins(0, 0, 0, 0)
        
        # Sidebar setup
        self.sidebar = QWidget()
        self.sidebar.setStyleSheet("background-color: #555; color: white;")
        self.sidebar.setFixedWidth(150)
        sidebarLayout = QVBoxLayout(self.sidebar)
        sidebarLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        sidebarLayout.setContentsMargins(10, 10, 10, 10)
        sidebarLayout.setSpacing(10)
        
        # Sidebar buttons with icons
        btnHome = QPushButton(self.recolor_icon("Icons/home.png", 'white'), " Home")
        btnOpen = QPushButton(self.recolor_icon("Icons/open.png", 'white')," Open")
        btnHelp = QPushButton(self.recolor_icon("Icons/help.png", 'white'), " Help")

        # Apply styles and add sidebar buttons
        sidebarButtonStyle = """
            QPushButton {
                font-family: 'Arial';
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
        
        for btn in [btnHome, btnHelp, btnOpen]:
            btn.setIconSize(QSize(25, 25))
            btn.setStyleSheet(sidebarButtonStyle)
        
        sidebarLayout.addWidget(btnHome)
        sidebarLayout.addWidget(btnOpen)
        sidebarLayout.addStretch(1)
        sidebarLayout.addWidget(btnHelp)
        
        # Stacked widget setup for main content area
        self.contentStack = QStackedWidget()
        self.canvas = QWidget()
        self.canvas.setStyleSheet("background-color: #FFF8DC;")
        canvasLayout = QVBoxLayout(self.canvas)
        self.recentProjectsList = QListWidget()
        canvasLayout.addWidget(self.recentProjectsList, 1)
        self.contentStack.addWidget(self.canvas)
        
        self.helpTextLabel = QLabel()
        self.helpTextLabel.setStyleSheet("color: black; padding: 10px;")
        self.helpTextLabel.setWordWrap(True)
        self.contentStack.addWidget(self.helpTextLabel)

        # Finalize main layout
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.sidebar, 0)
        mainLayout.addWidget(self.contentStack, 1)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        
        # Combine title bar and main layout
        finalLayout = QVBoxLayout()
        finalLayout.addWidget(self.titleBar)
        finalLayout.addLayout(mainLayout)
        finalLayout.setContentsMargins(0, 0, 0, 0)
        finalLayout.setSpacing(0)
        
        # Set the final layout to the central widget
        container = QWidget()
        container.setLayout(finalLayout)
        self.setCentralWidget(container)
        
        # Connect signals to slots for button actions
        btnHome.clicked.connect(self.on_home_clicked)
        btnOpen.clicked.connect(self.on_open_clicked)
        btnHelp.clicked.connect(self.on_help_clicked)
    
    def recolor_icon(self, icon_path, color):
        """
        Recolors the provided icon with the specified color.
        """
        pixmap = QPixmap(icon_path)
        mask = pixmap.createMaskFromColor(QColor('black'), Qt.MaskMode.MaskOutColor)
        colored_pixmap = QPixmap(pixmap.size())
        colored_pixmap.fill(QColor(color))
        colored_pixmap.setMask(mask)
        return QIcon(colored_pixmap)
    
    def load_recent_projects(self):
        """
        Loads and displays the list of recent projects from a JSON file.
        """
        self.recentProjectsList.clear()
        try:
            with open('recent_projects.json', 'r') as file:
                recent_projects = json.load(file)
            for project in recent_projects:
                item = QListWidgetItem(os.path.basename(project['path']))
                item.setToolTip(project['path'])  # Full path as tooltip
                self.recentProjectsList.addItem(item)
        except (FileNotFoundError, json.JSONDecodeError):
            pass 
    
    def mousePressEvent(self, event):
        """
        Captures the initial position when the mouse is pressed to allow moving the frameless window.
        """
        if self.titleBar.rect().contains(event.position().toPoint()):  # Check if click is within title bar
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """
        Allows the window to be moved by dragging the title bar.
        """
        if not self.oldPos:
            return
        if self.titleBar.rect().contains(event.position().toPoint()):
            delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()
            
    def toggleMaximize(self):
        """
        Toggles the window between normal and maximized states.
        """
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def on_open_clicked(self):
        """
        Handles the 'Open' button click. Opens a file dialog to select a file and loads it in MainWindow.
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xls *.xlsx);;CSV Files (*.csv)")
        if file_name:
            self.open_file(file_name)

    def open_file(self, file_path):
        """
        Initializes and shows the main window with the loaded file, then closes the start page.
        """
        self.main_window = MainWindow()
        self.main_window.load_data(file_path)
        self.main_window.show()
        self.update_recent_projects(file_path)  # Update the list of recent projects
        self.close()  # Close the start page

    def update_recent_projects(self, file_path):
        """
        Updates the list of recent projects in a JSON file and refreshes the list in the UI.
        """
        # Read existing projects and update with the new one
        try:
            with open('recent_projects.json', 'r') as file:
                recent_projects = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            recent_projects = []

        new_entry = {'path': file_path, 'date_modified': QFileInfo(file_path).lastModified().toString()}
        recent_projects = [proj for proj in recent_projects if proj['path'] != file_path]  # Remove duplicate
        recent_projects.insert(0, new_entry)  # Insert new at the top
        recent_projects = recent_projects[:10]  # Keep only the most recent 10 entries

        with open('recent_projects.json', 'w') as file:
            json.dump(recent_projects, file)

        self.load_recent_projects()
        
    def setupContentAreas(self):
        self.recentProjectsView = QWidget()
        rpLayout = QVBoxLayout(self.recentProjectsView)
        self.recentProjectsList = QListWidget()
        rpLayout.addWidget(self.recentProjectsList)
        self.contentStack.addWidget(self.recentProjectsView)

        self.helpTextView = QWidget()
        helpLayout = QVBoxLayout(self.helpTextView)
        self.helpTextLabel = QLabel()
        self.helpTextLabel.setWordWrap(True)
        helpLayout.addWidget(self.helpTextLabel)
        self.contentStack.addWidget(self.helpTextView)
        
    def on_help_clicked(self):
        """
        Displays help information in the content area when the 'Help' button is clicked.
        """
        self.recentProjectsList.setVisible(False)
        self.helpTextLabel.setVisible(True)
        
        self.helpTextLabel.setText("""
            <html>
            <head>
                <style>
                    body { font-family: "Segoe UI", sans-serif; font-size: 14px; }
                    h2 { color: #333366; }
                    b { font-weight: bold; color: #333366; }
                    p { line-height: 1.6; }
                    .instructions { margin-bottom: 15px; }
                    .step { margin-top: 10px; }
                </style>
            </head>
            <body>
                <div class="instructions">
                    <h2>Starting</h2>
                    <p>To begin, navigate to the <b>Home Page</b> and select <b>Open</b> to open an existing file. Locate and open the desired file. Upon opening, the application presents a drop-down menu for sheet selection within the Excel file.</p>
                    <p class="step">The selected sheet's data will be displayed, and you are free to view or modify the content as required.</p>
                </div>
                
                <h2>Graphing</h2>
                <p>To visualize data, open the file and select the <b>Graph</b> option. A new window will emerge, showcasing a bar graph representing the selected dataset. This interactive graphing window enables you to specify parameters such as <b>SLO</b>, <b>Measure</b>, <b>Target</b>, and the desired <b>Year Range</b> for the graph.</p>
            </body>
            </html>
        """)
        
        self.contentStack.setCurrentWidget(self.helpTextLabel)

    def on_home_clicked(self):
        """
        Resets the visibility of UI components to show the home page content.
        """
        self.contentStack.setCurrentWidget(self.recentProjectsList)
        self.recentProjectsList.setVisible(True)
