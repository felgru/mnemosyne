# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sync_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SyncDlg(object):
    def setupUi(self, SyncDlg):
        SyncDlg.setObjectName("SyncDlg")
        SyncDlg.resize(337, 152)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SyncDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(SyncDlg)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.server = QtWidgets.QLineEdit(SyncDlg)
        self.server.setMinimumSize(QtCore.QSize(140, 0))
        self.server.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.server.setObjectName("server")
        self.gridLayout.addWidget(self.server, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(SyncDlg)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(SyncDlg)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 1, 1, 1, 5)
        self.label_4 = QtWidgets.QLabel(SyncDlg)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(SyncDlg)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 2, 1, 1, 5)
        self.label_3 = QtWidgets.QLabel(SyncDlg)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.port = QtWidgets.QSpinBox(SyncDlg)
        self.port.setMinimum(1)
        self.port.setMaximum(99999)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 0, 4, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.check_for_edited_local_media_files = QtWidgets.QCheckBox(SyncDlg)
        self.check_for_edited_local_media_files.setObjectName("check_for_edited_local_media_files")
        self.verticalLayout.addWidget(self.check_for_edited_local_media_files)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QtWidgets.QPushButton(SyncDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(SyncDlg)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SyncDlg)
        self.ok_button.clicked.connect(SyncDlg.accept)
        self.cancel_button.clicked.connect(SyncDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(SyncDlg)

    def retranslateUi(self, SyncDlg):
        _translate = QtCore.QCoreApplication.translate
        SyncDlg.setWindowTitle(_('Sync with server'))
        self.label.setText(_('Server:'))
        self.label_2.setText(_('Username:'))
        self.label_4.setText(_('Password:'))
        self.label_3.setText(_('Port:'))
        self.check_for_edited_local_media_files.setText(_('Check for changed media files on client'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

