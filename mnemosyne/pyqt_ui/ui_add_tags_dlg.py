# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_tags_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddTagsDlg(object):
    def setupUi(self, AddTagsDlg):
        AddTagsDlg.setObjectName("AddTagsDlg")
        AddTagsDlg.resize(274, 65)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AddTagsDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(AddTagsDlg)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.tags = CompletionComboBox(AddTagsDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tags.sizePolicy().hasHeightForWidth())
        self.tags.setSizePolicy(sizePolicy)
        self.tags.setEditable(True)
        self.tags.setObjectName("tags")
        self.horizontalLayout.addWidget(self.tags)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.ok_button = QtWidgets.QPushButton(AddTagsDlg)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.hboxlayout.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(101, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(AddTagsDlg)
        self.cancel_button.setAutoDefault(False)
        self.cancel_button.setObjectName("cancel_button")
        self.hboxlayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(AddTagsDlg)
        self.cancel_button.clicked.connect(AddTagsDlg.reject)
        self.ok_button.clicked.connect(AddTagsDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(AddTagsDlg)

    def retranslateUi(self, AddTagsDlg):
        _translate = QtCore.QCoreApplication.translate
        AddTagsDlg.setWindowTitle(_('Add tags'))
        self.label.setText(_('Tags:'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

from mnemosyne.pyqt_ui.completion_combo_box import CompletionComboBox
from . import mnemosyne_rc
