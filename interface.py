# coding = utf-8
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 200)
    w.move(300, 300)
    w.setWindowTitle("GUI Application by Qt")
    w.show()
    sys.exit(app.exec())