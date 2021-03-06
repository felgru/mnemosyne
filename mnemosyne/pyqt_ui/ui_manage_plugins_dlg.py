# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_plugins_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManagePluginsDlg(object):
    def setupUi(self, ManagePluginsDlg):
        ManagePluginsDlg.setObjectName("ManagePluginsDlg")
        ManagePluginsDlg.resize(382, 495)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ManagePluginsDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ManagePluginsDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plugin_list = QtWidgets.QListWidget(ManagePluginsDlg)
        self.plugin_list.setMinimumSize(QtCore.QSize(350, 200))
        self.plugin_list.setObjectName("plugin_list")
        self.verticalLayout.addWidget(self.plugin_list)
        self.label_2 = QtWidgets.QLabel(ManagePluginsDlg)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.plugin_description = QtWidgets.QTextBrowser(ManagePluginsDlg)
        self.plugin_description.setMinimumSize(QtCore.QSize(350, 200))
        self.plugin_description.setObjectName("plugin_description")
        self.verticalLayout.addWidget(self.plugin_description)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.ok_button = QtWidgets.QPushButton(ManagePluginsDlg)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.hboxlayout.addWidget(self.ok_button)
        self.install_button = QtWidgets.QPushButton(ManagePluginsDlg)
        self.install_button.setObjectName("install_button")
        self.hboxlayout.addWidget(self.install_button)
        self.delete_button = QtWidgets.QPushButton(ManagePluginsDlg)
        self.delete_button.setObjectName("delete_button")
        self.hboxlayout.addWidget(self.delete_button)
        self.exit_button = QtWidgets.QPushButton(ManagePluginsDlg)
        self.exit_button.setObjectName("exit_button")
        self.hboxlayout.addWidget(self.exit_button)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ManagePluginsDlg)
        self.exit_button.clicked.connect(ManagePluginsDlg.reject)
        self.ok_button.clicked.connect(ManagePluginsDlg.accept)
        self.install_button.clicked.connect(ManagePluginsDlg.install_plugin)
        self.delete_button.clicked.connect(ManagePluginsDlg.delete_plugin)
        self.plugin_list.currentItemChanged['QListWidgetItem*','QListWidgetItem*'].connect(ManagePluginsDlg.plugin_selected)
        self.plugin_list.itemClicked['QListWidgetItem*'].connect(ManagePluginsDlg.plugin_selected)
        QtCore.QMetaObject.connectSlotsByName(ManagePluginsDlg)

    def retranslateUi(self, ManagePluginsDlg):
        _translate = QtCore.QCoreApplication.translate
        ManagePluginsDlg.setWindowTitle(_('Manage plugins'))
        self.label.setText(_('Installed plugins (active and inactive):'))
        self.label_2.setText(_('Plugin description:'))
        self.ok_button.setText(_('&OK'))
        self.install_button.setText(_('&Install new plugin'))
        self.delete_button.setText(_('&Delete plugin'))
        self.exit_button.setText(_('E&xit'))

from . import mnemosyne_rc
