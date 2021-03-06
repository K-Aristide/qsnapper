# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layoutWindow = QtWidgets.QVBoxLayout()
        self.layoutWindow.setObjectName("layoutWindow")
        self.verticalLayout_2.addLayout(self.layoutWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lstConfigs = QtWidgets.QListWidget(self.dockWidgetContents)
        self.lstConfigs.setObjectName("lstConfigs")
        self.verticalLayout.addWidget(self.lstConfigs)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuSnapshot = QtWidgets.QMenu(self.menuBar)
        self.menuSnapshot.setObjectName("menuSnapshot")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.dockInfo = QtWidgets.QDockWidget(MainWindow)
        self.dockInfo.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockInfo.setObjectName("dockInfo")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolBox = QtWidgets.QToolBox(self.dockWidgetContents_4)
        self.toolBox.setObjectName("toolBox")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 155, 463))
        self.page_3.setObjectName("page_3")
        self.formLayout = QtWidgets.QFormLayout(self.page_3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lblConfig = QtWidgets.QLabel(self.page_3)
        self.lblConfig.setObjectName("lblConfig")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblConfig)
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lblSelectSnapshot = QtWidgets.QLabel(self.page_3)
        self.lblSelectSnapshot.setObjectName("lblSelectSnapshot")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lblSelectSnapshot)
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lblDate = QtWidgets.QLabel(self.page_3)
        self.lblDate.setObjectName("lblDate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lblDate)
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lblSize = QtWidgets.QLabel(self.page_3)
        self.lblSize.setObjectName("lblSize")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lblSize)
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 96, 84))
        self.page_4.setObjectName("page_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.treeContent = QtWidgets.QTreeView(self.page_4)
        self.treeContent.setObjectName("treeContent")
        self.verticalLayout_4.addWidget(self.treeContent)
        self.toolBox.addItem(self.page_4, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        self.dockInfo.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockInfo)
        self.actionNew_Snapshot = QtWidgets.QAction(MainWindow)
        self.actionNew_Snapshot.setObjectName("actionNew_Snapshot")
        self.actionRemove_Snapshot = QtWidgets.QAction(MainWindow)
        self.actionRemove_Snapshot.setObjectName("actionRemove_Snapshot")
        self.actionClean_Snapshot = QtWidgets.QAction(MainWindow)
        self.actionClean_Snapshot.setObjectName("actionClean_Snapshot")
        self.actionReload_list_of_snapshots = QtWidgets.QAction(MainWindow)
        self.actionReload_list_of_snapshots.setObjectName("actionReload_list_of_snapshots")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionMount_this_snapshot = QtWidgets.QAction(MainWindow)
        self.actionMount_this_snapshot.setObjectName("actionMount_this_snapshot")
        self.actionExport_this_snapshot_into_image = QtWidgets.QAction(MainWindow)
        self.actionExport_this_snapshot_into_image.setObjectName("actionExport_this_snapshot_into_image")
        self.actionRefresh_snapshot_informations = QtWidgets.QAction(MainWindow)
        self.actionRefresh_snapshot_informations.setObjectName("actionRefresh_snapshot_informations")
        self.actionCreate_new_Snapshot = QtWidgets.QAction(MainWindow)
        self.actionCreate_new_Snapshot.setObjectName("actionCreate_new_Snapshot")
        self.actionDelete_Snapshots = QtWidgets.QAction(MainWindow)
        self.actionDelete_Snapshots.setObjectName("actionDelete_Snapshots")
        self.actionExplore_this_Snapshot = QtWidgets.QAction(MainWindow)
        self.actionExplore_this_Snapshot.setObjectName("actionExplore_this_Snapshot")
        self.actionOpen_File_Manager = QtWidgets.QAction(MainWindow)
        self.actionOpen_File_Manager.setObjectName("actionOpen_File_Manager")
        self.actionMount_this_Snapshot = QtWidgets.QAction(MainWindow)
        self.actionMount_this_Snapshot.setObjectName("actionMount_this_Snapshot")
        self.actionRollback_to_this_Snapshot = QtWidgets.QAction(MainWindow)
        self.actionRollback_to_this_Snapshot.setObjectName("actionRollback_to_this_Snapshot")
        self.actionExport_Snapshot_Image = QtWidgets.QAction(MainWindow)
        self.actionExport_Snapshot_Image.setObjectName("actionExport_Snapshot_Image")
        self.actionQuit_2 = QtWidgets.QAction(MainWindow)
        self.actionQuit_2.setObjectName("actionQuit_2")
        self.actionOpen_Snapshot_in_file_manager = QtWidgets.QAction(MainWindow)
        self.actionOpen_Snapshot_in_file_manager.setObjectName("actionOpen_Snapshot_in_file_manager")
        self.actionCreate_new_snapshot = QtWidgets.QAction(MainWindow)
        self.actionCreate_new_snapshot.setObjectName("actionCreate_new_snapshot")
        self.actionDelete_this_snapshot = QtWidgets.QAction(MainWindow)
        self.actionDelete_this_snapshot.setObjectName("actionDelete_this_snapshot")
        self.actionUpdate_list = QtWidgets.QAction(MainWindow)
        self.actionUpdate_list.setObjectName("actionUpdate_list")
        self.actionRollback_to_this_snapshot = QtWidgets.QAction(MainWindow)
        self.actionRollback_to_this_snapshot.setObjectName("actionRollback_to_this_snapshot")
        self.actionCompare_files = QtWidgets.QAction(MainWindow)
        self.actionCompare_files.setObjectName("actionCompare_files")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionAbout_QSnapper = QtWidgets.QAction(MainWindow)
        self.actionAbout_QSnapper.setObjectName("actionAbout_QSnapper")
        self.menuFile.addAction(self.actionOpen_Snapshot_in_file_manager)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_2)
        self.menuSnapshot.addAction(self.actionUpdate_list)
        self.menuSnapshot.addSeparator()
        self.menuSnapshot.addAction(self.actionCreate_new_snapshot)
        self.menuSnapshot.addAction(self.actionDelete_this_snapshot)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuHelp.addAction(self.actionAbout_QSnapper)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSnapshot.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QSnapper - BTRFS Snapshots manager"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Configs"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuSnapshot.setTitle(_translate("MainWindow", "Snaps&hot"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.dockInfo.setWindowTitle(_translate("MainWindow", "Info"))
        self.label.setText(_translate("MainWindow", "Config :"))
        self.lblConfig.setText(_translate("MainWindow", "Select config"))
        self.label_2.setText(_translate("MainWindow", "Snapshot :"))
        self.lblSelectSnapshot.setText(_translate("MainWindow", "Select Snapshot"))
        self.label_4.setText(_translate("MainWindow", "Date :"))
        self.lblDate.setText(_translate("MainWindow", "Date"))
        self.label_3.setText(_translate("MainWindow", "Size :"))
        self.lblSize.setText(_translate("MainWindow", "Size"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Informations"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Content"))
        self.actionNew_Snapshot.setText(_translate("MainWindow", "&New Snapshot"))
        self.actionRemove_Snapshot.setText(_translate("MainWindow", "&Remove Snapshot"))
        self.actionClean_Snapshot.setText(_translate("MainWindow", "&Clean Snapshot"))
        self.actionReload_list_of_snapshots.setText(_translate("MainWindow", "Reload &list of snapshots"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionMount_this_snapshot.setText(_translate("MainWindow", "&Mount this snapshot"))
        self.actionExport_this_snapshot_into_image.setText(_translate("MainWindow", "&Export this snapshot into image"))
        self.actionRefresh_snapshot_informations.setText(_translate("MainWindow", "Refresh snapshot informations"))
        self.actionCreate_new_Snapshot.setText(_translate("MainWindow", "Create new Snapshot"))
        self.actionDelete_Snapshots.setText(_translate("MainWindow", "Delete Snapshots"))
        self.actionExplore_this_Snapshot.setText(_translate("MainWindow", "Explore this Snapshot"))
        self.actionOpen_File_Manager.setText(_translate("MainWindow", "Open File Manager"))
        self.actionMount_this_Snapshot.setText(_translate("MainWindow", "Mount this Snapshot"))
        self.actionRollback_to_this_Snapshot.setText(_translate("MainWindow", "Rollback to this Snapshot"))
        self.actionExport_Snapshot_Image.setText(_translate("MainWindow", "&Export Snapshot Image"))
        self.actionQuit_2.setText(_translate("MainWindow", "&Quit"))
        self.actionOpen_Snapshot_in_file_manager.setText(_translate("MainWindow", "&Open Snapshot in file manager"))
        self.actionOpen_Snapshot_in_file_manager.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionCreate_new_snapshot.setText(_translate("MainWindow", "&Create new snapshot"))
        self.actionCreate_new_snapshot.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionDelete_this_snapshot.setText(_translate("MainWindow", "&Delete this snapshot"))
        self.actionDelete_this_snapshot.setShortcut(_translate("MainWindow", "Del"))
        self.actionUpdate_list.setText(_translate("MainWindow", "&Update list"))
        self.actionUpdate_list.setShortcut(_translate("MainWindow", "F5"))
        self.actionRollback_to_this_snapshot.setText(_translate("MainWindow", "&Rollback to this snapshot"))
        self.actionCompare_files.setText(_translate("MainWindow", "&Compare files"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "&About Qt"))
        self.actionAbout_QSnapper.setText(_translate("MainWindow", "About &QSnapper"))

