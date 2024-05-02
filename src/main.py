import sys
from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer
from start_page import StartPage

def main():
    app = QApplication(sys.argv)
    # Load the image file for the splash screen
    pixmap = QPixmap(r"C:\Users\ghost\Desktop\Assessment-Viz\src\assets\splash.jpg")
    splash = QSplashScreen(pixmap, Qt.WindowType.WindowStaysOnTopHint)
    splash.showMessage("Loading...", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter, Qt.GlobalColor.black)
    splash.show()

    # Initialize the main window while the splash screen is displayed
    QTimer.singleShot(2500, splash.close)  # Keep the splash for 2.5 seconds

    start_page = StartPage()
    start_page.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()