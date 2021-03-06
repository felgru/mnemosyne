# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_card_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditCardDlg(object):
    def setupUi(self, EditCardDlg):
        EditCardDlg.setObjectName("EditCardDlg")
        EditCardDlg.resize(271, 100)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(EditCardDlg)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vbox_layout = QtWidgets.QVBoxLayout()
        self.vbox_layout.setObjectName("vbox_layout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.label_2 = QtWidgets.QLabel(EditCardDlg)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.card_types_widget = QtWidgets.QComboBox(EditCardDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_types_widget.sizePolicy().hasHeightForWidth())
        self.card_types_widget.setSizePolicy(sizePolicy)
        self.card_types_widget.setObjectName("card_types_widget")
        self.gridlayout.addWidget(self.card_types_widget, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(EditCardDlg)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.tags = CompletionComboBox(EditCardDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tags.sizePolicy().hasHeightForWidth())
        self.tags.setSizePolicy(sizePolicy)
        self.tags.setEditable(True)
        self.tags.setObjectName("tags")
        self.gridlayout.addWidget(self.tags, 1, 1, 1, 1)
        self.vbox_layout.addLayout(self.gridlayout)
        self.button_row = QtWidgets.QHBoxLayout()
        self.button_row.setObjectName("button_row")
        self.OK_button = QtWidgets.QPushButton(EditCardDlg)
        self.OK_button.setDefault(True)
        self.OK_button.setObjectName("OK_button")
        self.button_row.addWidget(self.OK_button)
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_row.addItem(spacerItem)
        self.preview_button = QtWidgets.QPushButton(EditCardDlg)
        self.preview_button.setObjectName("preview_button")
        self.button_row.addWidget(self.preview_button)
        spacerItem1 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_row.addItem(spacerItem1)
        self.exit_button = QtWidgets.QPushButton(EditCardDlg)
        self.exit_button.setObjectName("exit_button")
        self.button_row.addWidget(self.exit_button)
        self.vbox_layout.addLayout(self.button_row)
        self.horizontalLayout_2.addLayout(self.vbox_layout)

        self.retranslateUi(EditCardDlg)
        self.preview_button.clicked.connect(EditCardDlg.preview)
        self.OK_button.clicked.connect(EditCardDlg.accept)
        self.exit_button.clicked.connect(EditCardDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(EditCardDlg)

    def retranslateUi(self, EditCardDlg):
        _translate = QtCore.QCoreApplication.translate
        EditCardDlg.setWindowTitle(_('Edit card'))
        self.label_2.setText(_('Card type:'))
        self.label.setText(_('Tags:'))
        self.OK_button.setText(_('&OK'))
        self.preview_button.setText(_('&Preview'))
        self.exit_button.setText(_('&Exit'))

from mnemosyne.pyqt_ui.completion_combo_box import CompletionComboBox
from . import mnemosyne_rc
