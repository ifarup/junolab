import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = 'main.ui'
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class JunoLab(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = JunoLab()
    window.show()
    sys.exit(app.exec_())
