# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_card_type_dlg.ui'
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

class Ui_ChangeCardTypeDlg(object):
    def setupUi(self, ChangeCardTypeDlg):
        ChangeCardTypeDlg.setObjectName(_fromUtf8("ChangeCardTypeDlg"))
        ChangeCardTypeDlg.resize(384, 68)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ChangeCardTypeDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(ChangeCardTypeDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.card_types_widget = QtGui.QComboBox(ChangeCardTypeDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_types_widget.sizePolicy().hasHeightForWidth())
        self.card_types_widget.setSizePolicy(sizePolicy)
        self.card_types_widget.setObjectName(_fromUtf8("card_types_widget"))
        self.horizontalLayout.addWidget(self.card_types_widget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ok_button = QtGui.QPushButton(ChangeCardTypeDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout_2.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(ChangeCardTypeDlg)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ChangeCardTypeDlg)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ChangeCardTypeDlg.accept)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ChangeCardTypeDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangeCardTypeDlg)

    def retranslateUi(self, ChangeCardTypeDlg):
        ChangeCardTypeDlg.setWindowTitle(_('Change card type'))
        self.label.setText(_('New card type:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

