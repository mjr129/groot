# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/martinrusilowicz/work/apps/groot/groot/frontends/gui/forms/designer/frm_workflow_designer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 681)
        Dialog.setMinimumSize(QtCore.QSize(400, 600))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.FRA_PAUSED = QtWidgets.QFrame(Dialog)
        self.FRA_PAUSED.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRA_PAUSED.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRA_PAUSED.setObjectName("FRA_PAUSED")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.FRA_PAUSED)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LBL_PAUSED = QtWidgets.QLabel(self.FRA_PAUSED)
        self.LBL_PAUSED.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_PAUSED.setObjectName("LBL_PAUSED")
        self.verticalLayout.addWidget(self.LBL_PAUSED)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.BTN_CONTINUE = QtWidgets.QPushButton(self.FRA_PAUSED)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_CONTINUE.sizePolicy().hasHeightForWidth())
        self.BTN_CONTINUE.setSizePolicy(sizePolicy)
        self.BTN_CONTINUE.setObjectName("BTN_CONTINUE")
        self.horizontalLayout_2.addWidget(self.BTN_CONTINUE)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.LBL_NEXT = QtWidgets.QLabel(self.FRA_PAUSED)
        self.LBL_NEXT.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_NEXT.setObjectName("LBL_NEXT")
        self.verticalLayout.addWidget(self.LBL_NEXT)
        self.line = QtWidgets.QFrame(self.FRA_PAUSED)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.LBL_CLOSE = QtWidgets.QLabel(self.FRA_PAUSED)
        self.LBL_CLOSE.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_CLOSE.setObjectName("LBL_CLOSE")
        self.verticalLayout.addWidget(self.LBL_CLOSE)
        self.gridLayout.addWidget(self.FRA_PAUSED, 2, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 3)
        self.LBL_FILENAME_3 = QtWidgets.QLabel(Dialog)
        self.LBL_FILENAME_3.setObjectName("LBL_FILENAME_3")
        self.gridLayout.addWidget(self.LBL_FILENAME_3, 0, 0, 1, 3)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(16, 16))
        self.widget.setObjectName("widget")
        self.LAY_MAIN = QtWidgets.QGridLayout(self.widget)
        self.LAY_MAIN.setContentsMargins(0, 0, 0, 0)
        self.LAY_MAIN.setObjectName("LAY_MAIN")
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.LBL_PAUSED.setText(_translate("Dialog", "The wizard has paused for you to review the progress."))
        self.BTN_CONTINUE.setText(_translate("Dialog", "CLICK TO CONTINUE"))
        self.BTN_CONTINUE.setProperty("style", _translate("Dialog", "completed"))
        self.LBL_NEXT.setText(_translate("Dialog", "Next step: <a href=\"action:wizard_next\">{}</a>."))
        self.LBL_CLOSE.setText(_translate("Dialog", "You can always <a href=\"action:stop_wizard\">stop</a> using the wizard and continue manually."))
        self.LBL_FILENAME_3.setText(_translate("Dialog", "Workflow"))
        self.LBL_FILENAME_3.setProperty("style", _translate("Dialog", "title"))


