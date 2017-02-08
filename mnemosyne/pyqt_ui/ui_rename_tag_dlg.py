# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename_tag_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RenameTagDlg(object):
    def setupUi(self, RenameTagDlg):
        RenameTagDlg.setObjectName("RenameTagDlg")
        RenameTagDlg.resize(366, 82)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(RenameTagDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(RenameTagDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tag_name = QtWidgets.QLineEdit(RenameTagDlg)
        self.tag_name.setObjectName("tag_name")
        self.verticalLayout.addWidget(self.tag_name)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QtWidgets.QPushButton(RenameTagDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(RenameTagDlg)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RenameTagDlg)
        self.ok_button.clicked.connect(RenameTagDlg.accept)
        self.cancel_button.clicked.connect(RenameTagDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(RenameTagDlg)

    def retranslateUi(self, RenameTagDlg):
        _translate = QtCore.QCoreApplication.translate
        RenameTagDlg.setWindowTitle(_('Rename tag'))
        self.label.setText(_('Enter new tag name:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

