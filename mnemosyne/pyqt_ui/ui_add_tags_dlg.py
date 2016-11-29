# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_tags_dlg.ui'
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

class Ui_AddTagsDlg(object):
    def setupUi(self, AddTagsDlg):
        AddTagsDlg.setObjectName(_fromUtf8("AddTagsDlg"))
        AddTagsDlg.resize(274, 65)
        self.verticalLayout_2 = QtGui.QVBoxLayout(AddTagsDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(AddTagsDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.tags = QtGui.QComboBox(AddTagsDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tags.sizePolicy().hasHeightForWidth())
        self.tags.setSizePolicy(sizePolicy)
        self.tags.setEditable(True)
        self.tags.setObjectName(_fromUtf8("tags"))
        self.horizontalLayout.addWidget(self.tags)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.ok_button = QtGui.QPushButton(AddTagsDlg)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.hboxlayout.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(101, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(AddTagsDlg)
        self.cancel_button.setAutoDefault(False)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.hboxlayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(AddTagsDlg)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), AddTagsDlg.reject)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), AddTagsDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(AddTagsDlg)

    def retranslateUi(self, AddTagsDlg):
        AddTagsDlg.setWindowTitle(_('Add tags'))
        self.label.setText(_('Tags:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

import mnemosyne_rc
