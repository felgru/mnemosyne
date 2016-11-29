# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_metadata_dlg.ui'
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

class Ui_ExportMetadataDlg(object):
    def setupUi(self, ExportMetadataDlg):
        ExportMetadataDlg.setObjectName(_fromUtf8("ExportMetadataDlg"))
        ExportMetadataDlg.resize(455, 433)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ExportMetadataDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(ExportMetadataDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.card_set_name = QtGui.QLineEdit(ExportMetadataDlg)
        self.card_set_name.setObjectName(_fromUtf8("card_set_name"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.card_set_name)
        self.label_2 = QtGui.QLabel(ExportMetadataDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.author_name = QtGui.QLineEdit(ExportMetadataDlg)
        self.author_name.setObjectName(_fromUtf8("author_name"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.author_name)
        self.label_3 = QtGui.QLabel(ExportMetadataDlg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(ExportMetadataDlg)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.date = QtGui.QDateEdit(ExportMetadataDlg)
        self.date.setObjectName(_fromUtf8("date"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.date)
        self.label_5 = QtGui.QLabel(ExportMetadataDlg)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.revision = QtGui.QSpinBox(ExportMetadataDlg)
        self.revision.setMinimum(1)
        self.revision.setMaximum(9999)
        self.revision.setObjectName(_fromUtf8("revision"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.revision)
        self.author_email = QtGui.QLineEdit(ExportMetadataDlg)
        self.author_email.setObjectName(_fromUtf8("author_email"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.author_email)
        self.tags = QtGui.QLineEdit(ExportMetadataDlg)
        self.tags.setObjectName(_fromUtf8("tags"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.tags)
        self.label_7 = QtGui.QLabel(ExportMetadataDlg)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_7)
        self.verticalLayout.addLayout(self.formLayout)
        self.label_6 = QtGui.QLabel(ExportMetadataDlg)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.notes = QtGui.QPlainTextEdit(ExportMetadataDlg)
        self.notes.setObjectName(_fromUtf8("notes"))
        self.verticalLayout.addWidget(self.notes)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ok_button = QtGui.QPushButton(ExportMetadataDlg)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ExportMetadataDlg)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportMetadataDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(ExportMetadataDlg)
        ExportMetadataDlg.setTabOrder(self.card_set_name, self.author_name)
        ExportMetadataDlg.setTabOrder(self.author_name, self.author_email)
        ExportMetadataDlg.setTabOrder(self.author_email, self.tags)
        ExportMetadataDlg.setTabOrder(self.tags, self.date)
        ExportMetadataDlg.setTabOrder(self.date, self.revision)
        ExportMetadataDlg.setTabOrder(self.revision, self.notes)
        ExportMetadataDlg.setTabOrder(self.notes, self.ok_button)

    def retranslateUi(self, ExportMetadataDlg):
        ExportMetadataDlg.setWindowTitle(_('Export cards'))
        self.label.setText(_('Card set name:'))
        self.label_2.setText(_('Author name:'))
        self.label_3.setText(_('Author email:'))
        self.label_4.setText(_('Date:'))
        self.label_5.setText(_('Revision:'))
        self.label_7.setText(_('Tags:'))
        self.label_6.setText(_('Notes:'))
        self.ok_button.setText(_('&OK'))

