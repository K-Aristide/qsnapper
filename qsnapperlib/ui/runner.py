from PyQt5.QtWidgets import QDialog, QProgressBar, QTextBrowser, QLabel, QPushButton, QVBoxLayout, QGroupBox
from PyQt5.QtCore import QProcess, Qt


class RunnerWindow(QDialog):
    def __init__(self, command, arguments):
        QDialog.__init__(self)
        
        self.setFixedSize(900, 500)
        
        self.setWindowTitle("Closed when finish")
        
        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        
        
        self.vbox = QVBoxLayout()
        self.label1 = QLabel("Running : %s %s" % (command, arguments))
        self.label1.setWordWrap(True)
        self.textbox = QTextBrowser()
        self.progressbar = QProgressBar()
        self.progressbar.setMaximum(0)
        
        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.textbox)
        self.vbox.addWidget(self.progressbar)
        self.setLayout(self.vbox)
        
        self._process = QProcess()
        self._process.finished.connect(self.finish)
        self._process.readyRead.connect(self._read)
        self._process.start(command, arguments.split(" "))
        self.show()
        
        
    def _read(self):
        self.textbox.append(self._process.readAll().data().decode("utf-8"))
        
    def finish(self):
        self.returncode = self._process.exitCode()
        self.close()
