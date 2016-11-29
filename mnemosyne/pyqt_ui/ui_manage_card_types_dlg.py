# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_card_types_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManageCardTypesDlg(object):
    def setupUi(self, ManageCardTypesDlg):
        ManageCardTypesDlg.setObjectName("ManageCardTypesDlg")
        ManageCardTypesDlg.resize(352, 245)
        ManageCardTypesDlg.setMinimumSize(QtCore.QSize(300, 240))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ManageCardTypesDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(ManageCardTypesDlg)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.cloned_card_types = QtWidgets.QListWidget(ManageCardTypesDlg)
        self.cloned_card_types.setObjectName("cloned_card_types")
        self.verticalLayout.addWidget(self.cloned_card_types)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clone_button = QtWidgets.QPushButton(ManageCardTypesDlg)
        self.clone_button.setObjectName("clone_button")
        self.horizontalLayout.addWidget(self.clone_button)
        self.rename_button = QtWidgets.QPushButton(ManageCardTypesDlg)
        self.rename_button.setObjectName("rename_button")
        self.horizontalLayout.addWidget(self.rename_button)
        self.delete_button = QtWidgets.QPushButton(ManageCardTypesDlg)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.exit_button = QtWidgets.QPushButton(ManageCardTypesDlg)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout.addWidget(self.exit_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ManageCardTypesDlg)
        self.exit_button.clicked.connect(ManageCardTypesDlg.reject)
        self.clone_button.clicked.connect(ManageCardTypesDlg.clone_card_type)
        self.delete_button.clicked.connect(ManageCardTypesDlg.delete_card_type)
        self.rename_button.clicked.connect(ManageCardTypesDlg.rename_card_type)
        QtCore.QMetaObject.connectSlotsByName(ManageCardTypesDlg)

    def retranslateUi(self, ManageCardTypesDlg):
        _translate = QtCore.QCoreApplication.translate
        ManageCardTypesDlg.setWindowTitle(_('Card type manager'))
        self.label_2.setText(_('Cloned card types:'))
        self.clone_button.setText(_('&New clone'))
        self.rename_button.setText(_('&Rename'))
        self.delete_button.setText(_('&Delete'))
        self.exit_button.setText(_('E&xit'))

