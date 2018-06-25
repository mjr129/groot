# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/martinrusilowicz/work/apps/groot/groot_gui/forms/designer/frm_view_splits_designer.ui'
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
        self.FRA_TOOLBAR = QtWidgets.QFrame(Dialog)
        self.FRA_TOOLBAR.setObjectName("FRA_TOOLBAR")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.FRA_TOOLBAR)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BTN_ADD_TO_FILTER = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        self.BTN_ADD_TO_FILTER.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_ADD_TO_FILTER.setMaximumSize(QtCore.QSize(64, 64))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/groot/shift_right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_ADD_TO_FILTER.setIcon(icon)
        self.BTN_ADD_TO_FILTER.setIconSize(QtCore.QSize(32, 32))
        self.BTN_ADD_TO_FILTER.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_ADD_TO_FILTER.setObjectName("BTN_ADD_TO_FILTER")
        self.horizontalLayout_3.addWidget(self.BTN_ADD_TO_FILTER)
        self.BTN_ADD_TEXT_TO_FILTER = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        self.BTN_ADD_TEXT_TO_FILTER.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_ADD_TEXT_TO_FILTER.setMaximumSize(QtCore.QSize(64, 64))
        self.BTN_ADD_TEXT_TO_FILTER.setIcon(icon)
        self.BTN_ADD_TEXT_TO_FILTER.setIconSize(QtCore.QSize(32, 32))
        self.BTN_ADD_TEXT_TO_FILTER.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_ADD_TEXT_TO_FILTER.setObjectName("BTN_ADD_TEXT_TO_FILTER")
        self.horizontalLayout_3.addWidget(self.BTN_ADD_TEXT_TO_FILTER)
        self.BTN_REMOVE_FROM_FILTER = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        self.BTN_REMOVE_FROM_FILTER.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_REMOVE_FROM_FILTER.setMaximumSize(QtCore.QSize(64, 64))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/groot/shift_left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_REMOVE_FROM_FILTER.setIcon(icon1)
        self.BTN_REMOVE_FROM_FILTER.setIconSize(QtCore.QSize(32, 32))
        self.BTN_REMOVE_FROM_FILTER.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_REMOVE_FROM_FILTER.setObjectName("BTN_REMOVE_FROM_FILTER")
        self.horizontalLayout_3.addWidget(self.BTN_REMOVE_FROM_FILTER)
        self.BTN_CLEAR_ = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        self.BTN_CLEAR_.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_CLEAR_.setMaximumSize(QtCore.QSize(64, 64))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/groot/expand_left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_CLEAR_.setIcon(icon2)
        self.BTN_CLEAR_.setIconSize(QtCore.QSize(32, 32))
        self.BTN_CLEAR_.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_CLEAR_.setObjectName("BTN_CLEAR_")
        self.horizontalLayout_3.addWidget(self.BTN_CLEAR_)
        self.LBL_FILTER = QtWidgets.QLabel(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBL_FILTER.sizePolicy().hasHeightForWidth())
        self.LBL_FILTER.setSizePolicy(sizePolicy)
        self.LBL_FILTER.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LBL_FILTER.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_FILTER.setObjectName("LBL_FILTER")
        self.horizontalLayout_3.addWidget(self.LBL_FILTER)
        self.BTN_VIEW_ELSEWHERE = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        self.BTN_VIEW_ELSEWHERE.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_VIEW_ELSEWHERE.setMaximumSize(QtCore.QSize(64, 64))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/groot/view.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_VIEW_ELSEWHERE.setIcon(icon3)
        self.BTN_VIEW_ELSEWHERE.setIconSize(QtCore.QSize(32, 32))
        self.BTN_VIEW_ELSEWHERE.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_VIEW_ELSEWHERE.setObjectName("BTN_VIEW_ELSEWHERE")
        self.horizontalLayout_3.addWidget(self.BTN_VIEW_ELSEWHERE)
        self.BTN_REFRESH = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        self.BTN_REFRESH.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_REFRESH.setMaximumSize(QtCore.QSize(64, 64))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/groot/refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_REFRESH.setIcon(icon4)
        self.BTN_REFRESH.setIconSize(QtCore.QSize(32, 32))
        self.BTN_REFRESH.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_REFRESH.setObjectName("BTN_REFRESH")
        self.horizontalLayout_3.addWidget(self.BTN_REFRESH)
        self.BTN_HELP = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        self.BTN_HELP.setMinimumSize(QtCore.QSize(64, 64))
        self.BTN_HELP.setMaximumSize(QtCore.QSize(64, 64))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/groot/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_HELP.setIcon(icon5)
        self.BTN_HELP.setIconSize(QtCore.QSize(32, 32))
        self.BTN_HELP.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_HELP.setObjectName("BTN_HELP")
        self.horizontalLayout_3.addWidget(self.BTN_HELP)
        self.verticalLayout_2.addWidget(self.FRA_TOOLBAR)
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
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 32))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1153, 30))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.LAY_BBAR = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.LAY_BBAR.setContentsMargins(0, 0, 0, 0)
        self.LAY_BBAR.setObjectName("LAY_BBAR")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.LAY_BBAR.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.BTN_ADD_TO_FILTER.setToolTip(_translate("Dialog", "<html><head/><body><p>Switch to edge edit mode.</p></body></html>"))
        self.BTN_ADD_TO_FILTER.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_ADD_TO_FILTER.setText(_translate("Dialog", "Add\n"
"to filter"))
        self.BTN_ADD_TEXT_TO_FILTER.setToolTip(_translate("Dialog", "<html><head/><body><p>Switch to edge edit mode.</p></body></html>"))
        self.BTN_ADD_TEXT_TO_FILTER.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_ADD_TEXT_TO_FILTER.setText(_translate("Dialog", "Add text\n"
"to filter"))
        self.BTN_REMOVE_FROM_FILTER.setToolTip(_translate("Dialog", "<html><head/><body><p>Switch to edge edit mode.</p></body></html>"))
        self.BTN_REMOVE_FROM_FILTER.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_REMOVE_FROM_FILTER.setText(_translate("Dialog", "Remove\n"
"from filter"))
        self.BTN_CLEAR_.setToolTip(_translate("Dialog", "<html><head/><body><p>Switch to edge edit mode.</p></body></html>"))
        self.BTN_CLEAR_.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_CLEAR_.setText(_translate("Dialog", "Clear\n"
"filter"))
        self.LBL_FILTER.setText(_translate("Dialog", "..."))
        self.BTN_VIEW_ELSEWHERE.setToolTip(_translate("Dialog", "<html><head/><body><p>Switch to edge edit mode.</p></body></html>"))
        self.BTN_VIEW_ELSEWHERE.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_VIEW_ELSEWHERE.setText(_translate("Dialog", "View"))
        self.BTN_REFRESH.setToolTip(_translate("Dialog", "<html><head/><body><p>Switch to edge edit mode.</p></body></html>"))
        self.BTN_REFRESH.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_REFRESH.setText(_translate("Dialog", "Refresh"))
        self.BTN_HELP.setToolTip(_translate("Dialog", "<html><head/><body><p>Switch to edge edit mode.</p></body></html>"))
        self.BTN_HELP.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_HELP.setText(_translate("Dialog", "Help"))
        self.LBL_TITLE.setText(_translate("Dialog", "Text goes here"))
        self.LBL_TITLE.setProperty("style", _translate("Dialog", "title"))
        self.label.setText(_translate("Dialog", "(placeholder)"))


