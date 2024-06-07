from login import LoginWindow
from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication
import sys
from share import SI
from mainUI import MainWindow

app = QApplication(sys.argv)
# SI.loginWin = LoginWindow()
# SI.loginWin.show()
SI.mainWin = MainWindow()
SI.mainWin.show()
app.exec_()