# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browse_cards_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BrowseCardsDlg(object):
    def setupUi(self, BrowseCardsDlg):
        BrowseCardsDlg.setObjectName("BrowseCardsDlg")
        BrowseCardsDlg.resize(990, 580)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(BrowseCardsDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(BrowseCardsDlg)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter_1 = QtWidgets.QSplitter(self.splitter_2)
        self.splitter_1.setOrientation(QtCore.Qt.Vertical)
        self.splitter_1.setObjectName("splitter_1")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.table = QtWidgets.QTableView(self.layoutWidget)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSortingEnabled(True)
        self.table.setObjectName("table")
        self.verticalLayout.addWidget(self.table)
        self.counter_label = QtWidgets.QLabel(self.layoutWidget)
        self.counter_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.counter_label.setObjectName("counter_label")
        self.verticalLayout.addWidget(self.counter_label)
        self.verticalLayout_2.addWidget(self.splitter_2)

        self.retranslateUi(BrowseCardsDlg)
        QtCore.QMetaObject.connectSlotsByName(BrowseCardsDlg)

    def retranslateUi(self, BrowseCardsDlg):
        _translate = QtCore.QCoreApplication.translate
        BrowseCardsDlg.setWindowTitle(_('Browse cards'))
        self.label_2.setText(_('Select one or more cards and right-click for more actions.'))
        self.counter_label.setText(_('XXX cards selected, of which XXX active'))

