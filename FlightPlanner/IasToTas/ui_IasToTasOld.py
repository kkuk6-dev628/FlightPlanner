# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_IasToTas.ui'
#
# Created: Tue Nov 10 16:27:45 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_IasToTas(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(378, 488)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.grbParameters = QtGui.QGroupBox(Form)
        self.grbParameters.setObjectName(_fromUtf8("grbParameters"))
        self.vLayout_grbParameters = QtGui.QVBoxLayout(self.grbParameters)
        self.vLayout_grbParameters.setObjectName(_fromUtf8("vLayout_grbParameters"))
        self.cmbType = QtGui.QComboBox(self.grbParameters)
        self.cmbType.setObjectName(_fromUtf8("cmbType"))
        self.vLayout_grbParameters.addWidget(self.cmbType)
        self.frame_IAS = QtGui.QFrame(self.grbParameters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_IAS.sizePolicy().hasHeightForWidth())
        self.frame_IAS.setSizePolicy(sizePolicy)
        self.frame_IAS.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_IAS.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_IAS.setObjectName(_fromUtf8("frame_IAS"))
        self.hLayoutIAS = QtGui.QHBoxLayout(self.frame_IAS)
        self.hLayoutIAS.setSpacing(0)
        self.hLayoutIAS.setMargin(0)
        self.hLayoutIAS.setObjectName(_fromUtf8("hLayoutIAS"))
        self.label_5 = QtGui.QLabel(self.frame_IAS)
        self.label_5.setMinimumSize(QtCore.QSize(180, 0))
        self.label_5.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.hLayoutIAS.addWidget(self.label_5)
        self.txtIAS = QtGui.QLineEdit(self.frame_IAS)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtIAS.sizePolicy().hasHeightForWidth())
        self.txtIAS.setSizePolicy(sizePolicy)
        self.txtIAS.setMinimumSize(QtCore.QSize(105, 0))
        self.txtIAS.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtIAS.setFont(font)
        self.txtIAS.setObjectName(_fromUtf8("txtIAS"))
        self.hLayoutIAS.addWidget(self.txtIAS)
        self.vLayout_grbParameters.addWidget(self.frame_IAS)
        self.frame_Altitude = QtGui.QFrame(self.grbParameters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_Altitude.sizePolicy().hasHeightForWidth())
        self.frame_Altitude.setSizePolicy(sizePolicy)
        self.frame_Altitude.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_Altitude.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Altitude.setObjectName(_fromUtf8("frame_Altitude"))
        self.hLayoutAltitude = QtGui.QHBoxLayout(self.frame_Altitude)
        self.hLayoutAltitude.setSpacing(0)
        self.hLayoutAltitude.setMargin(0)
        self.hLayoutAltitude.setObjectName(_fromUtf8("hLayoutAltitude"))
        self.label_6 = QtGui.QLabel(self.frame_Altitude)
        self.label_6.setMinimumSize(QtCore.QSize(180, 0))
        self.label_6.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.hLayoutAltitude.addWidget(self.label_6)
        self.txtAltitude = QtGui.QLineEdit(self.frame_Altitude)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtAltitude.sizePolicy().hasHeightForWidth())
        self.txtAltitude.setSizePolicy(sizePolicy)
        self.txtAltitude.setMinimumSize(QtCore.QSize(105, 0))
        self.txtAltitude.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtAltitude.setFont(font)
        self.txtAltitude.setObjectName(_fromUtf8("txtAltitude"))
        self.hLayoutAltitude.addWidget(self.txtAltitude)
        self.vLayout_grbParameters.addWidget(self.frame_Altitude)
        self.frame_ISA = QtGui.QFrame(self.grbParameters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_ISA.sizePolicy().hasHeightForWidth())
        self.frame_ISA.setSizePolicy(sizePolicy)
        self.frame_ISA.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_ISA.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_ISA.setObjectName(_fromUtf8("frame_ISA"))
        self.hLayoutISA = QtGui.QHBoxLayout(self.frame_ISA)
        self.hLayoutISA.setSpacing(0)
        self.hLayoutISA.setMargin(0)
        self.hLayoutISA.setObjectName(_fromUtf8("hLayoutISA"))
        self.label_7 = QtGui.QLabel(self.frame_ISA)
        self.label_7.setMinimumSize(QtCore.QSize(180, 0))
        self.label_7.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.hLayoutISA.addWidget(self.label_7)
        self.txtISA = QtGui.QLineEdit(self.frame_ISA)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtISA.sizePolicy().hasHeightForWidth())
        self.txtISA.setSizePolicy(sizePolicy)
        self.txtISA.setMinimumSize(QtCore.QSize(105, 0))
        self.txtISA.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtISA.setFont(font)
        self.txtISA.setObjectName(_fromUtf8("txtISA"))
        self.hLayoutISA.addWidget(self.txtISA)
        self.vLayout_grbParameters.addWidget(self.frame_ISA)
        self.gbNonStandard = QtGui.QGroupBox(self.grbParameters)
        self.gbNonStandard.setObjectName(_fromUtf8("gbNonStandard"))
        self.vLayoutNonStandard = QtGui.QVBoxLayout(self.gbNonStandard)
        self.vLayoutNonStandard.setObjectName(_fromUtf8("vLayoutNonStandard"))
        self.frame_RDH_2 = QtGui.QFrame(self.gbNonStandard)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_RDH_2.sizePolicy().hasHeightForWidth())
        self.frame_RDH_2.setSizePolicy(sizePolicy)
        self.frame_RDH_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_RDH_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_RDH_2.setObjectName(_fromUtf8("frame_RDH_2"))
        self.hLayoutRDH_2 = QtGui.QHBoxLayout(self.frame_RDH_2)
        self.hLayoutRDH_2.setSpacing(0)
        self.hLayoutRDH_2.setMargin(0)
        self.hLayoutRDH_2.setObjectName(_fromUtf8("hLayoutRDH_2"))
        self.label_9 = QtGui.QLabel(self.frame_RDH_2)
        self.label_9.setMinimumSize(QtCore.QSize(180, 0))
        self.label_9.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.hLayoutRDH_2.addWidget(self.label_9)
        self.txtTime = QtGui.QLineEdit(self.frame_RDH_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtTime.sizePolicy().hasHeightForWidth())
        self.txtTime.setSizePolicy(sizePolicy)
        self.txtTime.setMinimumSize(QtCore.QSize(105, 0))
        self.txtTime.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtTime.setFont(font)
        self.txtTime.setObjectName(_fromUtf8("txtTime"))
        self.hLayoutRDH_2.addWidget(self.txtTime)
        self.vLayoutNonStandard.addWidget(self.frame_RDH_2)
        self.vLayout_grbParameters.addWidget(self.gbNonStandard)
        self.verticalLayout.addWidget(self.grbParameters)
        self.gbResults = QtGui.QGroupBox(Form)
        self.gbResults.setObjectName(_fromUtf8("gbResults"))
        self.vLayoutResults = QtGui.QVBoxLayout(self.gbResults)
        self.vLayoutResults.setObjectName(_fromUtf8("vLayoutResults"))
        self.frame_TAS = QtGui.QFrame(self.gbResults)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_TAS.sizePolicy().hasHeightForWidth())
        self.frame_TAS.setSizePolicy(sizePolicy)
        self.frame_TAS.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_TAS.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_TAS.setObjectName(_fromUtf8("frame_TAS"))
        self.hLayoutRDH_3 = QtGui.QHBoxLayout(self.frame_TAS)
        self.hLayoutRDH_3.setSpacing(0)
        self.hLayoutRDH_3.setMargin(0)
        self.hLayoutRDH_3.setObjectName(_fromUtf8("hLayoutRDH_3"))
        self.label_10 = QtGui.QLabel(self.frame_TAS)
        self.label_10.setMinimumSize(QtCore.QSize(180, 0))
        self.label_10.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.hLayoutRDH_3.addWidget(self.label_10)
        self.txtTAS = QtGui.QLineEdit(self.frame_TAS)
        self.txtTAS.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtTAS.sizePolicy().hasHeightForWidth())
        self.txtTAS.setSizePolicy(sizePolicy)
        self.txtTAS.setMinimumSize(QtCore.QSize(105, 0))
        self.txtTAS.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtTAS.setFont(font)
        self.txtTAS.setObjectName(_fromUtf8("txtTAS"))
        self.hLayoutRDH_3.addWidget(self.txtTAS)
        self.vLayoutResults.addWidget(self.frame_TAS)
        self.frame_EST = QtGui.QFrame(self.gbResults)
        self.frame_EST.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_EST.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_EST.setObjectName(_fromUtf8("frame_EST"))
        self.horizontalLayout_65 = QtGui.QHBoxLayout(self.frame_EST)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setMargin(0)
        self.horizontalLayout_65.setObjectName(_fromUtf8("horizontalLayout_65"))
        self.label_73 = QtGui.QLabel(self.frame_EST)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setMinimumSize(QtCore.QSize(180, 0))
        self.label_73.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_73.setFont(font)
        self.label_73.setObjectName(_fromUtf8("label_73"))
        self.horizontalLayout_65.addWidget(self.label_73)
        self.frame_APV_9 = QtGui.QFrame(self.frame_EST)
        self.frame_APV_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_APV_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_APV_9.setObjectName(_fromUtf8("frame_APV_9"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.frame_APV_9)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.txtEST = QtGui.QLineEdit(self.frame_APV_9)
        self.txtEST.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtEST.setFont(font)
        self.txtEST.setObjectName(_fromUtf8("txtEST"))
        self.horizontalLayout_13.addWidget(self.txtEST)
        self.btnEST = QtGui.QToolButton(self.frame_APV_9)
        self.btnEST.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/Airplane.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEST.setIcon(icon)
        self.btnEST.setObjectName(_fromUtf8("btnEST"))
        self.horizontalLayout_13.addWidget(self.btnEST)
        self.horizontalLayout_65.addWidget(self.frame_APV_9)
        self.vLayoutResults.addWidget(self.frame_EST)
        self.frame_REA = QtGui.QFrame(self.gbResults)
        self.frame_REA.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_REA.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_REA.setObjectName(_fromUtf8("frame_REA"))
        self.horizontalLayout_66 = QtGui.QHBoxLayout(self.frame_REA)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setMargin(0)
        self.horizontalLayout_66.setObjectName(_fromUtf8("horizontalLayout_66"))
        self.label_74 = QtGui.QLabel(self.frame_REA)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setMinimumSize(QtCore.QSize(180, 0))
        self.label_74.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_74.setFont(font)
        self.label_74.setObjectName(_fromUtf8("label_74"))
        self.horizontalLayout_66.addWidget(self.label_74)
        self.frame_APV_10 = QtGui.QFrame(self.frame_REA)
        self.frame_APV_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_APV_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_APV_10.setObjectName(_fromUtf8("frame_APV_10"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.frame_APV_10)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setMargin(0)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.txtREA = QtGui.QLineEdit(self.frame_APV_10)
        self.txtREA.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtREA.setFont(font)
        self.txtREA.setObjectName(_fromUtf8("txtREA"))
        self.horizontalLayout_14.addWidget(self.txtREA)
        self.btnREA = QtGui.QToolButton(self.frame_APV_10)
        self.btnREA.setText(_fromUtf8(""))
        self.btnREA.setIcon(icon)
        self.btnREA.setObjectName(_fromUtf8("btnREA"))
        self.horizontalLayout_14.addWidget(self.btnREA)
        self.horizontalLayout_66.addWidget(self.frame_APV_10)
        self.vLayoutResults.addWidget(self.frame_REA)
        self.frame_C = QtGui.QFrame(self.gbResults)
        self.frame_C.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_C.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_C.setObjectName(_fromUtf8("frame_C"))
        self.horizontalLayout_67 = QtGui.QHBoxLayout(self.frame_C)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setMargin(0)
        self.horizontalLayout_67.setObjectName(_fromUtf8("horizontalLayout_67"))
        self.label_75 = QtGui.QLabel(self.frame_C)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setMinimumSize(QtCore.QSize(180, 0))
        self.label_75.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_75.setFont(font)
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.horizontalLayout_67.addWidget(self.label_75)
        self.frame_APV_11 = QtGui.QFrame(self.frame_C)
        self.frame_APV_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_APV_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_APV_11.setObjectName(_fromUtf8("frame_APV_11"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.frame_APV_11)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setMargin(0)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.txtC = QtGui.QLineEdit(self.frame_APV_11)
        self.txtC.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtC.setFont(font)
        self.txtC.setObjectName(_fromUtf8("txtC"))
        self.horizontalLayout_15.addWidget(self.txtC)
        self.btnC = QtGui.QToolButton(self.frame_APV_11)
        self.btnC.setText(_fromUtf8(""))
        self.btnC.setIcon(icon)
        self.btnC.setObjectName(_fromUtf8("btnC"))
        self.horizontalLayout_15.addWidget(self.btnC)
        self.horizontalLayout_67.addWidget(self.frame_APV_11)
        self.vLayoutResults.addWidget(self.frame_C)
        self.frame_X = QtGui.QFrame(self.gbResults)
        self.frame_X.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_X.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_X.setObjectName(_fromUtf8("frame_X"))
        self.horizontalLayout_69 = QtGui.QHBoxLayout(self.frame_X)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setMargin(0)
        self.horizontalLayout_69.setObjectName(_fromUtf8("horizontalLayout_69"))
        self.label_77 = QtGui.QLabel(self.frame_X)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        self.label_77.setMinimumSize(QtCore.QSize(180, 0))
        self.label_77.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_77.setFont(font)
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.horizontalLayout_69.addWidget(self.label_77)
        self.frame_APV_13 = QtGui.QFrame(self.frame_X)
        self.frame_APV_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_APV_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_APV_13.setObjectName(_fromUtf8("frame_APV_13"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.frame_APV_13)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setMargin(0)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.txtX = QtGui.QLineEdit(self.frame_APV_13)
        self.txtX.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtX.setFont(font)
        self.txtX.setObjectName(_fromUtf8("txtX"))
        self.horizontalLayout_17.addWidget(self.txtX)
        self.btnX = QtGui.QToolButton(self.frame_APV_13)
        self.btnX.setText(_fromUtf8(""))
        self.btnX.setIcon(icon)
        self.btnX.setObjectName(_fromUtf8("btnX"))
        self.horizontalLayout_17.addWidget(self.btnX)
        self.horizontalLayout_69.addWidget(self.frame_APV_13)
        self.vLayoutResults.addWidget(self.frame_X)
        self.frame_D = QtGui.QFrame(self.gbResults)
        self.frame_D.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_D.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_D.setObjectName(_fromUtf8("frame_D"))
        self.horizontalLayout_68 = QtGui.QHBoxLayout(self.frame_D)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setMargin(0)
        self.horizontalLayout_68.setObjectName(_fromUtf8("horizontalLayout_68"))
        self.label_76 = QtGui.QLabel(self.frame_D)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy)
        self.label_76.setMinimumSize(QtCore.QSize(180, 0))
        self.label_76.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_76.setFont(font)
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.horizontalLayout_68.addWidget(self.label_76)
        self.frame_APV_12 = QtGui.QFrame(self.frame_D)
        self.frame_APV_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_APV_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_APV_12.setObjectName(_fromUtf8("frame_APV_12"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.frame_APV_12)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setMargin(0)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.txtD = QtGui.QLineEdit(self.frame_APV_12)
        self.txtD.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtD.setFont(font)
        self.txtD.setObjectName(_fromUtf8("txtD"))
        self.horizontalLayout_16.addWidget(self.txtD)
        self.btnD = QtGui.QToolButton(self.frame_APV_12)
        self.btnD.setText(_fromUtf8(""))
        self.btnD.setIcon(icon)
        self.btnD.setObjectName(_fromUtf8("btnD"))
        self.horizontalLayout_16.addWidget(self.btnD)
        self.horizontalLayout_68.addWidget(self.frame_APV_12)
        self.vLayoutResults.addWidget(self.frame_D)
        self.gbNonStandardResult = QtGui.QGroupBox(self.gbResults)
        self.gbNonStandardResult.setObjectName(_fromUtf8("gbNonStandardResult"))
        self.vLayoutNonStandardResult = QtGui.QVBoxLayout(self.gbNonStandardResult)
        self.vLayoutNonStandardResult.setObjectName(_fromUtf8("vLayoutNonStandardResult"))
        self.frame_NonStandardResult = QtGui.QFrame(self.gbNonStandardResult)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_NonStandardResult.sizePolicy().hasHeightForWidth())
        self.frame_NonStandardResult.setSizePolicy(sizePolicy)
        self.frame_NonStandardResult.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_NonStandardResult.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_NonStandardResult.setObjectName(_fromUtf8("frame_NonStandardResult"))
        self.hLayoutRDH_4 = QtGui.QHBoxLayout(self.frame_NonStandardResult)
        self.hLayoutRDH_4.setSpacing(0)
        self.hLayoutRDH_4.setMargin(0)
        self.hLayoutRDH_4.setObjectName(_fromUtf8("hLayoutRDH_4"))
        self.label_11 = QtGui.QLabel(self.frame_NonStandardResult)
        self.label_11.setMinimumSize(QtCore.QSize(180, 0))
        self.label_11.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.hLayoutRDH_4.addWidget(self.label_11)
        self.txtNonStandardResult = QtGui.QLineEdit(self.frame_NonStandardResult)
        self.txtNonStandardResult.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtNonStandardResult.sizePolicy().hasHeightForWidth())
        self.txtNonStandardResult.setSizePolicy(sizePolicy)
        self.txtNonStandardResult.setMinimumSize(QtCore.QSize(105, 0))
        self.txtNonStandardResult.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtNonStandardResult.setFont(font)
        self.txtNonStandardResult.setObjectName(_fromUtf8("txtNonStandardResult"))
        self.hLayoutRDH_4.addWidget(self.txtNonStandardResult)
        self.vLayoutNonStandardResult.addWidget(self.frame_NonStandardResult)
        self.vLayoutResults.addWidget(self.gbNonStandardResult)
        self.verticalLayout.addWidget(self.gbResults)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.grbParameters.setTitle(_translate("Form", "Parameters", None))
        self.label_5.setText(_translate("Form", "IAS(kts):", None))
        self.txtIAS.setText(_translate("Form", "210", None))
        self.label_6.setText(_translate("Form", "Altitude(ft):", None))
        self.txtAltitude.setText(_translate("Form", "250", None))
        self.label_7.setText(_translate("Form", "ISA():", None))
        self.txtISA.setText(_translate("Form", "15", None))
        self.gbNonStandard.setTitle(_translate("Form", "Non-Standard", None))
        self.label_9.setText(_translate("Form", "Time(sec):", None))
        self.txtTime.setText(_translate("Form", "120", None))
        self.gbResults.setTitle(_translate("Form", "Results", None))
        self.label_10.setText(_translate("Form", "TAS:", None))
        self.txtTAS.setText(_translate("Form", "0", None))
        self.label_73.setText(_translate("Form", "EST:", None))
        self.txtEST.setText(_translate("Form", "0", None))
        self.label_74.setText(_translate("Form", "Pilot Reaction:", None))
        self.txtREA.setText(_translate("Form", "0", None))
        self.label_75.setText(_translate("Form", "c:", None))
        self.txtC.setText(_translate("Form", "0", None))
        self.label_77.setText(_translate("Form", "X(10kts / 15s):", None))
        self.txtX.setText(_translate("Form", "0", None))
        self.label_76.setText(_translate("Form", "d(10kts / 3s):", None))
        self.txtD.setText(_translate("Form", "0", None))
        self.gbNonStandardResult.setTitle(_translate("Form", "Non-Standard", None))
        self.label_11.setText(_translate("Form", "47.5kts / 120s:", None))
        self.txtNonStandardResult.setText(_translate("Form", "0", None))
