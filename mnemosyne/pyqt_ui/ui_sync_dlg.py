# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sync_dlg.ui'
#
# Created: Mon Apr 15 14:30:20 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SyncDlg(object):
    def setupUi(self, SyncDlg):
        SyncDlg.setObjectName(_fromUtf8("SyncDlg"))
        SyncDlg.resize(337, 152)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SyncDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(SyncDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.server = QtGui.QLineEdit(SyncDlg)
        self.server.setMinimumSize(QtCore.QSize(140, 0))
        self.server.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.server.setObjectName(_fromUtf8("server"))
        self.gridLayout.addWidget(self.server, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(SyncDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.username = QtGui.QLineEdit(SyncDlg)
        self.username.setObjectName(_fromUtf8("username"))
        self.gridLayout.addWidget(self.username, 1, 1, 1, 5)
        self.label_4 = QtGui.QLabel(SyncDlg)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.password = QtGui.QLineEdit(SyncDlg)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout.addWidget(self.password, 2, 1, 1, 5)
        self.label_3 = QtGui.QLabel(SyncDlg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.port = QtGui.QSpinBox(SyncDlg)
        self.port.setMinimum(1)
        self.port.setMaximum(99999)
        self.port.setObjectName(_fromUtf8("port"))
        self.gridLayout.addWidget(self.port, 0, 4, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.check_for_edited_local_media_files = QtGui.QCheckBox(SyncDlg)
        self.check_for_edited_local_media_files.setObjectName(_fromUtf8("check_for_edited_local_media_files"))
        self.verticalLayout.addWidget(self.check_for_edited_local_media_files)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ok_button = QtGui.QPushButton(SyncDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(SyncDlg)
        self.cancel_button.setAutoDefault(False)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SyncDlg)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), SyncDlg.accept)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), SyncDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(SyncDlg)

    def retranslateUi(self, SyncDlg):
        SyncDlg.setWindowTitle(_('Sync with server'))
        self.label.setText(_('Server:'))
        self.label_2.setText(_('Username:'))
        self.label_4.setText(_('Password:'))
        self.label_3.setText(_('Port:'))
        self.check_for_edited_local_media_files.setText(_('Check for changed media files on client'))
        self.ok_button.setText(_('&OK'))
        self.cancel_button.setText(_('&Cancel'))

