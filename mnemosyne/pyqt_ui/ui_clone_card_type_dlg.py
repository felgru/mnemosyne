# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clone_card_type_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CloneCardTypeDlg(object):
    def setupUi(self, CloneCardTypeDlg):
        CloneCardTypeDlg.setObjectName("CloneCardTypeDlg")
        CloneCardTypeDlg.resize(400, 100)
        CloneCardTypeDlg.setMinimumSize(QtCore.QSize(400, 100))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CloneCardTypeDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(CloneCardTypeDlg)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.parent_type = QtWidgets.QComboBox(CloneCardTypeDlg)
        self.parent_type.setObjectName("parent_type")
        self.gridLayout.addWidget(self.parent_type, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(CloneCardTypeDlg)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(CloneCardTypeDlg)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.OK_button = QtWidgets.QPushButton(CloneCardTypeDlg)
        self.OK_button.setEnabled(False)
        self.OK_button.setObjectName("OK_button")
        self.horizontalLayout_3.addWidget(self.OK_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(CloneCardTypeDlg)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CloneCardTypeDlg)
        self.OK_button.clicked.connect(CloneCardTypeDlg.accept)
        self.cancel_button.clicked.connect(CloneCardTypeDlg.reject)
        self.name.textChanged['QString'].connect(CloneCardTypeDlg.name_changed)
        QtCore.QMetaObject.connectSlotsByName(CloneCardTypeDlg)

    def retranslateUi(self, CloneCardTypeDlg):
        _translate = QtCore.QCoreApplication.translate
        CloneCardTypeDlg.setWindowTitle(_('Clone card type'))
        self.label.setText(_('Cloned from:'))
        self.label_2.setText(_('Clone name:'))
        self.OK_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

