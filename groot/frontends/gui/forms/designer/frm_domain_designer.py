# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/martinrusilowicz/work/apps/groot/groot/frontends/gui/forms/designer/frm_domain_designer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 311)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LBL_DATA_WARNING = QtWidgets.QLabel(Dialog)
        self.LBL_DATA_WARNING.setObjectName("LBL_DATA_WARNING")
        self.verticalLayout.addWidget(self.LBL_DATA_WARNING)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setSpacing(8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LBL_MAIN = QtWidgets.QLabel(self.frame)
        self.LBL_MAIN.setObjectName("LBL_MAIN")
        self.gridLayout_2.addWidget(self.LBL_MAIN, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.RAD_EXISTING = QtWidgets.QRadioButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RAD_EXISTING.sizePolicy().hasHeightForWidth())
        self.RAD_EXISTING.setSizePolicy(sizePolicy)
        self.RAD_EXISTING.setObjectName("RAD_EXISTING")
        self.verticalLayout.addWidget(self.RAD_EXISTING)
        self.RAD_NO = QtWidgets.QRadioButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RAD_NO.sizePolicy().hasHeightForWidth())
        self.RAD_NO.setSizePolicy(sizePolicy)
        self.RAD_NO.setObjectName("RAD_NO")
        self.verticalLayout.addWidget(self.RAD_NO)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.RAD_AUTO = QtWidgets.QRadioButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RAD_AUTO.sizePolicy().hasHeightForWidth())
        self.RAD_AUTO.setSizePolicy(sizePolicy)
        self.RAD_AUTO.setObjectName("RAD_AUTO")
        self.horizontalLayout_3.addWidget(self.RAD_AUTO)
        self.LBL_COMPONENT_WARNING = QtWidgets.QLabel(Dialog)
        self.LBL_COMPONENT_WARNING.setObjectName("LBL_COMPONENT_WARNING")
        self.horizontalLayout_3.addWidget(self.LBL_COMPONENT_WARNING)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RAD_SIZE = QtWidgets.QRadioButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RAD_SIZE.sizePolicy().hasHeightForWidth())
        self.RAD_SIZE.setSizePolicy(sizePolicy)
        self.RAD_SIZE.setObjectName("RAD_SIZE")
        self.horizontalLayout_2.addWidget(self.RAD_SIZE)
        self.WID_SIZE = QtWidgets.QWidget(Dialog)
        self.WID_SIZE.setObjectName("WID_SIZE")
        self.H = QtWidgets.QHBoxLayout(self.WID_SIZE)
        self.H.setContentsMargins(0, 0, 0, 0)
        self.H.setSpacing(8)
        self.H.setObjectName("H")
        self.label_4 = QtWidgets.QLabel(self.WID_SIZE)
        self.label_4.setObjectName("label_4")
        self.H.addWidget(self.label_4)
        self.SPN_SIZE = QtWidgets.QSpinBox(self.WID_SIZE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SPN_SIZE.sizePolicy().hasHeightForWidth())
        self.SPN_SIZE.setSizePolicy(sizePolicy)
        self.SPN_SIZE.setMinimumSize(QtCore.QSize(64, 0))
        self.SPN_SIZE.setMaximumSize(QtCore.QSize(64, 16777215))
        self.SPN_SIZE.setObjectName("SPN_SIZE")
        self.H.addWidget(self.SPN_SIZE)
        self.label_2 = QtWidgets.QLabel(self.WID_SIZE)
        self.label_2.setObjectName("label_2")
        self.H.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.WID_SIZE)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.RAD_NUM = QtWidgets.QRadioButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RAD_NUM.sizePolicy().hasHeightForWidth())
        self.RAD_NUM.setSizePolicy(sizePolicy)
        self.RAD_NUM.setObjectName("RAD_NUM")
        self.horizontalLayout_5.addWidget(self.RAD_NUM)
        self.WID_NUM = QtWidgets.QWidget(Dialog)
        self.WID_NUM.setObjectName("WID_NUM")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.WID_NUM)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.WID_NUM)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.SPN_NUM = QtWidgets.QSpinBox(self.WID_NUM)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SPN_NUM.sizePolicy().hasHeightForWidth())
        self.SPN_NUM.setSizePolicy(sizePolicy)
        self.SPN_NUM.setMinimumSize(QtCore.QSize(64, 0))
        self.SPN_NUM.setMaximumSize(QtCore.QSize(64, 16777215))
        self.SPN_NUM.setObjectName("SPN_NUM")
        self.horizontalLayout_4.addWidget(self.SPN_NUM)
        self.label_3 = QtWidgets.QLabel(self.WID_NUM)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_5.addWidget(self.WID_NUM)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.BTN_OK = QtWidgets.QPushButton(Dialog)
        self.BTN_OK.setObjectName("BTN_OK")
        self.horizontalLayout.addWidget(self.BTN_OK)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LBL_DATA_WARNING.setText(_translate("Dialog", "<html><head/><body><p>Requires sequences. <a href=\"action:show_load_model\">Load data</a> first.</p></body></html>"))
        self.LBL_DATA_WARNING.setProperty("style", _translate("Dialog", "warning"))
        self.LBL_MAIN.setText(_translate("Dialog", "You currently have no domains defined."))
        self.RAD_EXISTING.setText(_translate("Dialog", "Keep existing domains"))
        self.RAD_NO.setText(_translate("Dialog", "No domains"))
        self.RAD_AUTO.setText(_translate("Dialog", "Automated domain detection"))
        self.LBL_COMPONENT_WARNING.setText(_translate("Dialog", "<html><head/><body><p>Requires components. <a href=\"action:create_components\">Create components</a> first.</p></body></html>"))
        self.LBL_COMPONENT_WARNING.setProperty("style", _translate("Dialog", "warning"))
        self.RAD_SIZE.setText(_translate("Dialog", "Equally sized domains"))
        self.label_4.setText(_translate("Dialog", "- each with"))
        self.label_2.setText(_translate("Dialog", "sites"))
        self.RAD_NUM.setText(_translate("Dialog", "Equal number of domains"))
        self.label_5.setText(_translate("Dialog", "- using"))
        self.label_3.setText(_translate("Dialog", "domains"))
        self.BTN_OK.setText(_translate("Dialog", "Generate domains"))

