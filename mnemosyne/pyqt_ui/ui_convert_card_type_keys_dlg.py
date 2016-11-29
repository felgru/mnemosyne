# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert_card_type_keys_dlg.ui'
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

class Ui_ConvertCardTypeKeysDlg(object):
    def setupUi(self, ConvertCardTypeKeysDlg):
        ConvertCardTypeKeysDlg.setObjectName(_fromUtf8("ConvertCardTypeKeysDlg"))
        ConvertCardTypeKeysDlg.resize(260, 105)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ConvertCardTypeKeysDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(ConvertCardTypeKeysDlg)
        self.label_2.setMinimumSize(QtCore.QSize(250, 40))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(ConvertCardTypeKeysDlg)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(ConvertCardTypeKeysDlg)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ok_button = QtGui.QPushButton(ConvertCardTypeKeysDlg)
        self.ok_button.setEnabled(False)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(208, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(ConvertCardTypeKeysDlg)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ConvertCardTypeKeysDlg)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ConvertCardTypeKeysDlg.accept)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ConvertCardTypeKeysDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ConvertCardTypeKeysDlg)

    def retranslateUi(self, ConvertCardTypeKeysDlg):
        ConvertCardTypeKeysDlg.setWindowTitle(_('Convert card type data'))
        self.label_2.setText(_('Set the correspondence between data in the old and the new card type:'))
        self.label.setText(_('Old:'))
        self.label_3.setText(_('New:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

