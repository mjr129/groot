# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/martinrusilowicz/work/apps/groot/groot_gui/forms/designer/frm_lego_designer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1263, 1137)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.FRA_TOOLBAR = QtWidgets.QFrame(Dialog)
        self.FRA_TOOLBAR.setObjectName("FRA_TOOLBAR")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.FRA_TOOLBAR)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.FRA_TOOLBAR)
        self.label_2.setStyleSheet("border: 0px solid black;\n"
"border-bottom: 1px solid black;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.BTN_FIND = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_FIND.sizePolicy().hasHeightForWidth())
        self.BTN_FIND.setSizePolicy(sizePolicy)
        self.BTN_FIND.setMaximumSize(QtCore.QSize(64, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/groot/find.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_FIND.setIcon(icon)
        self.BTN_FIND.setIconSize(QtCore.QSize(32, 32))
        self.BTN_FIND.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_FIND.setObjectName("BTN_FIND")
        self.verticalLayout.addWidget(self.BTN_FIND)
        self.BTN_SELECT = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_SELECT.sizePolicy().hasHeightForWidth())
        self.BTN_SELECT.setSizePolicy(sizePolicy)
        self.BTN_SELECT.setMaximumSize(QtCore.QSize(64, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/groot/select.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_SELECT.setIcon(icon1)
        self.BTN_SELECT.setIconSize(QtCore.QSize(32, 32))
        self.BTN_SELECT.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_SELECT.setObjectName("BTN_SELECT")
        self.verticalLayout.addWidget(self.BTN_SELECT)
        self.BTN_DOMAINS = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_DOMAINS.sizePolicy().hasHeightForWidth())
        self.BTN_DOMAINS.setSizePolicy(sizePolicy)
        self.BTN_DOMAINS.setMaximumSize(QtCore.QSize(64, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/groot/domain.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_DOMAINS.setIcon(icon2)
        self.BTN_DOMAINS.setIconSize(QtCore.QSize(32, 32))
        self.BTN_DOMAINS.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_DOMAINS.setObjectName("BTN_DOMAINS")
        self.verticalLayout.addWidget(self.BTN_DOMAINS)
        self.BTN_COLOUR = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_COLOUR.sizePolicy().hasHeightForWidth())
        self.BTN_COLOUR.setSizePolicy(sizePolicy)
        self.BTN_COLOUR.setMaximumSize(QtCore.QSize(64, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/groot/colour.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_COLOUR.setIcon(icon3)
        self.BTN_COLOUR.setIconSize(QtCore.QSize(32, 32))
        self.BTN_COLOUR.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_COLOUR.setObjectName("BTN_COLOUR")
        self.verticalLayout.addWidget(self.BTN_COLOUR)
        self.BTN_ALIGN = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_ALIGN.sizePolicy().hasHeightForWidth())
        self.BTN_ALIGN.setSizePolicy(sizePolicy)
        self.BTN_ALIGN.setMaximumSize(QtCore.QSize(64, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/groot/align.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_ALIGN.setIcon(icon4)
        self.BTN_ALIGN.setIconSize(QtCore.QSize(32, 32))
        self.BTN_ALIGN.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_ALIGN.setObjectName("BTN_ALIGN")
        self.verticalLayout.addWidget(self.BTN_ALIGN)
        self.label_3 = QtWidgets.QLabel(self.FRA_TOOLBAR)
        self.label_3.setStyleSheet("border: 0px solid black;\n"
"border-bottom: 1px solid black;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.BTN_LEGEND = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_LEGEND.sizePolicy().hasHeightForWidth())
        self.BTN_LEGEND.setSizePolicy(sizePolicy)
        self.BTN_LEGEND.setMaximumSize(QtCore.QSize(64, 16777215))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/groot/legend.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_LEGEND.setIcon(icon5)
        self.BTN_LEGEND.setIconSize(QtCore.QSize(32, 32))
        self.BTN_LEGEND.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_LEGEND.setObjectName("BTN_LEGEND")
        self.verticalLayout.addWidget(self.BTN_LEGEND)
        self.BTN_OPTIONS = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_OPTIONS.sizePolicy().hasHeightForWidth())
        self.BTN_OPTIONS.setSizePolicy(sizePolicy)
        self.BTN_OPTIONS.setMaximumSize(QtCore.QSize(64, 16777215))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/groot/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_OPTIONS.setIcon(icon6)
        self.BTN_OPTIONS.setIconSize(QtCore.QSize(32, 32))
        self.BTN_OPTIONS.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_OPTIONS.setObjectName("BTN_OPTIONS")
        self.verticalLayout.addWidget(self.BTN_OPTIONS)
        self.BTN_REFRESH = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_REFRESH.sizePolicy().hasHeightForWidth())
        self.BTN_REFRESH.setSizePolicy(sizePolicy)
        self.BTN_REFRESH.setMaximumSize(QtCore.QSize(64, 16777215))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/groot/refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_REFRESH.setIcon(icon7)
        self.BTN_REFRESH.setIconSize(QtCore.QSize(32, 32))
        self.BTN_REFRESH.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_REFRESH.setObjectName("BTN_REFRESH")
        self.verticalLayout.addWidget(self.BTN_REFRESH)
        self.BTN_HELP = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_HELP.sizePolicy().hasHeightForWidth())
        self.BTN_HELP.setSizePolicy(sizePolicy)
        self.BTN_HELP.setMaximumSize(QtCore.QSize(64, 16777215))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/groot/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_HELP.setIcon(icon8)
        self.BTN_HELP.setIconSize(QtCore.QSize(32, 32))
        self.BTN_HELP.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_HELP.setObjectName("BTN_HELP")
        self.verticalLayout.addWidget(self.BTN_HELP)
        self.label_4 = QtWidgets.QLabel(self.FRA_TOOLBAR)
        self.label_4.setStyleSheet("border: 0px solid black;\n"
"border-bottom: 1px solid black;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.BTN_SHOW_EDIT = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_SHOW_EDIT.sizePolicy().hasHeightForWidth())
        self.BTN_SHOW_EDIT.setSizePolicy(sizePolicy)
        self.BTN_SHOW_EDIT.setMaximumSize(QtCore.QSize(64, 16777215))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/groot/maximize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_SHOW_EDIT.setIcon(icon9)
        self.BTN_SHOW_EDIT.setIconSize(QtCore.QSize(32, 32))
        self.BTN_SHOW_EDIT.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_SHOW_EDIT.setObjectName("BTN_SHOW_EDIT")
        self.verticalLayout.addWidget(self.BTN_SHOW_EDIT)
        self.BTN_DELETE_GENE = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_DELETE_GENE.sizePolicy().hasHeightForWidth())
        self.BTN_DELETE_GENE.setSizePolicy(sizePolicy)
        self.BTN_DELETE_GENE.setMaximumSize(QtCore.QSize(64, 16777215))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/groot/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_DELETE_GENE.setIcon(icon10)
        self.BTN_DELETE_GENE.setIconSize(QtCore.QSize(32, 32))
        self.BTN_DELETE_GENE.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_DELETE_GENE.setObjectName("BTN_DELETE_GENE")
        self.verticalLayout.addWidget(self.BTN_DELETE_GENE)
        self.BTN_OUTGROUP_GENE = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_OUTGROUP_GENE.sizePolicy().hasHeightForWidth())
        self.BTN_OUTGROUP_GENE.setSizePolicy(sizePolicy)
        self.BTN_OUTGROUP_GENE.setMaximumSize(QtCore.QSize(64, 16777215))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/groot/outgroup.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_OUTGROUP_GENE.setIcon(icon11)
        self.BTN_OUTGROUP_GENE.setIconSize(QtCore.QSize(32, 32))
        self.BTN_OUTGROUP_GENE.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_OUTGROUP_GENE.setObjectName("BTN_OUTGROUP_GENE")
        self.verticalLayout.addWidget(self.BTN_OUTGROUP_GENE)
        self.BTN_RENAME_GENE = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_RENAME_GENE.sizePolicy().hasHeightForWidth())
        self.BTN_RENAME_GENE.setSizePolicy(sizePolicy)
        self.BTN_RENAME_GENE.setMaximumSize(QtCore.QSize(64, 16777215))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/groot/save_as.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_RENAME_GENE.setIcon(icon12)
        self.BTN_RENAME_GENE.setIconSize(QtCore.QSize(32, 32))
        self.BTN_RENAME_GENE.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_RENAME_GENE.setObjectName("BTN_RENAME_GENE")
        self.verticalLayout.addWidget(self.BTN_RENAME_GENE)
        self.BTN_COMPONENT_GENE = QtWidgets.QToolButton(self.FRA_TOOLBAR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_COMPONENT_GENE.sizePolicy().hasHeightForWidth())
        self.BTN_COMPONENT_GENE.setSizePolicy(sizePolicy)
        self.BTN_COMPONENT_GENE.setMaximumSize(QtCore.QSize(64, 16777215))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/groot/import_.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_COMPONENT_GENE.setIcon(icon13)
        self.BTN_COMPONENT_GENE.setIconSize(QtCore.QSize(32, 32))
        self.BTN_COMPONENT_GENE.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BTN_COMPONENT_GENE.setObjectName("BTN_COMPONENT_GENE")
        self.verticalLayout.addWidget(self.BTN_COMPONENT_GENE)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.FRA_TOOLBAR, 0, 1, 1, 1)
        self.FRA_MAIN = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FRA_MAIN.sizePolicy().hasHeightForWidth())
        self.FRA_MAIN.setSizePolicy(sizePolicy)
        self.FRA_MAIN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRA_MAIN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRA_MAIN.setObjectName("FRA_MAIN")
        self.gridLayout.addWidget(self.FRA_MAIN, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BTN_S_DOMAINS_ = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_S_DOMAINS_.sizePolicy().hasHeightForWidth())
        self.BTN_S_DOMAINS_.setSizePolicy(sizePolicy)
        self.BTN_S_DOMAINS_.setStyleSheet("text-align: left;")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/groot/black_domain.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_S_DOMAINS_.setIcon(icon14)
        self.BTN_S_DOMAINS_.setAutoDefault(False)
        self.BTN_S_DOMAINS_.setFlat(True)
        self.BTN_S_DOMAINS_.setObjectName("BTN_S_DOMAINS_")
        self.gridLayout_2.addWidget(self.BTN_S_DOMAINS_, 1, 1, 1, 1)
        self.BTN_S_COMPS_ = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_S_COMPS_.sizePolicy().hasHeightForWidth())
        self.BTN_S_COMPS_.setSizePolicy(sizePolicy)
        self.BTN_S_COMPS_.setStyleSheet("text-align: left;")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/groot/black_major.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_S_COMPS_.setIcon(icon15)
        self.BTN_S_COMPS_.setAutoDefault(False)
        self.BTN_S_COMPS_.setFlat(True)
        self.BTN_S_COMPS_.setObjectName("BTN_S_COMPS_")
        self.gridLayout_2.addWidget(self.BTN_S_COMPS_, 1, 5, 1, 1)
        self.BTN_S_GENES_ = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_S_GENES_.sizePolicy().hasHeightForWidth())
        self.BTN_S_GENES_.setSizePolicy(sizePolicy)
        self.BTN_S_GENES_.setStyleSheet("text-align: left;")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/groot/black_gene.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_S_GENES_.setIcon(icon16)
        self.BTN_S_GENES_.setAutoDefault(False)
        self.BTN_S_GENES_.setFlat(True)
        self.BTN_S_GENES_.setObjectName("BTN_S_GENES_")
        self.gridLayout_2.addWidget(self.BTN_S_GENES_, 1, 3, 1, 1)
        self.LBL_DOMAIN = QtWidgets.QLabel(self.frame)
        self.LBL_DOMAIN.setStyleSheet("font-size: 8px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;")
        self.LBL_DOMAIN.setObjectName("LBL_DOMAIN")
        self.gridLayout_2.addWidget(self.LBL_DOMAIN, 0, 1, 1, 1)
        self.LBL_GENE = QtWidgets.QLabel(self.frame)
        self.LBL_GENE.setStyleSheet("font-size: 8px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;")
        self.LBL_GENE.setObjectName("LBL_GENE")
        self.gridLayout_2.addWidget(self.LBL_GENE, 0, 3, 1, 1)
        self.LBL_COMPONENT = QtWidgets.QLabel(self.frame)
        self.LBL_COMPONENT.setStyleSheet("font-size: 8px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;")
        self.LBL_COMPONENT.setObjectName("LBL_COMPONENT")
        self.gridLayout_2.addWidget(self.LBL_COMPONENT, 0, 5, 1, 1)
        self.LBL_COMPONENT_2 = QtWidgets.QLabel(self.frame)
        self.LBL_COMPONENT_2.setStyleSheet("font-size: 8px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;")
        self.LBL_COMPONENT_2.setObjectName("LBL_COMPONENT_2")
        self.gridLayout_2.addWidget(self.LBL_COMPONENT_2, 0, 6, 1, 1)
        self.BTN_S_MINCOMPS_ = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_S_MINCOMPS_.sizePolicy().hasHeightForWidth())
        self.BTN_S_MINCOMPS_.setSizePolicy(sizePolicy)
        self.BTN_S_MINCOMPS_.setStyleSheet("text-align: left;")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/groot/black_minor.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_S_MINCOMPS_.setIcon(icon17)
        self.BTN_S_MINCOMPS_.setAutoDefault(False)
        self.BTN_S_MINCOMPS_.setFlat(True)
        self.BTN_S_MINCOMPS_.setObjectName("BTN_S_MINCOMPS_")
        self.gridLayout_2.addWidget(self.BTN_S_MINCOMPS_, 1, 6, 1, 1)
        self.LBL_EDGE = QtWidgets.QLabel(self.frame)
        self.LBL_EDGE.setStyleSheet("font-size: 8px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;")
        self.LBL_EDGE.setObjectName("LBL_EDGE")
        self.gridLayout_2.addWidget(self.LBL_EDGE, 0, 7, 1, 1)
        self.BTN_S_EDGES_ = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_S_EDGES_.sizePolicy().hasHeightForWidth())
        self.BTN_S_EDGES_.setSizePolicy(sizePolicy)
        self.BTN_S_EDGES_.setStyleSheet("text-align: left;")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/groot/black_edge.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_S_EDGES_.setIcon(icon18)
        self.BTN_S_EDGES_.setAutoDefault(False)
        self.BTN_S_EDGES_.setFlat(True)
        self.BTN_S_EDGES_.setObjectName("BTN_S_EDGES_")
        self.gridLayout_2.addWidget(self.BTN_S_EDGES_, 1, 7, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Selection"))
        self.BTN_FIND.setToolTip(_translate("Dialog", "Select domains adjacent to those currently selected"))
        self.BTN_FIND.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_FIND.setText(_translate("Dialog", "Find"))
        self.BTN_SELECT.setToolTip(_translate("Dialog", "Select domains adjacent to those currently selected"))
        self.BTN_SELECT.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_SELECT.setText(_translate("Dialog", "Select"))
        self.BTN_DOMAINS.setToolTip(_translate("Dialog", "Align the selected domains"))
        self.BTN_DOMAINS.setText(_translate("Dialog", "Domains"))
        self.BTN_COLOUR.setToolTip(_translate("Dialog", "Colour the selected domains"))
        self.BTN_COLOUR.setText(_translate("Dialog", "Colour"))
        self.BTN_ALIGN.setToolTip(_translate("Dialog", "Align the selected domains"))
        self.BTN_ALIGN.setText(_translate("Dialog", "Position"))
        self.label_3.setText(_translate("Dialog", "View"))
        self.BTN_LEGEND.setToolTip(_translate("Dialog", "Shows the colour legend"))
        self.BTN_LEGEND.setText(_translate("Dialog", "Legend"))
        self.BTN_OPTIONS.setToolTip(_translate("Dialog", "Show the view options dialogue"))
        self.BTN_OPTIONS.setText(_translate("Dialog", "Options"))
        self.BTN_REFRESH.setToolTip(_translate("Dialog", "Refresh the view to reflect any changes in the model"))
        self.BTN_REFRESH.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_REFRESH.setText(_translate("Dialog", "Refresh"))
        self.BTN_HELP.setToolTip(_translate("Dialog", "Refresh the view to reflect any changes in the model"))
        self.BTN_HELP.setStatusTip(_translate("Dialog", "Remove edge"))
        self.BTN_HELP.setText(_translate("Dialog", "Help"))
        self.label_4.setText(_translate("Dialog", "Model"))
        self.BTN_SHOW_EDIT.setToolTip(_translate("Dialog", "Shows or hides the edit options"))
        self.BTN_SHOW_EDIT.setText(_translate("Dialog", "Edit"))
        self.BTN_DELETE_GENE.setToolTip(_translate("Dialog", "Deletes the selected gene(s)"))
        self.BTN_DELETE_GENE.setText(_translate("Dialog", "Delete"))
        self.BTN_OUTGROUP_GENE.setToolTip(_translate("Dialog", "Sets the selected gene(s) as the outgroup(s)"))
        self.BTN_OUTGROUP_GENE.setText(_translate("Dialog", "Outgroup"))
        self.BTN_RENAME_GENE.setToolTip(_translate("Dialog", "Renames the selected gene"))
        self.BTN_RENAME_GENE.setText(_translate("Dialog", "Rename"))
        self.BTN_COMPONENT_GENE.setToolTip(_translate("Dialog", "Make a component with the selected gene(s) as its major elements."))
        self.BTN_COMPONENT_GENE.setText(_translate("Dialog", "Component"))
        self.BTN_S_DOMAINS_.setText(_translate("Dialog", "..."))
        self.BTN_S_COMPS_.setText(_translate("Dialog", "..."))
        self.BTN_S_GENES_.setText(_translate("Dialog", "..."))
        self.LBL_DOMAIN.setText(_translate("Dialog", "Domain"))
        self.LBL_GENE.setText(_translate("Dialog", "Gene"))
        self.LBL_COMPONENT.setText(_translate("Dialog", "Component"))
        self.LBL_COMPONENT_2.setText(_translate("Dialog", "Minor comp."))
        self.BTN_S_MINCOMPS_.setText(_translate("Dialog", "..."))
        self.LBL_EDGE.setText(_translate("Dialog", "Edge"))
        self.BTN_S_EDGES_.setText(_translate("Dialog", "..."))


