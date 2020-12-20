from PyQt5.QtWidgets import QMainWindow
from main_menu_ui import Ui_MainWindow


class MainMenu(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.sql_manager = app.sql_manager
        self.setupUi(self)
        self.setupButtons()
        self.setFocus()

    def setupButtons(self):
        pass
