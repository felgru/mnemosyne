# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_cards_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddCardsDlg(object):
    def setupUi(self, AddCardsDlg):
        AddCardsDlg.setObjectName("AddCardsDlg")
        AddCardsDlg.resize(450, 170)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(AddCardsDlg)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vbox_layout = QtWidgets.QVBoxLayout()
        self.vbox_layout.setObjectName("vbox_layout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.label_2 = QtWidgets.QLabel(AddCardsDlg)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.card_types_widget = QtWidgets.QComboBox(AddCardsDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_types_widget.sizePolicy().hasHeightForWidth())
        self.card_types_widget.setSizePolicy(sizePolicy)
        self.card_types_widget.setObjectName("card_types_widget")
        self.gridlayout.addWidget(self.card_types_widget, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(AddCardsDlg)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.tags = CompletionComboBox(AddCardsDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tags.sizePolicy().hasHeightForWidth())
        self.tags.setSizePolicy(sizePolicy)
        self.tags.setEditable(True)
        self.tags.setObjectName("tags")
        self.gridlayout.addWidget(self.tags, 1, 1, 1, 1)
        self.vbox_layout.addLayout(self.gridlayout)
        self.grade_buttons = QtWidgets.QGroupBox(AddCardsDlg)
        self.grade_buttons.setObjectName("grade_buttons")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.grade_buttons)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.yet_to_learn_button = QtWidgets.QPushButton(self.grade_buttons)
        self.yet_to_learn_button.setAutoDefault(True)
        self.yet_to_learn_button.setDefault(True)
        self.yet_to_learn_button.setObjectName("yet_to_learn_button")
        self.hboxlayout.addWidget(self.yet_to_learn_button)
        self.line = QtWidgets.QFrame(self.grade_buttons)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hboxlayout.addWidget(self.line)
        self.grade_2_button = QtWidgets.QPushButton(self.grade_buttons)
        self.grade_2_button.setObjectName("grade_2_button")
        self.hboxlayout.addWidget(self.grade_2_button)
        self.grade_3_button = QtWidgets.QPushButton(self.grade_buttons)
        self.grade_3_button.setAutoDefault(True)
        self.grade_3_button.setObjectName("grade_3_button")
        self.hboxlayout.addWidget(self.grade_3_button)
        self.grade_4_button = QtWidgets.QPushButton(self.grade_buttons)
        self.grade_4_button.setAutoDefault(True)
        self.grade_4_button.setObjectName("grade_4_button")
        self.hboxlayout.addWidget(self.grade_4_button)
        self.grade_5_button = QtWidgets.QPushButton(self.grade_buttons)
        self.grade_5_button.setAutoDefault(True)
        self.grade_5_button.setObjectName("grade_5_button")
        self.hboxlayout.addWidget(self.grade_5_button)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.vbox_layout.addWidget(self.grade_buttons)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.preview_button = QtWidgets.QPushButton(AddCardsDlg)
        self.preview_button.setAutoDefault(True)
        self.preview_button.setObjectName("preview_button")
        self.hboxlayout1.addWidget(self.preview_button)
        spacerItem = QtWidgets.QSpacerItem(101, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.exit_button = QtWidgets.QPushButton(AddCardsDlg)
        self.exit_button.setObjectName("exit_button")
        self.hboxlayout1.addWidget(self.exit_button)
        self.vbox_layout.addLayout(self.hboxlayout1)
        self.horizontalLayout_2.addLayout(self.vbox_layout)

        self.retranslateUi(AddCardsDlg)
        self.exit_button.clicked.connect(AddCardsDlg.reject)
        self.preview_button.clicked.connect(AddCardsDlg.preview)
        QtCore.QMetaObject.connectSlotsByName(AddCardsDlg)

    def retranslateUi(self, AddCardsDlg):
        _translate = QtCore.QCoreApplication.translate
        AddCardsDlg.setWindowTitle(_('Add cards'))
        self.label_2.setText(_('Card type:'))
        self.label.setText(_('Tags:'))
        self.grade_buttons.setTitle(_('Select initial grade:'))
        self.yet_to_learn_button.setToolTip(_('You have yet to learn this.'))
        self.yet_to_learn_button.setText(_('&Yet to learn'))
        self.grade_2_button.setToolTip(_('You know this, but just barely.'))
        self.grade_2_button.setText(_('&2'))
        self.grade_3_button.setToolTip(_('You know this, but not very well.'))
        self.grade_3_button.setText(_('&3'))
        self.grade_4_button.setToolTip(_('You know this.'))
        self.grade_4_button.setText(_('&4'))
        self.grade_5_button.setToolTip(_('You know this very well.'))
        self.grade_5_button.setText(_('&5'))
        self.preview_button.setText(_('&Preview'))
        self.exit_button.setText(_('&Exit'))

from mnemosyne.pyqt_ui.completion_combo_box import CompletionComboBox
from . import mnemosyne_rc
