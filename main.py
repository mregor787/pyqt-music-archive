import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from entry_ui import Ui_MainWindow


class Entry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupButtons()

    def setupButtons(self):
        self.regToLogButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1)
        )
        self.logToRegButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0)
        )


def main():
    app = QApplication(sys.argv)
    en = Entry()
    en.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
