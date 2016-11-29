# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_unused_media_files_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleteUnusedMediaFilesDlg(object):
    def setupUi(self, DeleteUnusedMediaFilesDlg):
        DeleteUnusedMediaFilesDlg.setObjectName("DeleteUnusedMediaFilesDlg")
        DeleteUnusedMediaFilesDlg.resize(388, 263)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DeleteUnusedMediaFilesDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DeleteUnusedMediaFilesDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.file_list = QtWidgets.QTextBrowser(DeleteUnusedMediaFilesDlg)
        self.file_list.setObjectName("file_list")
        self.verticalLayout.addWidget(self.file_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QtWidgets.QPushButton(DeleteUnusedMediaFilesDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(DeleteUnusedMediaFilesDlg)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DeleteUnusedMediaFilesDlg)
        self.ok_button.clicked.connect(DeleteUnusedMediaFilesDlg.accept)
        self.cancel_button.clicked.connect(DeleteUnusedMediaFilesDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleteUnusedMediaFilesDlg)

    def retranslateUi(self, DeleteUnusedMediaFilesDlg):
        _translate = QtCore.QCoreApplication.translate
        DeleteUnusedMediaFilesDlg.setWindowTitle(_('Delete media'))
        self.label.setText(_('Delete these unused media files?'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

