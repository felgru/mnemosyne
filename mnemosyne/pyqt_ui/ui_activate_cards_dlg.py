# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'activate_cards_dlg.ui'
#
# Created: Mon Apr 15 14:30:19 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ActivateCardsDlg(object):
    def setupUi(self, ActivateCardsDlg):
        ActivateCardsDlg.setObjectName(_fromUtf8("ActivateCardsDlg"))
        ActivateCardsDlg.resize(593, 148)
        self.verticalLayout_3 = QtGui.QVBoxLayout(ActivateCardsDlg)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(ActivateCardsDlg)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.saved_sets_layout = QtGui.QVBoxLayout(self.layoutWidget)
        self.saved_sets_layout.setMargin(0)
        self.saved_sets_layout.setObjectName(_fromUtf8("saved_sets_layout"))
        self.saved_sets_label = QtGui.QLabel(self.layoutWidget)
        self.saved_sets_label.setObjectName(_fromUtf8("saved_sets_label"))
        self.saved_sets_layout.addWidget(self.saved_sets_label)
        self.saved_sets = QtGui.QListWidget(self.layoutWidget)
        self.saved_sets.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.saved_sets.setObjectName(_fromUtf8("saved_sets"))
        self.saved_sets_layout.addWidget(self.saved_sets)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.criterion_layout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.criterion_layout.setMargin(0)
        self.criterion_layout.setObjectName(_fromUtf8("criterion_layout"))
        self.tab_widget = QtGui.QTabWidget(self.layoutWidget1)
        self.tab_widget.setObjectName(_fromUtf8("tab_widget"))
        self.criterion_layout.addWidget(self.tab_widget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ok_button = QtGui.QPushButton(self.layoutWidget1)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout_3.addWidget(self.ok_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.save_button = QtGui.QPushButton(self.layoutWidget1)
        self.save_button.setAutoDefault(False)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.horizontalLayout_3.addWidget(self.save_button)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cancel_button = QtGui.QPushButton(self.layoutWidget1)
        self.cancel_button.setAutoDefault(False)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.criterion_layout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.splitter)

        self.retranslateUi(ActivateCardsDlg)
        self.tab_widget.setCurrentIndex(-1)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ActivateCardsDlg.accept)
        QtCore.QObject.connect(self.save_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ActivateCardsDlg.save_set)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ActivateCardsDlg.reject)
        QtCore.QObject.connect(self.saved_sets, QtCore.SIGNAL(_fromUtf8("itemActivated(QListWidgetItem*)")), ActivateCardsDlg.load_set)
        QtCore.QObject.connect(self.saved_sets, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), ActivateCardsDlg.saved_sets_custom_menu)
        QtCore.QObject.connect(self.tab_widget, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), ActivateCardsDlg.change_widget)
        QtCore.QObject.connect(self.saved_sets, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), ActivateCardsDlg.change_set)
        QtCore.QObject.connect(self.saved_sets, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), ActivateCardsDlg.select_set_and_close)
        QtCore.QMetaObject.connectSlotsByName(ActivateCardsDlg)

    def retranslateUi(self, ActivateCardsDlg):
        ActivateCardsDlg.setWindowTitle(_('(De)activate cards'))
        self.saved_sets_label.setText(_('Saved sets:'))
        self.ok_button.setText(_('&OK'))
        self.save_button.setText(_('&Save this set for later use'))
        self.cancel_button.setText(_('&Cancel'))

