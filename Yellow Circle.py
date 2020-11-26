from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from random import randint
import UI


class MainWindow(QtWidgets.QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.drawing)

    def drawing(self, painter):
        painter.setBrush(QColor('Yellow'))
        rand = randint(1, 100)
        painter.drawEllipse(self.x, self.y, rand, rand)
