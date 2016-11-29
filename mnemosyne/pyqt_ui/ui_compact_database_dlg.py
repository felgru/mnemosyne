# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compact_database_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CompactDatabaseDlg(object):
    def setupUi(self, CompactDatabaseDlg):
        CompactDatabaseDlg.setObjectName("CompactDatabaseDlg")
        CompactDatabaseDlg.resize(398, 133)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CompactDatabaseDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.delete_unused_media_files = QtWidgets.QCheckBox(CompactDatabaseDlg)
        self.delete_unused_media_files.setChecked(True)
        self.delete_unused_media_files.setObjectName("delete_unused_media_files")
        self.verticalLayout.addWidget(self.delete_unused_media_files)
        self.archive_old_logs = QtWidgets.QCheckBox(CompactDatabaseDlg)
        self.archive_old_logs.setChecked(True)
        self.archive_old_logs.setObjectName("archive_old_logs")
        self.verticalLayout.addWidget(self.archive_old_logs)
        self.defragment_database = QtWidgets.QCheckBox(CompactDatabaseDlg)
        self.defragment_database.setChecked(True)
        self.defragment_database.setObjectName("defragment_database")
        self.verticalLayout.addWidget(self.defragment_database)
        self.label = QtWidgets.QLabel(CompactDatabaseDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QtWidgets.QPushButton(CompactDatabaseDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(CompactDatabaseDlg)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CompactDatabaseDlg)
        self.ok_button.clicked.connect(CompactDatabaseDlg.accept)
        self.cancel_button.clicked.connect(CompactDatabaseDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(CompactDatabaseDlg)

    def retranslateUi(self, CompactDatabaseDlg):
        _translate = QtCore.QCoreApplication.translate
        CompactDatabaseDlg.setWindowTitle(_('Compact database'))
        self.delete_unused_media_files.setText(_('Delete unused media files'))
        self.archive_old_logs.setText(_('Archive statistics older than 1 year'))
        self.defragment_database.setText(_('Defragment database (only needed after deleting many cards)'))
        self.label.setText(_('(Note: archiving and defragmenting happens automatically every few months.)'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

