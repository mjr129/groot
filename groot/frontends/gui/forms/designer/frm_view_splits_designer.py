# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/martinrusilowicz/work/apps/groot/groot/frontends/gui/forms/designer/frm_view_splits_designer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1171, 822)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalFrame = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.GRP_WORKFLOW = QtWidgets.QGroupBox(self.horizontalFrame)
        self.GRP_WORKFLOW.setObjectName("GRP_WORKFLOW")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.GRP_WORKFLOW)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BTN_WORKFLOW_ = QtWidgets.QToolButton(self.GRP_WORKFLOW)
        self.BTN_WORKFLOW_.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_WORKFLOW_.setMaximumSize(QtCore.QSize(64, 64))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/intermake/dropdown.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_WORKFLOW_.setIcon(icon)
        self.BTN_WORKFLOW_.setIconSize(QtCore.QSize(32, 32))
        self.BTN_WORKFLOW_.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_WORKFLOW_.setObjectName("BTN_WORKFLOW_")
        self.horizontalLayout_2.addWidget(self.BTN_WORKFLOW_)
        self.line_3 = QtWidgets.QFrame(self.GRP_WORKFLOW)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.BTN_CREATE_ = QtWidgets.QToolButton(self.GRP_WORKFLOW)
        self.BTN_CREATE_.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_CREATE_.setMaximumSize(QtCore.QSize(64, 64))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/groot/create.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_CREATE_.setIcon(icon1)
        self.BTN_CREATE_.setIconSize(QtCore.QSize(32, 32))
        self.BTN_CREATE_.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_CREATE_.setObjectName("BTN_CREATE_")
        self.horizontalLayout_2.addWidget(self.BTN_CREATE_)
        self.BTN_REMOVE_ = QtWidgets.QToolButton(self.GRP_WORKFLOW)
        self.BTN_REMOVE_.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_REMOVE_.setMaximumSize(QtCore.QSize(64, 64))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/groot/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_REMOVE_.setIcon(icon2)
        self.BTN_REMOVE_.setIconSize(QtCore.QSize(32, 32))
        self.BTN_REMOVE_.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_REMOVE_.setObjectName("BTN_REMOVE_")
        self.horizontalLayout_2.addWidget(self.BTN_REMOVE_)
        self.BTN_VIEW_ = QtWidgets.QToolButton(self.GRP_WORKFLOW)
        self.BTN_VIEW_.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_VIEW_.setMaximumSize(QtCore.QSize(64, 64))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/groot/view.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_VIEW_.setIcon(icon3)
        self.BTN_VIEW_.setIconSize(QtCore.QSize(32, 32))
        self.BTN_VIEW_.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_VIEW_.setObjectName("BTN_VIEW_")
        self.horizontalLayout_2.addWidget(self.BTN_VIEW_)
        self.horizontalLayout.addWidget(self.GRP_WORKFLOW)
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalFrame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BTN_CHANGE_SELECTION_ = QtWidgets.QToolButton(self.groupBox_2)
        self.BTN_CHANGE_SELECTION_.setMinimumSize(QtCore.QSize(192, 64))
        self.BTN_CHANGE_SELECTION_.setMaximumSize(QtCore.QSize(192, 64))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/groot/groot_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_CHANGE_SELECTION_.setIcon(icon4)
        self.BTN_CHANGE_SELECTION_.setIconSize(QtCore.QSize(32, 32))
        self.BTN_CHANGE_SELECTION_.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.BTN_CHANGE_SELECTION_.setObjectName("BTN_CHANGE_SELECTION_")
        self.horizontalLayout_3.addWidget(self.BTN_CHANGE_SELECTION_)
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.BTN_CLEAR_ = QtWidgets.QToolButton(self.groupBox_2)
        self.BTN_CLEAR_.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_CLEAR_.setMaximumSize(QtCore.QSize(64, 64))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/groot/empty.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_CLEAR_.setIcon(icon5)
        self.BTN_CLEAR_.setIconSize(QtCore.QSize(32, 32))
        self.BTN_CLEAR_.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_CLEAR_.setObjectName("BTN_CLEAR_")
        self.horizontalLayout_3.addWidget(self.BTN_CLEAR_)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.LBL_ADDFILTER = QtWidgets.QLabel(self.groupBox_2)
        self.LBL_ADDFILTER.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_ADDFILTER.setObjectName("LBL_ADDFILTER")
        self.verticalLayout.addWidget(self.LBL_ADDFILTER)
        self.TXT_ADDFILTER = QtWidgets.QLineEdit(self.groupBox_2)
        self.TXT_ADDFILTER.setObjectName("TXT_ADDFILTER")
        self.verticalLayout.addWidget(self.TXT_ADDFILTER)
        spacerItem1 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.BTN_REFRESH = QtWidgets.QToolButton(self.groupBox_2)
        self.BTN_REFRESH.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_REFRESH.setMaximumSize(QtCore.QSize(64, 64))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/groot/refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_REFRESH.setIcon(icon6)
        self.BTN_REFRESH.setIconSize(QtCore.QSize(32, 32))
        self.BTN_REFRESH.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_REFRESH.setObjectName("BTN_REFRESH")
        self.horizontalLayout_3.addWidget(self.BTN_REFRESH)
        self.horizontalLayout.addWidget(self.groupBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.horizontalFrame)
        self.LBL_TITLE = QtWidgets.QLabel(Dialog)
        self.LBL_TITLE.setObjectName("LBL_TITLE")
        self.verticalLayout_2.addWidget(self.LBL_TITLE)
        self.LST_MAIN = QtWidgets.QTreeWidget(Dialog)
        self.LST_MAIN.setAlternatingRowColors(True)
        self.LST_MAIN.setRootIsDecorated(False)
        self.LST_MAIN.setItemsExpandable(False)
        self.LST_MAIN.setExpandsOnDoubleClick(False)
        self.LST_MAIN.setObjectName("LST_MAIN")
        self.LST_MAIN.headerItem().setText(0, "1")
        self.verticalLayout_2.addWidget(self.LST_MAIN)
        self.LBL_SELECTION_INFO = QtWidgets.QLabel(Dialog)
        self.LBL_SELECTION_INFO.setFrameShape(QtWidgets.QFrame.Box)
        self.LBL_SELECTION_INFO.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LBL_SELECTION_INFO.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_SELECTION_INFO.setObjectName("LBL_SELECTION_INFO")
        self.verticalLayout_2.addWidget(self.LBL_SELECTION_INFO)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.GRP_WORKFLOW.setTitle(_translate("Dialog", "Workflow"))
        self.BTN_WORKFLOW_.setText(_translate("Dialog", "Workflow"))
        self.BTN_CREATE_.setText(_translate("Dialog", "Create"))
        self.BTN_REMOVE_.setText(_translate("Dialog", "Remove"))
        self.BTN_VIEW_.setText(_translate("Dialog", "View"))
        self.groupBox_2.setTitle(_translate("Dialog", "Viewer"))
        self.BTN_CHANGE_SELECTION_.setToolTip(_translate("Dialog", "<html><head/><body><p>Switch to edge edit mode.</p></body></html>"))
        self.BTN_CHANGE_SELECTION_.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_CHANGE_SELECTION_.setText(_translate("Dialog", "Select"))
        self.BTN_CLEAR_.setToolTip(_translate("Dialog", "<html><head/><body><p>Switch to edge edit mode.</p></body></html>"))
        self.BTN_CLEAR_.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_CLEAR_.setText(_translate("Dialog", "Clear"))
        self.LBL_ADDFILTER.setText(_translate("Dialog", "Additional filter"))
        self.BTN_REFRESH.setToolTip(_translate("Dialog", "<html><head/><body><p>Switch to edge edit mode.</p></body></html>"))
        self.BTN_REFRESH.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_REFRESH.setText(_translate("Dialog", "Refresh"))
        self.LBL_TITLE.setText(_translate("Dialog", "Text goes here"))
        self.LBL_TITLE.setProperty("style", _translate("Dialog", "title"))
        self.LBL_SELECTION_INFO.setToolTip(_translate("Dialog", "Baum-Ragan representation"))
        self.LBL_SELECTION_INFO.setText(_translate("Dialog", "Text goes here"))


