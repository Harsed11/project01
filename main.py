import sys
import random
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            with QPainter(self) as qp:
                qp.setBrush(QColor('yellow'))
                d = random.randint(20, 150)
                x = random.randint(0, self.width() - d)
                y = random.randint(70, self.height() - d)
                qp.drawEllipse(x, y, d, d)
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
