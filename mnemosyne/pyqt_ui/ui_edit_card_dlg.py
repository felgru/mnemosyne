# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_card_dlg.ui'
#
# Created: Mon Apr 15 14:30:17 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditCardDlg(object):
    def setupUi(self, EditCardDlg):
        EditCardDlg.setObjectName(_fromUtf8("EditCardDlg"))
        EditCardDlg.resize(209, 100)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(EditCardDlg)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.vbox_layout = QtGui.QVBoxLayout()
        self.vbox_layout.setObjectName(_fromUtf8("vbox_layout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_2 = QtGui.QLabel(EditCardDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.card_types_widget = QtGui.QComboBox(EditCardDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_types_widget.sizePolicy().hasHeightForWidth())
        self.card_types_widget.setSizePolicy(sizePolicy)
        self.card_types_widget.setObjectName(_fromUtf8("card_types_widget"))
        self.gridlayout.addWidget(self.card_types_widget, 0, 1, 1, 1)
        self.label = QtGui.QLabel(EditCardDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.tags = QtGui.QComboBox(EditCardDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tags.sizePolicy().hasHeightForWidth())
        self.tags.setSizePolicy(sizePolicy)
        self.tags.setEditable(True)
        self.tags.setObjectName(_fromUtf8("tags"))
        self.gridlayout.addWidget(self.tags, 1, 1, 1, 1)
        self.vbox_layout.addLayout(self.gridlayout)
        self.button_row = QtGui.QHBoxLayout()
        self.button_row.setObjectName(_fromUtf8("button_row"))
        self.OK_button = QtGui.QPushButton(EditCardDlg)
        self.OK_button.setDefault(True)
        self.OK_button.setObjectName(_fromUtf8("OK_button"))
        self.button_row.addWidget(self.OK_button)
        spacerItem = QtGui.QSpacerItem(70, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.button_row.addItem(spacerItem)
        self.preview_button = QtGui.QPushButton(EditCardDlg)
        self.preview_button.setAutoDefault(False)
        self.preview_button.setObjectName(_fromUtf8("preview_button"))
        self.button_row.addWidget(self.preview_button)
        spacerItem1 = QtGui.QSpacerItem(70, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.button_row.addItem(spacerItem1)
        self.exit_button = QtGui.QPushButton(EditCardDlg)
        self.exit_button.setAutoDefault(False)
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.button_row.addWidget(self.exit_button)
        self.vbox_layout.addLayout(self.button_row)
        self.horizontalLayout_2.addLayout(self.vbox_layout)

        self.retranslateUi(EditCardDlg)
        QtCore.QObject.connect(self.preview_button, QtCore.SIGNAL(_fromUtf8("clicked()")), EditCardDlg.preview)
        QtCore.QObject.connect(self.OK_button, QtCore.SIGNAL(_fromUtf8("clicked()")), EditCardDlg.accept)
        QtCore.QObject.connect(self.exit_button, QtCore.SIGNAL(_fromUtf8("clicked()")), EditCardDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(EditCardDlg)

    def retranslateUi(self, EditCardDlg):
        EditCardDlg.setWindowTitle(_('Edit card'))
        self.label_2.setText(_('Card type:'))
        self.label.setText(_('Tags:'))
        self.OK_button.setText(_('&OK'))
        self.preview_button.setText(_('&Preview'))
        self.exit_button.setText(_('&Exit'))

import mnemosyne_rc
