# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QaWindow.ui'
#
# Created: Mon Apr 10 22:01:16 2017
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from FlightPlanner.Panels.TreeView import TreeView, TreeNode

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tabControl = QtGui.QTabWidget(self.frame)
        self.tabControl.setObjectName(_fromUtf8("tabControl"))
        self.tabQA = QtGui.QWidget(self.tabControl)
        self.tabQA.setObjectName(_fromUtf8("tabQA"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tabQA)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.treeView = TreeView(self.tabQA)#QtGui.QTreeWidget(self.tabQA)
        # self.treeView.setObjectName(_fromUtf8("treeView"))
        # self.treeView.headerItem().setText(0, _fromUtf8("1"))
        # self.horizontalLayout_2.addWidget(self.treeView)
        self.tabControl.addTab(self.tabQA, _fromUtf8(""))
        self.tabReport = QtGui.QWidget(self.tabControl)
        self.tabReport.setObjectName(_fromUtf8("tabReport"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tabReport)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.treeViewReport = TreeView(self.tabReport)#QtGui.QTreeWidget(self.tabReport)
        # self.treeViewReport.setObjectName(_fromUtf8("treeViewReport"))
        # self.treeViewReport.headerItem().setText(0, _fromUtf8("1"))
        # self.horizontalLayout_3.addWidget(self.treeViewReport)
        self.tabControl.addTab(self.tabReport, _fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.tabControl)
        self.pnlEntry = QtGui.QFrame(self.frame)
        self.pnlEntry.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pnlEntry.setFrameShadow(QtGui.QFrame.Raised)
        self.pnlEntry.setObjectName(_fromUtf8("pnlEntry"))
        self.verticalLayout = QtGui.QVBoxLayout(self.pnlEntry)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.richBox = QtGui.QPlainTextEdit(self.pnlEntry)
        self.richBox.setObjectName(_fromUtf8("richBox"))
        self.verticalLayout.addWidget(self.richBox)
        self.picSnapshot = QtGui.QFrame(self.pnlEntry)
        self.picSnapshot.setMinimumSize(QtCore.QSize(0, 200))
        self.picSnapshot.setFrameShape(QtGui.QFrame.StyledPanel)
        self.picSnapshot.setFrameShadow(QtGui.QFrame.Raised)
        self.picSnapshot.setObjectName(_fromUtf8("picSnapshot"))
        self.verticalLayout.addWidget(self.picSnapshot)
        self.lblDateTime = QtGui.QLabel(self.pnlEntry)
        self.lblDateTime.setText(_fromUtf8(""))
        self.lblDateTime.setObjectName(_fromUtf8("lblDateTime"))
        self.verticalLayout.addWidget(self.lblDateTime)
        self.horizontalLayout_4.addWidget(self.pnlEntry)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame_3 = QtGui.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblHeading = QtGui.QLabel(self.frame_3)
        self.lblHeading.setObjectName(_fromUtf8("lblHeading"))
        self.horizontalLayout.addWidget(self.lblHeading)
        self.txtComment = QtGui.QLineEdit(self.frame_3)
        self.txtComment.setObjectName(_fromUtf8("txtComment"))
        self.horizontalLayout.addWidget(self.txtComment)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.txtHeading = QtGui.QLineEdit(self.frame_2)
        self.txtHeading.setObjectName(_fromUtf8("txtHeading"))
        self.verticalLayout_3.addWidget(self.txtHeading)
        self.btnSubmit = QtGui.QPushButton(self.frame_2)
        self.btnSubmit.setObjectName(_fromUtf8("btnSubmit"))
        self.verticalLayout_3.addWidget(self.btnSubmit)
        self.verticalLayout_2.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.mniFile = QtGui.QMenu(self.menubar)
        self.mniFile.setObjectName(_fromUtf8("mniFile"))
        self.mniEdit = QtGui.QMenu(self.menubar)
        self.mniEdit.setObjectName(_fromUtf8("mniEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.mniFileExportQA = QtGui.QAction(MainWindow)
        self.mniFileExportQA.setObjectName(_fromUtf8("mniFileExportQA"))
        self.mniFileExportReport = QtGui.QAction(MainWindow)
        self.mniFileExportReport.setObjectName(_fromUtf8("mniFileExportReport"))
        self.mniFileClose = QtGui.QAction(MainWindow)
        self.mniFileClose.setObjectName(_fromUtf8("mniFileClose"))
        self.mniEditCopy = QtGui.QAction(MainWindow)
        self.mniEditCopy.setObjectName(_fromUtf8("mniEditCopy"))
        self.mniEditDelete = QtGui.QAction(MainWindow)
        self.mniEditDelete.setObjectName(_fromUtf8("mniEditDelete"))
        self.mniEditExportWord = QtGui.QAction(MainWindow)
        self.mniEditExportWord.setObjectName(_fromUtf8("mniEditExportWord"))
        self.mniEditComment = QtGui.QAction(MainWindow)
        self.mniEditComment.setObjectName(_fromUtf8("mniEditComment"))
        self.mniEditExportSST = QtGui.QAction(MainWindow)
        self.mniEditExportSST.setObjectName(_fromUtf8("mniEditExportSST"))
        self.mniEditRestoreView = QtGui.QAction(MainWindow)
        self.mniEditRestoreView.setObjectName(_fromUtf8("mniEditRestoreView"))
        self.mniFile.addAction(self.mniFileExportQA)
        self.mniFile.addAction(self.mniFileExportReport)
        self.mniFile.addSeparator()
        self.mniFile.addAction(self.mniFileClose)
        self.mniEdit.addAction(self.mniEditCopy)
        self.mniEdit.addAction(self.mniEditDelete)
        self.mniEdit.addSeparator()
        self.mniEdit.addAction(self.mniEditExportWord)
        self.mniEdit.addAction(self.mniEditComment)
        self.mniEdit.addAction(self.mniEditExportSST)
        self.mniEdit.addAction(self.mniEditRestoreView)
        self.menubar.addAction(self.mniFile.menuAction())
        self.menubar.addAction(self.mniEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabControl.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabControl.setTabText(self.tabControl.indexOf(self.tabQA), _translate("MainWindow", "QA", None))
        self.tabControl.setTabText(self.tabControl.indexOf(self.tabReport), _translate("MainWindow", "Report", None))
        self.lblHeading.setText(_translate("MainWindow", "Title: ", None))
        self.btnSubmit.setText(_translate("MainWindow", "Submit", None))
        self.mniFile.setTitle(_translate("MainWindow", "File", None))
        self.mniEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.mniFileExportQA.setText(_translate("MainWindow", "Export as QA Document", None))
        self.mniFileExportReport.setText(_translate("MainWindow", "Export as Report Document", None))
        self.mniFileClose.setText(_translate("MainWindow", "Close", None))
        self.mniEditCopy.setText(_translate("MainWindow", "Copy", None))
        self.mniEditDelete.setText(_translate("MainWindow", "Delete", None))
        self.mniEditExportWord.setText(_translate("MainWindow", "Export to MS Word", None))
        self.mniEditComment.setText(_translate("MainWindow", "Edit Comment...", None))
        self.mniEditExportSST.setText(_translate("MainWindow", "Export to File...", None))
        self.mniEditRestoreView.setText(_translate("MainWindow", "Restore View", None))

