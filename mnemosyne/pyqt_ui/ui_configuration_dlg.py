# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuration_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigurationDlg(object):
    def setupUi(self, ConfigurationDlg):
        ConfigurationDlg.setObjectName("ConfigurationDlg")
        ConfigurationDlg.resize(271, 156)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ConfigurationDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_widget = QtWidgets.QTabWidget(ConfigurationDlg)
        self.tab_widget.setObjectName("tab_widget")
        self.verticalLayout.addWidget(self.tab_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QtWidgets.QPushButton(ConfigurationDlg)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.defaults_button = QtWidgets.QPushButton(ConfigurationDlg)
        self.defaults_button.setAutoDefault(True)
        self.defaults_button.setObjectName("defaults_button")
        self.horizontalLayout.addWidget(self.defaults_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancel_button = QtWidgets.QPushButton(ConfigurationDlg)
        self.cancel_button.setAutoDefault(True)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ConfigurationDlg)
        self.tab_widget.setCurrentIndex(-1)
        self.ok_button.clicked.connect(ConfigurationDlg.accept)
        self.defaults_button.clicked.connect(ConfigurationDlg.reset_to_defaults)
        self.cancel_button.clicked.connect(ConfigurationDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationDlg)

    def retranslateUi(self, ConfigurationDlg):
        _translate = QtCore.QCoreApplication.translate
        ConfigurationDlg.setWindowTitle(_('Configuration'))
        self.ok_button.setText(_('&OK'))
        self.defaults_button.setText(_('&Defaults'))
        self.cancel_button.setText(_('&Cancel'))

