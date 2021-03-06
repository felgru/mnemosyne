# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuration_wdgt_servers.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigurationWdgtServers(object):
    def setupUi(self, ConfigurationWdgtServers):
        ConfigurationWdgtServers.setObjectName("ConfigurationWdgtServers")
        ConfigurationWdgtServers.resize(426, 352)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(ConfigurationWdgtServers)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.run_sync_server = QtWidgets.QGroupBox(ConfigurationWdgtServers)
        self.run_sync_server.setCheckable(True)
        self.run_sync_server.setObjectName("run_sync_server")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.run_sync_server)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.username = QtWidgets.QLineEdit(self.run_sync_server)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.run_sync_server)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.run_sync_server)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.run_sync_server)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.run_sync_server)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.sync_port = QtWidgets.QSpinBox(self.run_sync_server)
        self.sync_port.setMinimum(1)
        self.sync_port.setMaximum(99999)
        self.sync_port.setObjectName("sync_port")
        self.gridLayout.addWidget(self.sync_port, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.check_for_edited_local_media_files = QtWidgets.QCheckBox(self.run_sync_server)
        self.check_for_edited_local_media_files.setObjectName("check_for_edited_local_media_files")
        self.verticalLayout.addWidget(self.check_for_edited_local_media_files)
        self.sync_server_status = QtWidgets.QLabel(self.run_sync_server)
        self.sync_server_status.setObjectName("sync_server_status")
        self.verticalLayout.addWidget(self.sync_server_status)
        self.verticalLayout_3.addWidget(self.run_sync_server)
        self.run_web_server = QtWidgets.QGroupBox(ConfigurationWdgtServers)
        self.run_web_server.setCheckable(True)
        self.run_web_server.setObjectName("run_web_server")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.run_web_server)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.run_web_server)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.web_port = QtWidgets.QSpinBox(self.run_web_server)
        self.web_port.setMinimum(1)
        self.web_port.setMaximum(99999)
        self.web_port.setObjectName("web_port")
        self.horizontalLayout.addWidget(self.web_port)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.web_server_status = QtWidgets.QLabel(self.run_web_server)
        self.web_server_status.setObjectName("web_server_status")
        self.verticalLayout_2.addWidget(self.web_server_status)
        spacerItem2 = QtWidgets.QSpacerItem(271, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.run_web_server)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(ConfigurationWdgtServers)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationWdgtServers)

    def retranslateUi(self, ConfigurationWdgtServers):
        _translate = QtCore.QCoreApplication.translate
        ConfigurationWdgtServers.setWindowTitle(_('Form'))
        self.run_sync_server.setTitle(_('Allow other devices to sync with this computer'))
        self.label_4.setText(_('Password:'))
        self.label_2.setText(_('Username:'))
        self.label_3.setText(_('Port:'))
        self.check_for_edited_local_media_files.setText(_('Check for changed media files on server'))
        self.sync_server_status.setText(_('Sync server status'))
        self.run_web_server.setTitle(_('Allow remote review through a web browser'))
        self.label_5.setText(_('Port:         '))
        self.web_server_status.setText(_('Web server status'))

