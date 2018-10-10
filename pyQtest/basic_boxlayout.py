import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle('Computer Vision - Analysing Image')
    # Left, Top, Width, Height
    w.setGeometry(500, 400, 500, 250)

    lblVideo = QtWidgets.QLabel('Video')
    lblOutput = QtWidgets.QLabel('Output file')
    lblThresh = QtWidgets.QLabel('Threshold')
    lblBlob = QtWidgets.QLabel('Minimum blob size')

    btnAnalyse = QtWidgets.QPushButton('Analyse')

    #l1.setPixmap(QtGui.QPixmap('160px-Python_and_Qt.svg.png'))
    #l2.setText('Video')
    #l2.move(10, 10)

    hbox = QtWidgets.QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(lblVideo)
    hbox.addStretch()
    hbox.addWidget(lblOutput)
    hbox.addStretch()

    vbox = QtWidgets.QVBoxLayout()
    vbox.addLayout(hbox)
    vbox.addWidget(lblThresh)
    vbox.addWidget(lblBlob)
    vbox.addWidget(btnAnalyse)

    w.setLayout(vbox)
    w.show()

    sys.exit(app.exec_())

window()