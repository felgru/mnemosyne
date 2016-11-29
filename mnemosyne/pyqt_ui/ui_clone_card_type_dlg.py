# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clone_card_type_dlg.ui'
#
# Created: Mon Apr 15 14:30:18 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CloneCardTypeDlg(object):
    def setupUi(self, CloneCardTypeDlg):
        CloneCardTypeDlg.setObjectName(_fromUtf8("CloneCardTypeDlg"))
        CloneCardTypeDlg.resize(400, 100)
        CloneCardTypeDlg.setMinimumSize(QtCore.QSize(400, 100))
        self.verticalLayout_2 = QtGui.QVBoxLayout(CloneCardTypeDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(CloneCardTypeDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.parent_type = QtGui.QComboBox(CloneCardTypeDlg)
        self.parent_type.setObjectName(_fromUtf8("parent_type"))
        self.gridLayout.addWidget(self.parent_type, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(CloneCardTypeDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.name = QtGui.QLineEdit(CloneCardTypeDlg)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.OK_button = QtGui.QPushButton(CloneCardTypeDlg)
        self.OK_button.setEnabled(False)
        self.OK_button.setObjectName(_fromUtf8("OK_button"))
        self.horizontalLayout_3.addWidget(self.OK_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(CloneCardTypeDlg)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CloneCardTypeDlg)
        QtCore.QObject.connect(self.OK_button, QtCore.SIGNAL(_fromUtf8("clicked()")), CloneCardTypeDlg.accept)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), CloneCardTypeDlg.reject)
        QtCore.QObject.connect(self.name, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), CloneCardTypeDlg.name_changed)
        QtCore.QMetaObject.connectSlotsByName(CloneCardTypeDlg)

    def retranslateUi(self, CloneCardTypeDlg):
        CloneCardTypeDlg.setWindowTitle(_('Clone card type'))
        self.label.setText(_('Cloned from:'))
        self.label_2.setText(_('Clone name:'))
        self.OK_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

