from window import Window
from main_window_ui import Ui_MainWindow


class MainWindow(Window, Ui_MainWindow):
    def __init__(self, app):
        super().__init__(app)

    def setupButtons(self):
        self.toProfileButton.clicked.connect(
            lambda: self.pageSwitch(self.stackedWidget, 1)
        )
        self.profileBackButton.clicked.connect(
            lambda: self.pageSwitch(self.stackedWidget, 0)
        )
