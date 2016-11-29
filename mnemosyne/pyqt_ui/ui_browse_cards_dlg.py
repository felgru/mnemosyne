# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browse_cards_dlg.ui'
#
# Created: Mon Apr 15 14:30:21 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BrowseCardsDlg(object):
    def setupUi(self, BrowseCardsDlg):
        BrowseCardsDlg.setObjectName(_fromUtf8("BrowseCardsDlg"))
        BrowseCardsDlg.resize(990, 580)
        self.verticalLayout_2 = QtGui.QVBoxLayout(BrowseCardsDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter_2 = QtGui.QSplitter(BrowseCardsDlg)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter_1 = QtGui.QSplitter(self.splitter_2)
        self.splitter_1.setOrientation(QtCore.Qt.Vertical)
        self.splitter_1.setObjectName(_fromUtf8("splitter_1"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.table = QtGui.QTableView(self.layoutWidget)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setSortingEnabled(True)
        self.table.setObjectName(_fromUtf8("table"))
        self.verticalLayout.addWidget(self.table)
        self.counter_label = QtGui.QLabel(self.layoutWidget)
        self.counter_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.counter_label.setObjectName(_fromUtf8("counter_label"))
        self.verticalLayout.addWidget(self.counter_label)
        self.verticalLayout_2.addWidget(self.splitter_2)

        self.retranslateUi(BrowseCardsDlg)
        QtCore.QMetaObject.connectSlotsByName(BrowseCardsDlg)

    def retranslateUi(self, BrowseCardsDlg):
        BrowseCardsDlg.setWindowTitle(_('Browse cards'))
        self.label_2.setText(_('Select one or more cards and right-click for more actions.'))
        self.counter_label.setText(_('XXX cards selected, of which XXX active'))

