# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics_dlg.ui'
#
# Created: Mon Apr 15 14:30:20 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_StatisticsDlg(object):
    def setupUi(self, StatisticsDlg):
        StatisticsDlg.setObjectName(_fromUtf8("StatisticsDlg"))
        StatisticsDlg.resize(564, 545)
        self.verticalLayout_2 = QtGui.QVBoxLayout(StatisticsDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tab_widget = QtGui.QTabWidget(StatisticsDlg)
        self.tab_widget.setObjectName(_fromUtf8("tab_widget"))
        self.verticalLayout.addWidget(self.tab_widget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_button = QtGui.QPushButton(StatisticsDlg)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(StatisticsDlg)
        self.tab_widget.setCurrentIndex(-1)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), StatisticsDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(StatisticsDlg)

    def retranslateUi(self, StatisticsDlg):
        StatisticsDlg.setWindowTitle(_('Statistics'))
        self.ok_button.setText(_('&OK'))

