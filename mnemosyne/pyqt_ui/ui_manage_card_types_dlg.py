# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_card_types_dlg.ui'
#
# Created: Mon Apr 15 14:30:18 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ManageCardTypesDlg(object):
    def setupUi(self, ManageCardTypesDlg):
        ManageCardTypesDlg.setObjectName(_fromUtf8("ManageCardTypesDlg"))
        ManageCardTypesDlg.resize(352, 245)
        ManageCardTypesDlg.setMinimumSize(QtCore.QSize(300, 240))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ManageCardTypesDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(ManageCardTypesDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.cloned_card_types = QtGui.QListWidget(ManageCardTypesDlg)
        self.cloned_card_types.setObjectName(_fromUtf8("cloned_card_types"))
        self.verticalLayout.addWidget(self.cloned_card_types)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clone_button = QtGui.QPushButton(ManageCardTypesDlg)
        self.clone_button.setObjectName(_fromUtf8("clone_button"))
        self.horizontalLayout.addWidget(self.clone_button)
        self.rename_button = QtGui.QPushButton(ManageCardTypesDlg)
        self.rename_button.setObjectName(_fromUtf8("rename_button"))
        self.horizontalLayout.addWidget(self.rename_button)
        self.delete_button = QtGui.QPushButton(ManageCardTypesDlg)
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.horizontalLayout.addWidget(self.delete_button)
        self.exit_button = QtGui.QPushButton(ManageCardTypesDlg)
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.horizontalLayout.addWidget(self.exit_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ManageCardTypesDlg)
        QtCore.QObject.connect(self.exit_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageCardTypesDlg.reject)
        QtCore.QObject.connect(self.clone_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageCardTypesDlg.clone_card_type)
        QtCore.QObject.connect(self.delete_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageCardTypesDlg.delete_card_type)
        QtCore.QObject.connect(self.rename_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageCardTypesDlg.rename_card_type)
        QtCore.QMetaObject.connectSlotsByName(ManageCardTypesDlg)

    def retranslateUi(self, ManageCardTypesDlg):
        ManageCardTypesDlg.setWindowTitle(_('Card type manager'))
        self.label_2.setText(_('Cloned card types:'))
        self.clone_button.setText(_('&New clone'))
        self.rename_button.setText(_('&Rename'))
        self.delete_button.setText(_('&Delete'))
        self.exit_button.setText(_('E&xit'))

