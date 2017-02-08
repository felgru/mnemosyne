# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExportDlg(object):
    def setupUi(self, ExportDlg):
        ExportDlg.setObjectName("ExportDlg")
        ExportDlg.resize(293, 175)
        self.vboxlayout = QtWidgets.QVBoxLayout(ExportDlg)
        self.vboxlayout.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.textLabel_5 = QtWidgets.QLabel(ExportDlg)
        self.textLabel_5.setWordWrap(False)
        self.textLabel_5.setObjectName("textLabel_5")
        self.vboxlayout1.addWidget(self.textLabel_5)
        self.file_formats = QtWidgets.QComboBox(ExportDlg)
        self.file_formats.setEditable(False)
        self.file_formats.setDuplicatesEnabled(False)
        self.file_formats.setObjectName("file_formats")
        self.vboxlayout1.addWidget(self.file_formats)
        self.textLabel1 = QtWidgets.QLabel(ExportDlg)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.vboxlayout1.addWidget(self.textLabel1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(11, 11, 11, 11)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.filename_box = QtWidgets.QLineEdit(ExportDlg)
        self.filename_box.setObjectName("filename_box")
        self.hboxlayout.addWidget(self.filename_box)
        self.browse_button = QtWidgets.QPushButton(ExportDlg)
        self.browse_button.setObjectName("browse_button")
        self.hboxlayout.addWidget(self.browse_button)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.label = QtWidgets.QLabel(ExportDlg)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.vboxlayout1.addWidget(self.label)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(11, 11, 11, 11)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.ok_button = QtWidgets.QPushButton(ExportDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.hboxlayout1.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(201, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(ExportDlg)
        self.cancel_button.setDefault(False)
        self.cancel_button.setObjectName("cancel_button")
        self.hboxlayout1.addWidget(self.cancel_button)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(ExportDlg)
        self.cancel_button.clicked.connect(ExportDlg.reject)
        self.browse_button.clicked.connect(ExportDlg.browse)
        self.ok_button.clicked.connect(ExportDlg.accept)
        self.file_formats.currentIndexChanged['int'].connect(ExportDlg.file_format_changed)
        QtCore.QMetaObject.connectSlotsByName(ExportDlg)
        ExportDlg.setTabOrder(self.filename_box, self.browse_button)
        ExportDlg.setTabOrder(self.browse_button, self.file_formats)
        ExportDlg.setTabOrder(self.file_formats, self.ok_button)
        ExportDlg.setTabOrder(self.ok_button, self.cancel_button)

    def retranslateUi(self, ExportDlg):
        _translate = QtCore.QCoreApplication.translate
        ExportDlg.setWindowTitle(_('Export to file'))
        self.textLabel_5.setText(_('File format:'))
        self.textLabel1.setText(_('File to export to:'))
        self.browse_button.setText(_('&Browse'))
        self.label.setText(_('(Only active cards will be exported, without learning data.)'))
        self.ok_button.setText(_('&OK'))
        self.ok_button.setShortcut(_('Alt+O'))
        self.cancel_button.setText(_('&Cancel'))

