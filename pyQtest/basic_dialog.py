import sys
from PyQt5.QtWidgets import QApplication, QDialog

class ImageProcessing(QDialog):
    def __init__(self):
        super(ImageProcessing, self).__init__()

        # Set up the user interface from Designer
        #self.ui = Ui_ImageDialog()
        self.ui = QDialog()
        self.ui.setupUi(self)

        # Make some local modifications
        self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons
        self.ui.okButton.clicked.connect(self.accept)
        self.ui.cancelButton.clicked.connect(self.reject)

#app = QApplication(sys.argv)
#window = QDialog()
# Ui_ImageDialog() its a fake class
#ui = Ui_ImageDialog()
#ui.setupUi(window)

#window.show()
#sys.exit(app.exec_())