# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename_tag_dlg.ui'
#
# Created: Mon Apr 15 14:30:21 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RenameTagDlg(object):
    def setupUi(self, RenameTagDlg):
        RenameTagDlg.setObjectName(_fromUtf8("RenameTagDlg"))
        RenameTagDlg.resize(366, 82)
        self.verticalLayout_2 = QtGui.QVBoxLayout(RenameTagDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(RenameTagDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tag_name = QtGui.QLineEdit(RenameTagDlg)
        self.tag_name.setObjectName(_fromUtf8("tag_name"))
        self.verticalLayout.addWidget(self.tag_name)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ok_button = QtGui.QPushButton(RenameTagDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(RenameTagDlg)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RenameTagDlg)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), RenameTagDlg.accept)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), RenameTagDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(RenameTagDlg)

    def retranslateUi(self, RenameTagDlg):
        RenameTagDlg.setWindowTitle(_('Rename tag'))
        self.label.setText(_('Enter new tag name:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

