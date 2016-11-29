# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card_set_name_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CardSetNameDlg(object):
    def setupUi(self, CardSetNameDlg):
        CardSetNameDlg.setObjectName("CardSetNameDlg")
        CardSetNameDlg.resize(312, 36)
        self.verticalLayout = QtWidgets.QVBoxLayout(CardSetNameDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(CardSetNameDlg)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.set_name = QtWidgets.QComboBox(CardSetNameDlg)
        self.set_name.setEditable(True)
        self.set_name.setObjectName("set_name")
        self.horizontalLayout.addWidget(self.set_name)
        self.ok_button = QtWidgets.QPushButton(CardSetNameDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CardSetNameDlg)
        self.ok_button.clicked.connect(CardSetNameDlg.accept)
        self.set_name.editTextChanged['QString'].connect(CardSetNameDlg.text_changed)
        QtCore.QMetaObject.connectSlotsByName(CardSetNameDlg)

    def retranslateUi(self, CardSetNameDlg):
        _translate = QtCore.QCoreApplication.translate
        CardSetNameDlg.setWindowTitle(_('Card set name'))
        self.label.setText(_('Card set name:'))
        self.ok_button.setText(_('&OK'))

