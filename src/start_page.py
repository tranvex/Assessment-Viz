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
        self.load_recent_projects()

    def initUI(self):               
        # Custom title bar setup
        self.titleBar = QWidget()
        self.titleBarLayout = QHBoxLayout()
        self.titleBar.setStyleSheet("background-color: #686868;")
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
                background-color: #686868;
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
        self.sidebar.setStyleSheet("background-color: #949494; color: white;")
        self.sidebar.setFixedWidth(150)
        sidebarLayout = QVBoxLayout(self.sidebar)
        sidebarLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        sidebarLayout.setContentsMargins(10, 10, 10, 10)
        sidebarLayout.setSpacing(10)
        
        self.stacked_widget()
        
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

        self.final_layout()
        
        # Connect signals to slots for button actions
        btnHome.clicked.connect(self.on_home_clicked)
        btnOpen.clicked.connect(self.on_open_clicked)
        btnHelp.clicked.connect(self.on_help_clicked)
        
        self.recentProjectsList.itemClicked.connect(self.on_recent_project_clicked)

    def final_layout(self):
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
        
    def stacked_widget(self):
        # Stacked widget setup for main content area
        self.contentStack = QStackedWidget()
        self.mainContent = QWidget()  # Main content widget
        self.mainContentLayout = QVBoxLayout(self.mainContent)
        self.recentProjectsList = QListWidget()
        self.mainContentLayout.addWidget(self.recentProjectsList)
        
        if not hasattr(self, 'helpTextWidget'):
            self.helpTextWidget = QWidget()  # Help text widget
            self.helpTextLayout = QVBoxLayout(self.helpTextWidget)
            self.helpTextLabel = QLabel("""
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
                         <p>To begin, navigate to the <b>Home Page</b> and select <b>Open</b> to open an existing file. Locate and open the desired file. Upon opening, the application presents a tabular view for sheet selection within the Excel file.</p>
                         <p class="step">The selected sheet's data will be displayed, and you are free to view or modify the content as required.</p>
                     </div>
                    
                    <h2>Graphing</h2>
                    <p>To visualize data, open the file and select the <b>Graph</b> option. A new window will emerge, showcasing a bar graph representing the selected dataset. This interactive graphing window enables you to specify parameters such as <b>SLO</b>, <b>Measure</b>, <b>Target</b>, and the desired <b>Year Range</b> for the graph.</p>
                 </body>
                 </html>
             """)
            self.helpTextLabel.setWordWrap(True)
            self.helpTextLayout.addWidget(self.helpTextLabel)
            
            self.contentStack.addWidget(self.helpTextWidget)

        # Add widgets to the stacked widget
        self.contentStack.addWidget(self.mainContent)
        self.contentStack.setCurrentWidget(self.mainContent)
        
        
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
        self.update_recent_projects(file_path)
        self.close()

    
    def on_home_clicked(self):
        self.contentStack.setCurrentWidget(self.mainContent)

        
    def on_help_clicked(self):
        self.contentStack.setCurrentWidget(self.helpTextWidget)
        
    def load_recent_projects(self):
        self.recentProjectsList.clear()
        try:
            with open('recent_projects.json', 'r') as file:
                recent_projects = json.load(file)
                for project in recent_projects:
                    item_text = f"{project['name']} - Last opened on {project['date_modified']}"
                    item = QListWidgetItem(item_text)
                    item.setToolTip(project['path'])
                    self.recentProjectsList.addItem(item)
        except FileNotFoundError:
            QMessageBox.information(self, "Information", "No recent projects file found. Starting fresh.")
        except json.JSONDecodeError:
            QMessageBox.warning(self, "Warning", "Corrupted recent projects file.")

    def get_project_name_from_path(file_path):
        # Extracts the base name (e.g., 'SWE Datafile2023.xlsx') and then splits off the extension.
        base_name = os.path.basename(file_path)
        project_name, _ = os.path.splitext(base_name)
        return project_name

    def update_recent_projects(self, file_path):
        project_name = StartPage.get_project_name_from_path(file_path)
        date_modified = QDateTime.currentDateTime().toString(Qt.DateFormat.ISODate)
        
        new_entry = {
            'name': project_name,
            'path': file_path,
            'date_modified': date_modified
        }

        try:
            # Load existing projects from file
            if os.path.exists('recent_projects.json'):
                with open('recent_projects.json', 'r') as file:
                    recent_projects = json.load(file)
            else:
                recent_projects = []

            # Remove any existing entry for this path to prevent duplicates
            recent_projects = [proj for proj in recent_projects if proj['path'] != file_path]
            # Insert the new entry at the beginning
            recent_projects.insert(0, new_entry)
            # Keep only the most recent 10 entries
            recent_projects = recent_projects[:10]

            # Write updated projects back to file
            with open('recent_projects.json', 'w') as file:
                json.dump(recent_projects, file, indent=4)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update recent projects: {str(e)}")

    def on_recent_project_clicked(self, item):
        """Opens the file when a recent project is clicked from the list."""
        file_path = item.toolTip()
        self.open_file(file_path)  # Function to open the file