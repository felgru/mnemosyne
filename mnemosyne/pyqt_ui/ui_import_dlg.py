# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_dlg.ui'
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

class Ui_ImportDlg(object):
    def setupUi(self, ImportDlg):
        ImportDlg.setObjectName(_fromUtf8("ImportDlg"))
        ImportDlg.resize(292, 192)
        self.gridLayout = QtGui.QGridLayout(ImportDlg)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.textLabel_5 = QtGui.QLabel(ImportDlg)
        self.textLabel_5.setWordWrap(False)
        self.textLabel_5.setObjectName(_fromUtf8("textLabel_5"))
        self.vboxlayout.addWidget(self.textLabel_5)
        self.file_formats = QtGui.QComboBox(ImportDlg)
        self.file_formats.setEditable(False)
        self.file_formats.setAutoCompletion(True)
        self.file_formats.setDuplicatesEnabled(False)
        self.file_formats.setObjectName(_fromUtf8("file_formats"))
        self.vboxlayout.addWidget(self.file_formats)
        self.textLabel1 = QtGui.QLabel(ImportDlg)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.vboxlayout.addWidget(self.textLabel1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.filename_box = QtGui.QLineEdit(ImportDlg)
        self.filename_box.setObjectName(_fromUtf8("filename_box"))
        self.hboxlayout.addWidget(self.filename_box)
        self.browse_button = QtGui.QPushButton(ImportDlg)
        self.browse_button.setAutoDefault(False)
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.hboxlayout.addWidget(self.browse_button)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.textLabel2 = QtGui.QLabel(ImportDlg)
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.vboxlayout.addWidget(self.textLabel2)
        self.tags = QtGui.QComboBox(ImportDlg)
        self.tags.setEditable(True)
        self.tags.setAutoCompletion(True)
        self.tags.setDuplicatesEnabled(False)
        self.tags.setObjectName(_fromUtf8("tags"))
        self.vboxlayout.addWidget(self.tags)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.ok_button = QtGui.QPushButton(ImportDlg)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.hboxlayout1.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(201, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(ImportDlg)
        self.cancel_button.setAutoDefault(False)
        self.cancel_button.setDefault(False)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.hboxlayout1.addWidget(self.cancel_button)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.gridLayout.addLayout(self.vboxlayout, 0, 0, 1, 1)

        self.retranslateUi(ImportDlg)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ImportDlg.reject)
        QtCore.QObject.connect(self.browse_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ImportDlg.browse)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ImportDlg.accept)
        QtCore.QObject.connect(self.file_formats, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), ImportDlg.file_format_changed)
        QtCore.QMetaObject.connectSlotsByName(ImportDlg)
        ImportDlg.setTabOrder(self.filename_box, self.browse_button)
        ImportDlg.setTabOrder(self.browse_button, self.file_formats)
        ImportDlg.setTabOrder(self.file_formats, self.tags)
        ImportDlg.setTabOrder(self.tags, self.ok_button)
        ImportDlg.setTabOrder(self.ok_button, self.cancel_button)

    def retranslateUi(self, ImportDlg):
        ImportDlg.setWindowTitle(_('Import from file'))
        self.textLabel_5.setText(_('File format:'))
        self.textLabel1.setText(_('File to import from:'))
        self.browse_button.setText(_('&Browse'))
        self.textLabel2.setText(_('Add additional tag(s) to cards:'))
        self.ok_button.setText(_('&OK'))
        self.ok_button.setShortcut(_('Alt+O'))
        self.cancel_button.setText(_('&Cancel'))

