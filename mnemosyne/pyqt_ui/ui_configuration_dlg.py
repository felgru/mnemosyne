# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuration_dlg.ui'
#
# Created: Mon Apr 15 14:30:19 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ConfigurationDlg(object):
    def setupUi(self, ConfigurationDlg):
        ConfigurationDlg.setObjectName(_fromUtf8("ConfigurationDlg"))
        ConfigurationDlg.resize(237, 156)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ConfigurationDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tab_widget = QtGui.QTabWidget(ConfigurationDlg)
        self.tab_widget.setObjectName(_fromUtf8("tab_widget"))
        self.verticalLayout.addWidget(self.tab_widget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ok_button = QtGui.QPushButton(ConfigurationDlg)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.defaults_button = QtGui.QPushButton(ConfigurationDlg)
        self.defaults_button.setObjectName(_fromUtf8("defaults_button"))
        self.horizontalLayout.addWidget(self.defaults_button)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancel_button = QtGui.QPushButton(ConfigurationDlg)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ConfigurationDlg)
        self.tab_widget.setCurrentIndex(-1)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ConfigurationDlg.accept)
        QtCore.QObject.connect(self.defaults_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ConfigurationDlg.reset_to_defaults)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ConfigurationDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationDlg)

    def retranslateUi(self, ConfigurationDlg):
        ConfigurationDlg.setWindowTitle(_('Configuration'))
        self.ok_button.setText(_('&OK'))
        self.defaults_button.setText(_('&Defaults'))
        self.cancel_button.setText(_('&Cancel'))

