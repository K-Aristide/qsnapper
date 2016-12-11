from PyQt5.QtWidgets import QApplication
from sys import argv
from qsnapperlib.ui.mainwindow_code import MainWindow

app = QApplication(argv)

x = MainWindow()
x.show()

exit(app.exec_())
