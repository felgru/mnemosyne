# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card_set_name_dlg.ui'
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

class Ui_CardSetNameDlg(object):
    def setupUi(self, CardSetNameDlg):
        CardSetNameDlg.setObjectName(_fromUtf8("CardSetNameDlg"))
        CardSetNameDlg.resize(312, 36)
        self.verticalLayout = QtGui.QVBoxLayout(CardSetNameDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(CardSetNameDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.set_name = QtGui.QComboBox(CardSetNameDlg)
        self.set_name.setEditable(True)
        self.set_name.setObjectName(_fromUtf8("set_name"))
        self.horizontalLayout.addWidget(self.set_name)
        self.ok_button = QtGui.QPushButton(CardSetNameDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CardSetNameDlg)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), CardSetNameDlg.accept)
        QtCore.QObject.connect(self.set_name, QtCore.SIGNAL(_fromUtf8("editTextChanged(QString)")), CardSetNameDlg.text_changed)
        QtCore.QMetaObject.connectSlotsByName(CardSetNameDlg)

    def retranslateUi(self, CardSetNameDlg):
        CardSetNameDlg.setWindowTitle(_('Card set name'))
        self.label.setText(_('Card set name:'))
        self.ok_button.setText(_('&OK'))

