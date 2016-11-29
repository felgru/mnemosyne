# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuration_wdgt_sync_server.ui'
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

class Ui_ConfigurationWdgtSyncServer(object):
    def setupUi(self, ConfigurationWdgtSyncServer):
        ConfigurationWdgtSyncServer.setObjectName(_fromUtf8("ConfigurationWdgtSyncServer"))
        ConfigurationWdgtSyncServer.resize(349, 299)
        self.verticalLayout_3 = QtGui.QVBoxLayout(ConfigurationWdgtSyncServer)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.run_sync_server = QtGui.QGroupBox(ConfigurationWdgtSyncServer)
        self.run_sync_server.setCheckable(True)
        self.run_sync_server.setObjectName(_fromUtf8("run_sync_server"))
        self.verticalLayout = QtGui.QVBoxLayout(self.run_sync_server)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.run_sync_server)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.username = QtGui.QLineEdit(self.run_sync_server)
        self.username.setObjectName(_fromUtf8("username"))
        self.gridLayout.addWidget(self.username, 0, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.run_sync_server)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.password = QtGui.QLineEdit(self.run_sync_server)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout.addWidget(self.password, 1, 1, 1, 2)
        self.label_3 = QtGui.QLabel(self.run_sync_server)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.port = QtGui.QSpinBox(self.run_sync_server)
        self.port.setMinimum(1)
        self.port.setMaximum(99999)
        self.port.setObjectName(_fromUtf8("port"))
        self.gridLayout.addWidget(self.port, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.check_for_edited_local_media_files = QtGui.QCheckBox(self.run_sync_server)
        self.check_for_edited_local_media_files.setObjectName(_fromUtf8("check_for_edited_local_media_files"))
        self.verticalLayout.addWidget(self.check_for_edited_local_media_files)
        spacerItem1 = QtGui.QSpacerItem(20, 124, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.server_status = QtGui.QLabel(self.run_sync_server)
        self.server_status.setObjectName(_fromUtf8("server_status"))
        self.verticalLayout.addWidget(self.server_status)
        self.verticalLayout_3.addWidget(self.run_sync_server)

        self.retranslateUi(ConfigurationWdgtSyncServer)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationWdgtSyncServer)

    def retranslateUi(self, ConfigurationWdgtSyncServer):
        ConfigurationWdgtSyncServer.setWindowTitle(_('Form'))
        self.run_sync_server.setTitle(_('Allow other devices to sync with this computer'))
        self.label_2.setText(_('Username:'))
        self.label_4.setText(_('Password:'))
        self.label_3.setText(_('Port:'))
        self.check_for_edited_local_media_files.setText(_('Check for changed media files on server'))
        self.server_status.setText(_('Server status'))

