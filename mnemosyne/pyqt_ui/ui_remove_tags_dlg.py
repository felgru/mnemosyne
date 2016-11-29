# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remove_tags_dlg.ui'
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

class Ui_RemoveTagsDlg(object):
    def setupUi(self, RemoveTagsDlg):
        RemoveTagsDlg.setObjectName(_fromUtf8("RemoveTagsDlg"))
        RemoveTagsDlg.resize(257, 260)
        self.verticalLayout_2 = QtGui.QVBoxLayout(RemoveTagsDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(RemoveTagsDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tag_list = QtGui.QListWidget(RemoveTagsDlg)
        self.tag_list.setObjectName(_fromUtf8("tag_list"))
        self.verticalLayout.addWidget(self.tag_list)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.ok_button = QtGui.QPushButton(RemoveTagsDlg)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.hboxlayout.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(101, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(RemoveTagsDlg)
        self.cancel_button.setAutoDefault(False)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.hboxlayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RemoveTagsDlg)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), RemoveTagsDlg.reject)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), RemoveTagsDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(RemoveTagsDlg)

    def retranslateUi(self, RemoveTagsDlg):
        RemoveTagsDlg.setWindowTitle(_('Remove tags'))
        self.label.setText(_('Tags to remove:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

import mnemosyne_rc
