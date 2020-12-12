import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from register_ui import Ui_MainWindow


class Register(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    reg = Register()
    reg.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
