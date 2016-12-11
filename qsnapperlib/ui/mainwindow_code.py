from PyQt5.QtWidgets import QMainWindow, QMessageBox, qApp, QLabel, QProgressBar
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtCore import QRunnable, QProcess, QObject, pyqtSignal, QThreadPool, Qt
from qsnapperlib.ui.mainwindow import Ui_MainWindow
from qsnapperlib.snapperhandler import getSnapperTree
from qsnapperlib.ui.dlgnewsnapshot_code import NewSnapshotUi
import subprocess
import codecs

class ProcessSignalHandler(QObject):
    started = pyqtSignal()
    finish = pyqtSignal()
    error = pyqtSignal(str, str)
    statusUpdate = pyqtSignal(str)
    statusProgress = pyqtSignal(int)
    
    def __init__(self):
        QObject.__init__(self)
    
class Runner(QRunnable):
    def __init__(self, command, errorString):
        QRunnable.__init__(self)
        self.command = command
        self.errorString = errorString
        self.signals = ProcessSignalHandler()
        self.content = ""
        
    def run(self):
        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess().MergedChannels)
        self.process.readyReadStandardOutput.connect(self.appendLine)
        self.process.finished.connect(self.finished)
        self.signals.started.emit()
        
        self.process.start(self.command)
        self.process.waitForFinished()
        
    def finished(self):
        if self.process.exitCode() != 0:
            self.signals.error.emit("%s. \nExit status : %s" % (self.errorString, self.process.exitCode()), self.content)
        self.signals.finish.emit()
        
    def appendLine(self):
        readLine = codecs.decode(self.process.readAllStandardOutput())
        self.content = "%s %s" % (self.content, readLine)

class QStandardItem2(QStandardItem):
    def __init__(self, *args):
        QStandardItem.__init__(self, *args)
        self.setEditable(False)
        
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.prgProcessing = QProgressBar()
        self.prgProcessing.setVisible(False)
        self.lblProcessing = QLabel("Ready")
        self.ui.lstSnapshots.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lstSnapshots.customContextMenuRequested.connect(self._displayMenu)
        
        self.ui.statusbar.addWidget(self.prgProcessing)
        self.ui.statusbar.addWidget(self.lblProcessing)
        
        self.processing = QThreadPool()
        
        self.ui.lstConfigs.currentItemChanged.connect(self.fillSnapshots)
        self.ui.actionOpen_Snapshot_in_file_manager.triggered.connect(self.browseSnapshot)
        self.ui.actionDelete_this_snapshot.triggered.connect(self._delete)
        self.ui.actionUpdate_list.triggered.connect(self.refreshSnapshots)
        self.ui.actionCreate_new_snapshot.triggered.connect(self._addSnapshot)
        
        self.ui.actionAbout_Qt.triggered.connect(qApp.aboutQt)
        
        self.updateLists()
        if "error" in self.configs.keys():
            QMessageBox().critical(self, "Error", "Error while launching QSnapper : \n%s" % (self.configs["error"]), QMessageBox().Ok)
            exit()
        self.fillConfig()
        
        self.ui.lstConfigs.setCurrentRow(0)
        
        self.show()
    

    def updateLists(self):
        """Reload only internal Snapshots and configs list"""
        self.configs = getSnapperTree()

    def fillSnapshots(self):
        """Update Tree list from internal snapshot List. Call updateLists before.."""
        if self.ui.lstSnapshots.model():
            self.ui.lstSnapshots.model().clear()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Number", "UID", "Description", "Date", "Type", "Cleanup method", "Associated"])
        config = self.getSelectedConfig()

        # List all snapshots
        for snapshot in self.configs[config]["snapshots"]:
            number = QStandardItem2(snapshot["number"])
            number.setIcon(QIcon.fromTheme("camera-photo"))
            number.setCheckable(True)
            # If its a post snapshot, get associated pre snapshot. If not, put nothing.
            if snapshot["type"] == "post":
                associated = snapshot["pre"]
            else:
                associated = ""
            
            model.appendRow([QStandardItem2(number), QStandardItem2(snapshot["uid"]), QStandardItem2(snapshot["description"]), QStandardItem2(snapshot["date"]), QStandardItem2(snapshot["type"]), QStandardItem2(snapshot["cleanup"]) ,QStandardItem2(snapshot["pre"])])
            
        self.ui.lstSnapshots.setModel(model)
        for column in range(self.ui.lstSnapshots.model().columnCount()):
            self.ui.lstSnapshots.resizeColumnToContents(column)
    
    def fillConfig(self):
        """Update config list from internal Snapshot list. Call updateLists before."""
        self.ui.lstConfigs.clear()
        for config in self.configs.keys():
            self.ui.lstConfigs.addItem(config)

    def refreshSnapshots(self):
        """ Reload all snapshots content """
        self.updateLists()
        self.fillSnapshots()
    
    def getSelectedConfig(self):
        """Return the name of actual config
        
        :return: name of Selected config
        :rtype: str
        """
        return self.ui.lstConfigs.currentItem().text()
    
    def getSelectedSnapshot(self):
        """Return the number of actual Snapshot
        
        INFO : If snapshot has not selected, return None
        
        :return: number of Snapshot
        :rtype: str
        """
        try:
            return self.ui.lstSnapshots.model().index(self.ui.lstSnapshots.selectedIndexes()[0].row(), 0).data()
        except IndexError:
            return None

    
    def bindProcess(self, runner):
        """Bind a task to window signals for handle.
        
        :param runner: An QRunnable object (See Runner class)
        :type runner: QRunnable:
        """
        runner.signals.error.connect(self._displayError)
        runner.signals.started.connect(self._switchToProcessingMode)
        runner.signals.finish.connect(self._switchToIdleMode)
 
    def _switchToProcessingMode(self):
        """Switch window to process mode. Display progressbar, and disable all controls while processing."""
        self.ui.lstConfigs.setEnabled(False)
        self.ui.lstSnapshots.setEnabled(False)
        self.lblProcessing.setText("Processing ... Waiting for finish ...")
        self.prgProcessing.setVisible(True)
    
    def _switchToIdleMode(self):
        """Switch window to available mode. Hide progressbar, and enable all controls after process"""
        self.ui.lstConfigs.setEnabled(True)
        self.ui.lstSnapshots.setEnabled(True)
        self.lblProcessing.setText("Ready")
        self.prgProcessing.setVisible(False)
        
        self.updateLists()
        self.fillSnapshots()
        
    def _displayError(self, message, output):
        """Display an error (handle from Runner signals).
        
        :param message: Error message (see Runner class).
        :param output: Result of command (standard output and error)
        :type message: str
        :type output: str """
        print("ERROR")
        dlg = QMessageBox()
        dlg.setDetailedText(output)
        dlg.setText(message)
        dlg.setWindowTitle("Error")
        dlg.setIcon(3)
        dlg.exec_()
        
    def _displayMenu(self, pos):
        menu = self.ui.menuSnapshot
        menu.popup(self.ui.lstSnapshots.mapToGlobal(pos))
 
    def browseSnapshot(self):
        """Launch file manager to Snapshot directory. Triggered from menu"""
        subprocess.Popen(["xdg-open", self.configs[self.getSelectedConfig()]["subvolume"] + "/.snapshots/" + str(self.getSelectedSnapshot()) + "/snapshot/"])
     
    def _delete(self):
        """Delete selected snapshot. Triggered from menu."""
        selectedSnapshot = self.getSelectedSnapshot()
        if not selectedSnapshot:
            QMessageBox().critical(self, "Remove", "Please select a valid snapshot")
            return None
        message = QMessageBox().question(self, "Remove", "Do you want to remove selected snapshot ?\n\nCurrent config : %s\nCurrent snapshot : %s" % (self.getSelectedConfig(), selectedSnapshot), QMessageBox().Yes | QMessageBox().No)
        if message == QMessageBox().Yes:
            # Create process and run.
            deleter = Runner("snapper -c %s delete %s" % (self.getSelectedConfig(), selectedSnapshot), "Unable to remove snapshot %s on %s config" % (selectedSnapshot, self.getSelectedConfig()))
            self.bindProcess(deleter)
            self.processing.start(deleter)
            
    def _addSnapshot(self):
        """Add new snapshot. Triggered from menu"""
        window = NewSnapshotUi()
        window.ui.cmbConfigs.setCurrentText(self.getSelectedConfig())
        if window.exec_():
            # if validate, get command and call it. 
            command = window.generateCommand()
            creator = Runner(command, "Unable to create new snapshot (command : %s)" % (command))
            self.bindProcess(creator)
            self.processing.start(creator)
            self.lblProcessing.setText("Running : %s" % (command))
