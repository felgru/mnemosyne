# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename_card_type_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RenameCardTypeDlg(object):
    def setupUi(self, RenameCardTypeDlg):
        RenameCardTypeDlg.setObjectName("RenameCardTypeDlg")
        RenameCardTypeDlg.resize(366, 88)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(RenameCardTypeDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(RenameCardTypeDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.card_type_name = QtWidgets.QLineEdit(RenameCardTypeDlg)
        self.card_type_name.setObjectName("card_type_name")
        self.verticalLayout.addWidget(self.card_type_name)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QtWidgets.QPushButton(RenameCardTypeDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(RenameCardTypeDlg)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RenameCardTypeDlg)
        self.ok_button.clicked.connect(RenameCardTypeDlg.accept)
        self.cancel_button.clicked.connect(RenameCardTypeDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(RenameCardTypeDlg)

    def retranslateUi(self, RenameCardTypeDlg):
        _translate = QtCore.QCoreApplication.translate
        RenameCardTypeDlg.setWindowTitle(_('Rename card type'))
        self.label.setText(_('Enter new card type name:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

