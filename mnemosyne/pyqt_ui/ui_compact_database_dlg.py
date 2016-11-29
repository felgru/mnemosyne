# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compact_database_dlg.ui'
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

class Ui_CompactDatabaseDlg(object):
    def setupUi(self, CompactDatabaseDlg):
        CompactDatabaseDlg.setObjectName(_fromUtf8("CompactDatabaseDlg"))
        CompactDatabaseDlg.resize(263, 88)
        self.verticalLayout_2 = QtGui.QVBoxLayout(CompactDatabaseDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.compact_database = QtGui.QCheckBox(CompactDatabaseDlg)
        self.compact_database.setChecked(True)
        self.compact_database.setObjectName(_fromUtf8("compact_database"))
        self.verticalLayout.addWidget(self.compact_database)
        self.delete_unused_media_files = QtGui.QCheckBox(CompactDatabaseDlg)
        self.delete_unused_media_files.setChecked(True)
        self.delete_unused_media_files.setObjectName(_fromUtf8("delete_unused_media_files"))
        self.verticalLayout.addWidget(self.delete_unused_media_files)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ok_button = QtGui.QPushButton(CompactDatabaseDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(CompactDatabaseDlg)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CompactDatabaseDlg)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), CompactDatabaseDlg.accept)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), CompactDatabaseDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(CompactDatabaseDlg)

    def retranslateUi(self, CompactDatabaseDlg):
        CompactDatabaseDlg.setWindowTitle(_('Compact'))
        self.compact_database.setText(_('Compact database'))
        self.delete_unused_media_files.setText(_('Delete unused media files'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

