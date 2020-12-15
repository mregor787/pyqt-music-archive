import sys
from hashlib import sha256

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from entry_ui import Ui_MainWindow
from sql_manager import SqlManager


def get_hash(string: str) -> str:
    m = sha256()
    m.update(bytes(string, encoding='utf8'))
    return m.hexdigest()


def check_password(password: str) -> bool:
    if len(password) < 6:
        return False
    if password.lower() == password or password.upper() == password:
        return False
    if not any(map(lambda x: x.isdigit(), password)):
        return False
    return True


class Entry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupButtons()
        self.setFocus()
        self.sql_manager = SqlManager('music.db')

    def setupButtons(self):
        self.regToLogButton.clicked.connect(
            lambda: self.pageSwitch(self.stackedWidget, 1)
        )
        self.logToRegButton.clicked.connect(
            lambda: self.pageSwitch(self.stackedWidget, 0)
        )
        self.regButton.clicked.connect(
            lambda: self.registerUser()
        )

    def pageSwitch(self, stacked_widget, index):
        for obj in [self.regForm, self.logForm][abs(index - 1)].children():
            if isinstance(obj, QLineEdit):
                obj.setText('')
        stacked_widget.setCurrentIndex(index)
        self.setFocus()

    def registerUser(self):
        username = self.regUsernameInput.text()
        password = self.regPasswordInput.text()
        confirm = self.confirmInput.text()
        email = self.emailInput.text()
        if '' in [username, password, confirm, email]:
            return
        if password != confirm or not check_password(password):
            return
        self.sql_manager.add_user(username, get_hash(password), email)
        self.pageSwitch(self.stackedWidget, 1)


def main():
    app = QApplication(sys.argv)
    en = Entry()
    en.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
