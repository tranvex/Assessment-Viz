from PyQt6.QtGui import QPalette, QColor


def set_custom_palette(app):
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(211, 211, 211))
    palette.setColor(QPalette.WindowText, QColor("white"))
    palette.setColor(QPalette.Base, QColor(15, 15, 15))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QColor("white"))
    palette.setColor(QPalette.ToolTipText, QColor("white"))
    palette.setColor(QPalette.Text, QColor("white"))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor("white"))
    palette.setColor(QPalette.BrightText, QColor("red"))
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, QColor("black"))
    app.setPalette(palette)


def set_stylesheet(app):
    app.setStyleSheet(
        """
        QMainWindow {
            background-color: #999;
        }
        QPushButton {
            background-color: #555;
            color: white;
            border: none;
            padding: 5px;
            min-width: 70px;
            border-radius: 10px;
        }

        QPushButton:hover {
            background-color: #777;
        }
    """
    )
