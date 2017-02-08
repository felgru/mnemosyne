# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatisticsDlg(object):
    def setupUi(self, StatisticsDlg):
        StatisticsDlg.setObjectName("StatisticsDlg")
        StatisticsDlg.resize(564, 545)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(StatisticsDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_widget = QtWidgets.QTabWidget(StatisticsDlg)
        self.tab_widget.setObjectName("tab_widget")
        self.verticalLayout.addWidget(self.tab_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_button = QtWidgets.QPushButton(StatisticsDlg)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(StatisticsDlg)
        self.tab_widget.setCurrentIndex(-1)
        self.ok_button.clicked.connect(StatisticsDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(StatisticsDlg)

    def retranslateUi(self, StatisticsDlg):
        _translate = QtCore.QCoreApplication.translate
        StatisticsDlg.setWindowTitle(_('Statistics'))
        self.ok_button.setText(_('&OK'))

