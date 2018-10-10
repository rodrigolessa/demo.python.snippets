import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle('Computer Vision - Analysing Image')
    # Left, Top, Width, Height
    w.setGeometry(500, 400, 500, 250)

    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)
    l3 = QtWidgets.QLabel(w)
    l4 = QtWidgets.QLabel(w)
    l5 = QtWidgets.QLabel(w)

    b1 = QtWidgets.QPushButton(w)

    l1.setPixmap(QtGui.QPixmap('160px-Python_and_Qt.svg.png'))
    l2.setText('Video')
    l3.setText('Output file')
    l4.setText('Threshold')
    l5.setText('Minimum blob size')

    l2.move(10, 10)
    l3.move(10, 30)
    l4.move(10, 60)
    l5.move(10, 90)

    l1.move(10, 120)

    b1.setText('Analyse')
    b1.move(400, 120)

    w.show()
    sys.exit(app.exec_())

window()