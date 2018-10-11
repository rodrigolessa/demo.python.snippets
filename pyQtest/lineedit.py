import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lblVideo = QtWidgets.QLabel('Video')
        self.lblOutput = QtWidgets.QLabel('Output file')
        self.lblThresh = QtWidgets.QLabel('Threshold')
        self.lblBlob = QtWidgets.QLabel('Minimum blob size')

        self.txtOutput = QtWidgets.QLineEdit()

        self.btnAnalyse = QtWidgets.QPushButton('Analyse')
        self.btnClear = QtWidgets.QPushButton('Clear')

        self.btnAnalyse.clicked.connect(self.btnAnalyseClick)
        self.btnClear.clicked.connect(self.btnAnalyseClick)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.lblVideo)
        hbox.addStretch()
        hbox.addWidget(self.lblOutput)
        hbox.addWidget(self.txtOutput)
        hbox.addStretch()

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.lblThresh)
        vbox.addWidget(self.lblBlob)
        vbox.addWidget(self.btnAnalyse)
        vbox.addWidget(self.btnClear)

        # Left, Top, Width, Height
        self.setGeometry(500, 400, 500, 250)
        self.setLayout(vbox)
        self.setWindowTitle('Computer Vision - Analysing Image')
        self.show()

    def btnAnalyseClick(self):
        sender = self.sender()
        if sender.text() == 'Analyse':
            self.lblBlob.setText(self.txtOutput.text())
            print(self.txtOutput.text())
        else:
            self.txtOutput.clear()

app = QtWidgets.QApplication(sys.argv)
clsWindow = Window()

sys.exit(app.exec_())