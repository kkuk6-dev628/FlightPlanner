# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PinsDep.ui'
#
# Created: Tue Apr 07 09:19:23 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from FlightPlanner.Panels.TrackRadialBoxPanel import TrackRadialBoxPanel
from FlightPlanner.Panels.ComboBoxPanel import ComboBoxPanel
from FlightPlanner.Panels.AngleGradientBoxPanel import AngleGradientBoxPanel, AngleGradientSlopeUnits, AngleGradientSlope
from FlightPlanner.Panels.AltitudeBoxPanel import AltitudeBoxPanel, Altitude
from FlightPlanner.Panels.DistanceBoxPanel import Distance, DistanceBoxPanel, DistanceUnits

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class ui_PinSVisualSegmentDepDlg(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(548, 584)
        self.verticalLayout_8 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.tabControls = QtGui.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setWeight(50)
        font.setBold(False)
        self.tabControls.setFont(font)
        self.tabControls.setAutoFillBackground(False)
        self.tabControls.setStyleSheet(_fromUtf8(""))
        self.tabControls.setObjectName(_fromUtf8("tabControls"))
        self.tab_General = QtGui.QWidget(Dialog)
        self.tab_General.setObjectName(_fromUtf8("tab_General"))
        self.horizontalLayout_29 = QtGui.QHBoxLayout(self.tab_General)
        self.horizontalLayout_29.setMargin(3)
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.frame_2 = QtGui.QFrame(self.tab_General)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_20 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_20.setObjectName(_fromUtf8("groupBox_20"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_20)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))

        self.cmbSegmentType = ComboBoxPanel(self.groupBox_20)
        self.cmbSegmentType.Caption = "Visual Segment Type"
        self.cmbSegmentType.LabelWidth = 250
        self.verticalLayout_5.addWidget(self.cmbSegmentType)

        self.cmbDepartureType = ComboBoxPanel(self.groupBox_20)
        self.cmbDepartureType.Caption = "Departure Type"
        self.cmbDepartureType.LabelWidth = 250
        self.verticalLayout_5.addWidget(self.cmbDepartureType)

        self.txtVSDG = AngleGradientBoxPanel(self.groupBox_20)
        self.txtVSDG.CaptionUnits = AngleGradientSlopeUnits.Percent
        self.txtVSDG.Caption = "Visual Segment Design Gradient [VSDG]"
        self.txtVSDG.LabelWidth = 250
        self.txtVSDG.Value = AngleGradientSlope(5, AngleGradientSlopeUnits.Percent)
        self.verticalLayout_5.addWidget(self.txtVSDG)

        self.txtTakeOffSurfaceTrack = TrackRadialBoxPanel(self.groupBox_20)
        self.txtTakeOffSurfaceTrack.Caption = "Out-bound Take-off Surface Track"
        self.txtTakeOffSurfaceTrack.LabelWidth = 250
        self.verticalLayout_5.addWidget(self.txtTakeOffSurfaceTrack)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/coordinate_capture.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.txtMOC = AltitudeBoxPanel(self.groupBox_20)
        self.txtMOC.CaptionUnits = "m"
        self.txtMOC.Caption = "MOC"
        self.txtMOC.Value = Altitude(30)
        self.txtMOC.LabelWidth = 250
        self.verticalLayout_5.addWidget(self.txtMOC)

        self.frame_Limitation = QtGui.QFrame(self.groupBox_20)
        self.frame_Limitation.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_Limitation.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Limitation.setObjectName(_fromUtf8("frame_Limitation"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_Limitation)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.chbLeftTurnProhibited = QtGui.QCheckBox(self.frame_Limitation)
        self.chbLeftTurnProhibited.setMinimumSize(QtCore.QSize(230, 0))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.chbLeftTurnProhibited.setFont(font)
        self.chbLeftTurnProhibited.setObjectName(_fromUtf8("chbLeftTurnProhibited"))
        self.horizontalLayout_2.addWidget(self.chbLeftTurnProhibited)
        self.chbRightTurnProhibited = QtGui.QCheckBox(self.frame_Limitation)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.chbRightTurnProhibited.setFont(font)
        self.chbRightTurnProhibited.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chbRightTurnProhibited.setObjectName(_fromUtf8("chbRightTurnProhibited"))
        self.horizontalLayout_2.addWidget(self.chbRightTurnProhibited)
        self.verticalLayout_5.addWidget(self.frame_Limitation)
        self.grbIDF = QtGui.QGroupBox(self.groupBox_20)
        self.grbIDF.setObjectName(_fromUtf8("grbIDF"))
        self.verticalLayout_IDF = QtGui.QVBoxLayout(self.grbIDF)
        self.verticalLayout_IDF.setObjectName(_fromUtf8("verticalLayout_IDF"))

        self.txtTrackFrom = TrackRadialBoxPanel(self.grbIDF)
        self.txtTrackFrom.Caption = "Track From"
        self.verticalLayout_IDF.addWidget(self.txtTrackFrom)

        self.verticalLayout_5.addWidget(self.grbIDF)

        self.grbHRP = QtGui.QGroupBox(self.groupBox_20)
        self.grbHRP.setObjectName(_fromUtf8("grbHRP"))
        self.verticalLayout_HRP = QtGui.QVBoxLayout(self.grbHRP)
        self.verticalLayout_HRP.setObjectName(_fromUtf8("verticalLayout_HRP"))

        self.txtHSAL = DistanceBoxPanel(self.grbHRP, DistanceUnits.M)
        self.txtHSAL.Caption = "Safety Area Length"
        self.txtHSAL.Value = Distance(30)
        self.txtHSAL.LabelWidth = 240
        self.verticalLayout_HRP.addWidget(self.txtHSAL)

        self.txtHSAW = DistanceBoxPanel(self.grbHRP, DistanceUnits.M)
        self.txtHSAW.Caption = "Safety Area Width"
        self.txtHSAW.Value = Distance(30)
        self.txtHSAW.LabelWidth = 240
        self.verticalLayout_HRP.addWidget(self.txtHSAW)

        self.verticalLayout_5.addWidget(self.grbHRP)

        self.cmbConstructionType = ComboBoxPanel(self.groupBox_20)
        self.cmbConstructionType.Caption = "Construction Type"
        self.cmbConstructionType.LabelWidth = 250
        self.verticalLayout_5.addWidget(self.cmbConstructionType)

        self.verticalLayout_2.addWidget(self.groupBox_20)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_29.addWidget(self.frame_2)
        self.frame_38 = QtGui.QFrame(self.tab_General)
        self.frame_38.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_38.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_38.setObjectName(_fromUtf8("frame_38"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.frame_38)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.btnOpenData = QtGui.QPushButton(self.frame_38)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.btnOpenData.setFont(font)
        self.btnOpenData.setObjectName(_fromUtf8("btnOpenData"))
        self.verticalLayout_7.addWidget(self.btnOpenData)
        self.btnSaveData = QtGui.QPushButton(self.frame_38)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.btnSaveData.setFont(font)
        self.btnSaveData.setObjectName(_fromUtf8("btnSaveData"))
        self.verticalLayout_7.addWidget(self.btnSaveData)
        self.btnConstruct = QtGui.QPushButton(self.frame_38)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.btnConstruct.setFont(font)
        self.btnConstruct.setObjectName(_fromUtf8("btnConstruct"))
        self.verticalLayout_7.addWidget(self.btnConstruct)
        self.btnEvaluate = QtGui.QPushButton(self.frame_38)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.btnEvaluate.setFont(font)
        self.btnEvaluate.setObjectName(_fromUtf8("btnEvaluate"))
        self.verticalLayout_7.addWidget(self.btnEvaluate)
        self.btnUpdateQA = QtGui.QPushButton(self.frame_38)
        self.btnUpdateQA.setEnabled(False)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.btnUpdateQA.setFont(font)
        self.btnUpdateQA.setObjectName(_fromUtf8("btnUpdateQA"))
        self.verticalLayout_7.addWidget(self.btnUpdateQA)
        
        self.btnClose = QtGui.QPushButton(self.frame_38)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.verticalLayout_7.addWidget(self.btnClose)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_29.addWidget(self.frame_38)
        self.tabControls.addTab(self.tab_General, _fromUtf8(""))
        self.tab_Results = QtGui.QWidget(Dialog)
        self.tab_Results.setObjectName(_fromUtf8("tab_Results"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_Results)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setMargin(3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame_3 = QtGui.QFrame(self.tab_Results)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.frame_117 = QtGui.QFrame(self.frame_3)
        self.frame_117.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_117.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_117.setObjectName(_fromUtf8("frame_117"))
        self.horizontalLayout_105 = QtGui.QHBoxLayout(self.frame_117)
        self.horizontalLayout_105.setSpacing(0)
        self.horizontalLayout_105.setMargin(0)
        self.horizontalLayout_105.setObjectName(_fromUtf8("horizontalLayout_105"))
        self.label_126 = QtGui.QLabel(self.frame_117)
        self.label_126.setMinimumSize(QtCore.QSize(290, 0))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_126.setFont(font)
        self.label_126.setObjectName(_fromUtf8("label_126"))
        self.horizontalLayout_105.addWidget(self.label_126)
        self.cmbSurface = QtGui.QComboBox(self.frame_117)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbSurface.sizePolicy().hasHeightForWidth())
        self.cmbSurface.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setWeight(50)
        font.setBold(False)
        self.cmbSurface.setFont(font)
        self.cmbSurface.setObjectName(_fromUtf8("cmbSurface"))
        self.horizontalLayout_105.addWidget(self.cmbSurface)
        self.verticalLayout_6.addWidget(self.frame_117)
        self.tblObstacles = QtGui.QTableView(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tblObstacles.setFont(font)
        self.tblObstacles.setObjectName(_fromUtf8("tblObstacles"))
        self.verticalLayout_6.addWidget(self.tblObstacles)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame = QtGui.QFrame(self.tab_Results)
#         self.frame.setMinimumSize(QtCore.QSize(105, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.btnLocate = QtGui.QPushButton(self.frame)
        self.btnLocate.setEnabled(False)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.btnLocate.setFont(font)
        self.btnLocate.setObjectName(_fromUtf8("btnLocate"))
        self.verticalLayout_4.addWidget(self.btnLocate)
        self.btnUpdateQA_2 = QtGui.QPushButton(self.frame)
        self.btnUpdateQA_2.setEnabled(False)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.btnUpdateQA_2.setFont(font)
        self.btnUpdateQA_2.setObjectName(_fromUtf8("btnUpdateQA_2"))
        self.verticalLayout_4.addWidget(self.btnUpdateQA_2)
        self.btnExportResult = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.btnExportResult.setFont(font)
        self.btnExportResult.setObjectName(_fromUtf8("btnExportResult"))
        self.verticalLayout_4.addWidget(self.btnExportResult)
        self.btnClose_2 = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.btnClose_2.setFont(font)
        self.btnClose_2.setObjectName(_fromUtf8("btnClose_2"))
        self.verticalLayout_4.addWidget(self.btnClose_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.frame)
        self.tabControls.addTab(self.tab_Results, _fromUtf8(""))
        self.verticalLayout_8.addWidget(self.tabControls)

        self.retranslateUi(Dialog)
        self.tabControls.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/btnImage/openData.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpenData.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/btnImage/saveData.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveData.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/btnImage/construct.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConstruct.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/btnImage/evaluate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEvaluate.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/btnImage/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/btnImage/locate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLocate.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/btnImage/pdtCheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btnPDTCheck.setIcon(icon)
        icon = QtGui.QIcon()        
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/btnImage/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose_2.setIcon(icon)
        icon = QtGui.QIcon()        
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/btnImage/exportResult.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExportResult.setIcon(icon)
        
        self.btnClose.setToolTip(_fromUtf8("Close"))
        self.btnClose_2.setToolTip(_fromUtf8("Close"))
        self.btnConstruct.setToolTip(_fromUtf8("Construct"))
        self.btnEvaluate.setToolTip(_fromUtf8("Evaluate"))
        self.btnLocate.setToolTip(_fromUtf8("Locate"))
        self.btnExportResult.setToolTip(_fromUtf8("Export Result"))
        self.btnOpenData.setToolTip(_fromUtf8("Open Data"))
        self.btnSaveData.setToolTip(_fromUtf8("Save Data"))
#         self.btnMarkSoc.setToolTip(_fromUtf8("Mark SOC"))

        self.btnClose.setIconSize(QtCore.QSize(32,32))
        self.btnClose_2.setIconSize(QtCore.QSize(32,32))
        self.btnConstruct.setIconSize(QtCore.QSize(32,32))
        self.btnEvaluate.setIconSize(QtCore.QSize(32,32))
        self.btnLocate.setIconSize(QtCore.QSize(32,32))
        self.btnExportResult.setIconSize(QtCore.QSize(32,32))
        self.btnOpenData.setIconSize(QtCore.QSize(32,32))
        self.btnSaveData.setIconSize(QtCore.QSize(32,32))
        # self.btnPDTCheck.setIconSize(QtCore.QSize(32,32))

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "PinS Visual Segment for Departures", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_20.setTitle(QtGui.QApplication.translate("Dialog", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.chbLeftTurnProhibited.setText(QtGui.QApplication.translate("Dialog", "Left turn prohibited", None, QtGui.QApplication.UnicodeUTF8))
        self.chbRightTurnProhibited.setText(QtGui.QApplication.translate("Dialog", "Right turn prohibited", None, QtGui.QApplication.UnicodeUTF8))
        self.grbIDF.setTitle(QtGui.QApplication.translate("Dialog", "Initial Departure Fix (IDF)", None, QtGui.QApplication.UnicodeUTF8))
        self.grbHRP.setTitle(QtGui.QApplication.translate("Dialog", "Heliport", None, QtGui.QApplication.UnicodeUTF8))
        self.tabControls.setTabText(self.tabControls.indexOf(self.tab_General), QtGui.QApplication.translate("Dialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.label_126.setText(QtGui.QApplication.translate("Dialog", "Surface:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabControls.setTabText(self.tabControls.indexOf(self.tab_Results), QtGui.QApplication.translate("Dialog", "Results/Checked Obstacles", None, QtGui.QApplication.UnicodeUTF8))

