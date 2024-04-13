#main 
from PyQt6.QtWidgets import QApplication
from start_page import StartPage
import sys

def main():
    app = QApplication(sys.argv)
    startPage = StartPage()
    startPage.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()