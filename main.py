import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from entry_ui import Ui_MainWindow


class Entry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupButtons()
        self.setFocus()

    def setupButtons(self):
        self.regToLogButton.clicked.connect(
            lambda: self.pageSwitch(self.stackedWidget, 1)
        )
        self.logToRegButton.clicked.connect(
            lambda: self.pageSwitch(self.stackedWidget, 0)
        )

    def pageSwitch(self, stacked_widget, index):
        stacked_widget.setCurrentIndex(index)
        self.setFocus()


def main():
    app = QApplication(sys.argv)
    en = Entry()
    en.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
