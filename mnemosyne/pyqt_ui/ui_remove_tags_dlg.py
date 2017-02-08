# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remove_tags_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RemoveTagsDlg(object):
    def setupUi(self, RemoveTagsDlg):
        RemoveTagsDlg.setObjectName("RemoveTagsDlg")
        RemoveTagsDlg.resize(257, 260)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(RemoveTagsDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(RemoveTagsDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tag_list = QtWidgets.QListWidget(RemoveTagsDlg)
        self.tag_list.setObjectName("tag_list")
        self.verticalLayout.addWidget(self.tag_list)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.ok_button = QtWidgets.QPushButton(RemoveTagsDlg)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.hboxlayout.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(101, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(RemoveTagsDlg)
        self.cancel_button.setObjectName("cancel_button")
        self.hboxlayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RemoveTagsDlg)
        self.cancel_button.clicked.connect(RemoveTagsDlg.reject)
        self.ok_button.clicked.connect(RemoveTagsDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(RemoveTagsDlg)

    def retranslateUi(self, RemoveTagsDlg):
        _translate = QtCore.QCoreApplication.translate
        RemoveTagsDlg.setWindowTitle(_('Remove tags'))
        self.label.setText(_('Tags to remove:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

from . import mnemosyne_rc
