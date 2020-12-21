from hashlib import sha256

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from entry_ui import Ui_MainWindow


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
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.sql_manager = app.sql_manager
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
        self.regButton.clicked.connect(self.registerUser)
        self.logButton.clicked.connect(self.loginUser)

    def pageSwitch(self, stacked_widget, index: int):
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
        if self.sql_manager.get_user(username):
            return
        self.sql_manager.add_user(username, get_hash(password), email, 'images/profile.png')
        self.pageSwitch(self.stackedWidget, 1)

    def loginUser(self):
        username = self.logUsernameInput.text()
        password = self.logPasswordInput.text()
        if '' in [username, password]:
            return
        user = self.sql_manager.get_user(username)
        if not user:
            return
        if user[0]['password_hash'] != get_hash(password):
            return
        self.app.changeWindow('main_menu')
