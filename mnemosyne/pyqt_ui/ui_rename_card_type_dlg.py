# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename_card_type_dlg.ui'
#
# Created: Mon Apr 15 14:30:23 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RenameCardTypeDlg(object):
    def setupUi(self, RenameCardTypeDlg):
        RenameCardTypeDlg.setObjectName(_fromUtf8("RenameCardTypeDlg"))
        RenameCardTypeDlg.resize(366, 88)
        self.verticalLayout_2 = QtGui.QVBoxLayout(RenameCardTypeDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(RenameCardTypeDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.card_type_name = QtGui.QLineEdit(RenameCardTypeDlg)
        self.card_type_name.setObjectName(_fromUtf8("card_type_name"))
        self.verticalLayout.addWidget(self.card_type_name)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ok_button = QtGui.QPushButton(RenameCardTypeDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(RenameCardTypeDlg)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RenameCardTypeDlg)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), RenameCardTypeDlg.accept)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), RenameCardTypeDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(RenameCardTypeDlg)

    def retranslateUi(self, RenameCardTypeDlg):
        RenameCardTypeDlg.setWindowTitle(_('Rename card type'))
        self.label.setText(_('Enter new card type name:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

