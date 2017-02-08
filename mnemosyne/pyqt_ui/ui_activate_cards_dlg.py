# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'activate_cards_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ActivateCardsDlg(object):
    def setupUi(self, ActivateCardsDlg):
        ActivateCardsDlg.setObjectName("ActivateCardsDlg")
        ActivateCardsDlg.resize(593, 156)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ActivateCardsDlg)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(ActivateCardsDlg)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.saved_sets_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.saved_sets_layout.setContentsMargins(0, 0, 0, 0)
        self.saved_sets_layout.setObjectName("saved_sets_layout")
        self.saved_sets_label = QtWidgets.QLabel(self.layoutWidget)
        self.saved_sets_label.setObjectName("saved_sets_label")
        self.saved_sets_layout.addWidget(self.saved_sets_label)
        self.saved_sets = QtWidgets.QListWidget(self.layoutWidget)
        self.saved_sets.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.saved_sets.setObjectName("saved_sets")
        self.saved_sets_layout.addWidget(self.saved_sets)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.criterion_layout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.criterion_layout.setContentsMargins(0, 0, 0, 0)
        self.criterion_layout.setObjectName("criterion_layout")
        self.tab_widget = QtWidgets.QTabWidget(self.layoutWidget1)
        self.tab_widget.setObjectName("tab_widget")
        self.criterion_layout.addWidget(self.tab_widget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ok_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_3.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.save_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.save_button.setAutoDefault(True)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_3.addWidget(self.save_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cancel_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.criterion_layout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.splitter)

        self.retranslateUi(ActivateCardsDlg)
        self.tab_widget.setCurrentIndex(-1)
        self.ok_button.clicked.connect(ActivateCardsDlg.accept)
        self.save_button.clicked.connect(ActivateCardsDlg.save_set)
        self.cancel_button.clicked.connect(ActivateCardsDlg.reject)
        self.saved_sets.itemActivated['QListWidgetItem*'].connect(ActivateCardsDlg.load_set)
        self.saved_sets.customContextMenuRequested['QPoint'].connect(ActivateCardsDlg.saved_sets_custom_menu)
        self.tab_widget.currentChanged['int'].connect(ActivateCardsDlg.change_widget)
        self.saved_sets.currentItemChanged['QListWidgetItem*','QListWidgetItem*'].connect(ActivateCardsDlg.change_set)
        self.saved_sets.itemDoubleClicked['QListWidgetItem*'].connect(ActivateCardsDlg.select_set_and_close)
        QtCore.QMetaObject.connectSlotsByName(ActivateCardsDlg)

    def retranslateUi(self, ActivateCardsDlg):
        _translate = QtCore.QCoreApplication.translate
        ActivateCardsDlg.setWindowTitle(_('(De)activate cards'))
        self.saved_sets_label.setText(_('Saved sets:'))
        self.ok_button.setText(_('&OK'))
        self.save_button.setText(_('&Save this set for later use'))
        self.cancel_button.setText(_('&Cancel'))

