from PyQt5.QtWidgets import QWidget, QStyleOption, QStyle
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPaintEvent, QPainter


class QWidgetClickable(QWidget):
    clicked = pyqtSignal()

    def __init__(self, widget=None):
        super().__init__(widget)

    def mousePressEvent(self, event):
        self.clicked.emit()

    def paintEvent(self, a0: QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)
