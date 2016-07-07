from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, time

class Test(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.pts = [[80, 490], [180, 0], [280, 0], [430, 0], [580, 0], [680, 0], [780, 0]]

    def poly(self, pts):
        return QPolygonF(map(lambda p: QPointF(*p), pts))

    def paintEvent(self, event):
        painter = QPainter(self)

        pts = self.pts[:]

        painter.setPen(QPen(QColor(Qt.darkGreen), 3))
        painter.drawPolyline(self.poly(pts))

        painter.setBrush(QBrush(QColor(255, 0, 0)))
        painter.setPen(QPen(QColor(Qt.black), 1))

        for x, y in pts:
            painter.drawEllipse(QRectF(x - 4, y - 4, 8, 8))

        # print pts

    def wave(self):

        for point in self.pts:
            while point[1] < 600:
                point[1] += 1
                self.update()
                QApplication.processEvents()
                time.sleep(0.0025)


if __name__ == '__main__':
    example = QApplication(sys.argv)
    test2 = Test()
    test2.resize(800, 600)
    test2.show()
    test2.raise_()
    test2.wave()
    sys.exit(example.exec_())