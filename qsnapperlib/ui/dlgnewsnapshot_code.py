from PyQt5.QtWidgets import QDialog
from qsnapperlib.ui.dlgnewsnapshot import Ui_dlgNewSnapshot
from qsnapperlib.snapperhandler import getSnapperTree

class NewSnapshotUi(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_dlgNewSnapshot()
        self.ui.setupUi(self)
        
        self.ui.lblPaired.setVisible(False)
        self.ui.cmbPaired.setVisible(False)
        
        self.ui.optPost.toggled.connect(self.generateCommand)
        self.ui.optPre.toggled.connect(self.generateCommand)
        self.ui.optSingle.toggled.connect(self.generateCommand)
        self.ui.lneName.textChanged.connect(self.generateCommand)
        self.ui.cmbCleanAlgo.currentTextChanged.connect(self.generateCommand)
        self.ui.cmbPaired.currentTextChanged.connect(self.generateCommand)
        self.ui.cmbConfigs.currentTextChanged.connect(self.generateCommand)
        
        self.fillWindow()
        self.generateCommand()
    
    def fillWindow(self):
        """Fill window from snapshots tree"""
        self.ui.cmbConfigs.clear()
        self.ui.cmbPaired.clear()
        self.ui.optPost.setEnabled(True)
        self.ui.optSingle.setChecked(True)
        
        snappertree = getSnapperTree()
        pre_count = 0
        for config in snappertree:
            self.ui.cmbConfigs.addItem(config)
            for snapshot in snappertree[config]["snapshots"]:
                snapshotline = snappertree[config]["snapshots"][snapshot]
                if snapshotline["type"] == "pre": 
                    # If its 'pre' snapshot, add in paired list.
                    self.ui.cmbPaired.addItem(snapshotline["number"])
                    pre_count = pre_count + 1
            
            # We don't have found a pre snapshot, post can't be created
            if pre_count == 0:
                self.ui.optPost.setEnabled(False)


    def generateCommand(self):
        """Generate command from content, and update text display command (for information).
        :return: Command
        :rtype: str"""
        # Create initial command with config
        command = "snapper -c %s create" % (self.ui.cmbConfigs.currentText())
        # Add Description
        if self.ui.lneName.text() != "":
            # Remove all " 
            command = "%s -d \"%s\"" % (command, self.ui.lneName.text().replace("\"", ""))
        # Check what type
        if self.ui.optSingle.isChecked():
            stype = "single"
            extra = ""
        elif self.ui.optPre.isChecked():
            stype = "pre"
            extra = ""
        elif self.ui.optPost.isChecked():
            stype = "post"
            extra = "--pre-number %s" % (self.ui.cmbPaired.currentText())
        else:
            stype = "single"
            extra = ""
        command = "%s -t %s %s" % (command, stype, extra) 
        # Define cleanup algo
        command = "%s -c %s" % (command, self.ui.cmbCleanAlgo.currentText().lower())
        
        self.ui.txtCommandDisplay.setText(command)
        return command
