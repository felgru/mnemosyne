# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_unused_media_files_dlg.ui'
#
# Created: Mon Apr 15 14:30:22 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DeleteUnusedMediaFilesDlg(object):
    def setupUi(self, DeleteUnusedMediaFilesDlg):
        DeleteUnusedMediaFilesDlg.setObjectName(_fromUtf8("DeleteUnusedMediaFilesDlg"))
        DeleteUnusedMediaFilesDlg.resize(388, 263)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DeleteUnusedMediaFilesDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(DeleteUnusedMediaFilesDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.file_list = QtGui.QTextBrowser(DeleteUnusedMediaFilesDlg)
        self.file_list.setObjectName(_fromUtf8("file_list"))
        self.verticalLayout.addWidget(self.file_list)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ok_button = QtGui.QPushButton(DeleteUnusedMediaFilesDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(DeleteUnusedMediaFilesDlg)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DeleteUnusedMediaFilesDlg)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), DeleteUnusedMediaFilesDlg.accept)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), DeleteUnusedMediaFilesDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleteUnusedMediaFilesDlg)

    def retranslateUi(self, DeleteUnusedMediaFilesDlg):
        DeleteUnusedMediaFilesDlg.setWindowTitle(_('Delete media'))
        self.label.setText(_('Delete these unused media files?'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

