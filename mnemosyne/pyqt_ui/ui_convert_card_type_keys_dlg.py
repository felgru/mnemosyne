# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert_card_type_keys_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConvertCardTypeKeysDlg(object):
    def setupUi(self, ConvertCardTypeKeysDlg):
        ConvertCardTypeKeysDlg.setObjectName("ConvertCardTypeKeysDlg")
        ConvertCardTypeKeysDlg.resize(260, 105)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ConvertCardTypeKeysDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(ConvertCardTypeKeysDlg)
        self.label_2.setMinimumSize(QtCore.QSize(250, 40))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(ConvertCardTypeKeysDlg)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(ConvertCardTypeKeysDlg)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QtWidgets.QPushButton(ConvertCardTypeKeysDlg)
        self.ok_button.setEnabled(False)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(ConvertCardTypeKeysDlg)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ConvertCardTypeKeysDlg)
        self.ok_button.clicked.connect(ConvertCardTypeKeysDlg.accept)
        self.cancel_button.clicked.connect(ConvertCardTypeKeysDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ConvertCardTypeKeysDlg)

    def retranslateUi(self, ConvertCardTypeKeysDlg):
        _translate = QtCore.QCoreApplication.translate
        ConvertCardTypeKeysDlg.setWindowTitle(_('Convert card type data'))
        self.label_2.setText(_('Set the correspondence between data in the old and the new card type:'))
        self.label.setText(_('Old:'))
        self.label_3.setText(_('New:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

