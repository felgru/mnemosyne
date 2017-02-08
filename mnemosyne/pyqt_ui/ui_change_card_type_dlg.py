# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_card_type_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChangeCardTypeDlg(object):
    def setupUi(self, ChangeCardTypeDlg):
        ChangeCardTypeDlg.setObjectName("ChangeCardTypeDlg")
        ChangeCardTypeDlg.resize(384, 73)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ChangeCardTypeDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ChangeCardTypeDlg)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.card_types_widget = QtWidgets.QComboBox(ChangeCardTypeDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_types_widget.sizePolicy().hasHeightForWidth())
        self.card_types_widget.setSizePolicy(sizePolicy)
        self.card_types_widget.setObjectName("card_types_widget")
        self.horizontalLayout.addWidget(self.card_types_widget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ok_button = QtWidgets.QPushButton(ChangeCardTypeDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_2.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(ChangeCardTypeDlg)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ChangeCardTypeDlg)
        self.ok_button.clicked.connect(ChangeCardTypeDlg.accept)
        self.cancel_button.clicked.connect(ChangeCardTypeDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangeCardTypeDlg)

    def retranslateUi(self, ChangeCardTypeDlg):
        _translate = QtCore.QCoreApplication.translate
        ChangeCardTypeDlg.setWindowTitle(_('Change card type'))
        self.label.setText(_('New card type:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

