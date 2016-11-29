# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_dlg.ui'
#
# Created: Mon Apr 15 14:30:23 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ExportDlg(object):
    def setupUi(self, ExportDlg):
        ExportDlg.setObjectName(_fromUtf8("ExportDlg"))
        ExportDlg.resize(293, 175)
        self.vboxlayout = QtGui.QVBoxLayout(ExportDlg)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.textLabel_5 = QtGui.QLabel(ExportDlg)
        self.textLabel_5.setWordWrap(False)
        self.textLabel_5.setObjectName(_fromUtf8("textLabel_5"))
        self.vboxlayout1.addWidget(self.textLabel_5)
        self.file_formats = QtGui.QComboBox(ExportDlg)
        self.file_formats.setEditable(False)
        self.file_formats.setAutoCompletion(True)
        self.file_formats.setDuplicatesEnabled(False)
        self.file_formats.setObjectName(_fromUtf8("file_formats"))
        self.vboxlayout1.addWidget(self.file_formats)
        self.textLabel1 = QtGui.QLabel(ExportDlg)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.vboxlayout1.addWidget(self.textLabel1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.filename_box = QtGui.QLineEdit(ExportDlg)
        self.filename_box.setObjectName(_fromUtf8("filename_box"))
        self.hboxlayout.addWidget(self.filename_box)
        self.browse_button = QtGui.QPushButton(ExportDlg)
        self.browse_button.setAutoDefault(False)
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.hboxlayout.addWidget(self.browse_button)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.label = QtGui.QLabel(ExportDlg)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.vboxlayout1.addWidget(self.label)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.ok_button = QtGui.QPushButton(ExportDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.hboxlayout1.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(201, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(ExportDlg)
        self.cancel_button.setAutoDefault(False)
        self.cancel_button.setDefault(False)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.hboxlayout1.addWidget(self.cancel_button)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(ExportDlg)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportDlg.reject)
        QtCore.QObject.connect(self.browse_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportDlg.browse)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportDlg.accept)
        QtCore.QObject.connect(self.file_formats, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), ExportDlg.file_format_changed)
        QtCore.QMetaObject.connectSlotsByName(ExportDlg)
        ExportDlg.setTabOrder(self.filename_box, self.browse_button)
        ExportDlg.setTabOrder(self.browse_button, self.file_formats)
        ExportDlg.setTabOrder(self.file_formats, self.ok_button)
        ExportDlg.setTabOrder(self.ok_button, self.cancel_button)

    def retranslateUi(self, ExportDlg):
        ExportDlg.setWindowTitle(_('Export to file'))
        self.textLabel_5.setText(_('File format:'))
        self.textLabel1.setText(_('File to export to:'))
        self.browse_button.setText(_('&Browse'))
        self.label.setText(_('(Only active cards will be exported, without learning data.)'))
        self.ok_button.setText(_('&OK'))
        self.ok_button.setShortcut(_('Alt+O'))
        self.cancel_button.setText(_('&Cancel'))

