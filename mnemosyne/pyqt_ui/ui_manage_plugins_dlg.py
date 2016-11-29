# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_plugins_dlg.ui'
#
# Created: Mon Apr 15 14:30:18 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ManagePluginsDlg(object):
    def setupUi(self, ManagePluginsDlg):
        ManagePluginsDlg.setObjectName(_fromUtf8("ManagePluginsDlg"))
        ManagePluginsDlg.resize(382, 488)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ManagePluginsDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ManagePluginsDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.plugin_list = QtGui.QListWidget(ManagePluginsDlg)
        self.plugin_list.setMinimumSize(QtCore.QSize(350, 200))
        self.plugin_list.setObjectName(_fromUtf8("plugin_list"))
        self.verticalLayout.addWidget(self.plugin_list)
        self.label_2 = QtGui.QLabel(ManagePluginsDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.plugin_description = QtGui.QTextBrowser(ManagePluginsDlg)
        self.plugin_description.setMinimumSize(QtCore.QSize(350, 200))
        self.plugin_description.setObjectName(_fromUtf8("plugin_description"))
        self.verticalLayout.addWidget(self.plugin_description)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.ok_button = QtGui.QPushButton(ManagePluginsDlg)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.hboxlayout.addWidget(self.ok_button)
        self.install_button = QtGui.QPushButton(ManagePluginsDlg)
        self.install_button.setObjectName(_fromUtf8("install_button"))
        self.hboxlayout.addWidget(self.install_button)
        self.delete_button = QtGui.QPushButton(ManagePluginsDlg)
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.hboxlayout.addWidget(self.delete_button)
        self.exit_button = QtGui.QPushButton(ManagePluginsDlg)
        self.exit_button.setAutoDefault(False)
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.hboxlayout.addWidget(self.exit_button)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ManagePluginsDlg)
        QtCore.QObject.connect(self.exit_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ManagePluginsDlg.reject)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ManagePluginsDlg.accept)
        QtCore.QObject.connect(self.install_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ManagePluginsDlg.install_plugin)
        QtCore.QObject.connect(self.delete_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ManagePluginsDlg.delete_plugin)
        QtCore.QObject.connect(self.plugin_list, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), ManagePluginsDlg.plugin_selected)
        QtCore.QObject.connect(self.plugin_list, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), ManagePluginsDlg.plugin_selected)
        QtCore.QMetaObject.connectSlotsByName(ManagePluginsDlg)

    def retranslateUi(self, ManagePluginsDlg):
        ManagePluginsDlg.setWindowTitle(_('Manage plugins'))
        self.label.setText(_('Installed plugins (active and inactive):'))
        self.label_2.setText(_('Plugin description:'))
        self.ok_button.setText(_('&OK'))
        self.install_button.setText(_('&Install new plugin'))
        self.delete_button.setText(_('&Delete plugin'))
        self.exit_button.setText(_('E&xit'))

import mnemosyne_rc
