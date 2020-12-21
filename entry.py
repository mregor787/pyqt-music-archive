from hashlib import sha256

from window import Window
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


class Entry(Window, Ui_MainWindow):
    def __init__(self, app):
        super().__init__(app)

    def setupButtons(self):
        self.regToLogButton.clicked.connect(
            lambda: self.pageSwitch(self.stackedWidget, 1)
        )
        self.logToRegButton.clicked.connect(
            lambda: self.pageSwitch(self.stackedWidget, 0)
        )
        self.regButton.clicked.connect(self.registerUser)
        self.logButton.clicked.connect(self.loginUser)

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
        self.app.changeWindow('main_window')
