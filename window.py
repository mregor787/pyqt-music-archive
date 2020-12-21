from PyQt5.QtWidgets import QMainWindow, QLineEdit


class Window(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.sql_manager = app.sql_manager
        self.setupUi(self)
        self.setupButtons()
        self.setFocus()

    def setupButtons(self):
        pass

    def pageSwitch(self, stacked_widget, index: int):
        stacked_widget.setCurrentIndex(index)
        for obj in stacked_widget.currentWidget().findChildren(QLineEdit):
            obj.clear()
        self.setFocus()
