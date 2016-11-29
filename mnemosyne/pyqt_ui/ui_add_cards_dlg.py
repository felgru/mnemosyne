# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_cards_dlg.ui'
#
# Created: Mon Apr 15 14:30:17 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddCardsDlg(object):
    def setupUi(self, AddCardsDlg):
        AddCardsDlg.setObjectName(_fromUtf8("AddCardsDlg"))
        AddCardsDlg.resize(317, 170)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(AddCardsDlg)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.vbox_layout = QtGui.QVBoxLayout()
        self.vbox_layout.setObjectName(_fromUtf8("vbox_layout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_2 = QtGui.QLabel(AddCardsDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.card_types_widget = QtGui.QComboBox(AddCardsDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_types_widget.sizePolicy().hasHeightForWidth())
        self.card_types_widget.setSizePolicy(sizePolicy)
        self.card_types_widget.setObjectName(_fromUtf8("card_types_widget"))
        self.gridlayout.addWidget(self.card_types_widget, 0, 1, 1, 1)
        self.label = QtGui.QLabel(AddCardsDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.tags = QtGui.QComboBox(AddCardsDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tags.sizePolicy().hasHeightForWidth())
        self.tags.setSizePolicy(sizePolicy)
        self.tags.setEditable(True)
        self.tags.setObjectName(_fromUtf8("tags"))
        self.gridlayout.addWidget(self.tags, 1, 1, 1, 1)
        self.vbox_layout.addLayout(self.gridlayout)
        self.grade_buttons = QtGui.QGroupBox(AddCardsDlg)
        self.grade_buttons.setObjectName(_fromUtf8("grade_buttons"))
        self.vboxlayout = QtGui.QVBoxLayout(self.grade_buttons)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.yet_to_learn_button = QtGui.QPushButton(self.grade_buttons)
        self.yet_to_learn_button.setAutoDefault(True)
        self.yet_to_learn_button.setDefault(True)
        self.yet_to_learn_button.setObjectName(_fromUtf8("yet_to_learn_button"))
        self.hboxlayout.addWidget(self.yet_to_learn_button)
        self.line = QtGui.QFrame(self.grade_buttons)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hboxlayout.addWidget(self.line)
        self.grade_2_button = QtGui.QPushButton(self.grade_buttons)
        self.grade_2_button.setAutoDefault(False)
        self.grade_2_button.setObjectName(_fromUtf8("grade_2_button"))
        self.hboxlayout.addWidget(self.grade_2_button)
        self.grade_3_button = QtGui.QPushButton(self.grade_buttons)
        self.grade_3_button.setAutoDefault(False)
        self.grade_3_button.setObjectName(_fromUtf8("grade_3_button"))
        self.hboxlayout.addWidget(self.grade_3_button)
        self.grade_4_button = QtGui.QPushButton(self.grade_buttons)
        self.grade_4_button.setAutoDefault(False)
        self.grade_4_button.setObjectName(_fromUtf8("grade_4_button"))
        self.hboxlayout.addWidget(self.grade_4_button)
        self.grade_5_button = QtGui.QPushButton(self.grade_buttons)
        self.grade_5_button.setAutoDefault(False)
        self.grade_5_button.setObjectName(_fromUtf8("grade_5_button"))
        self.hboxlayout.addWidget(self.grade_5_button)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.vbox_layout.addWidget(self.grade_buttons)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.preview_button = QtGui.QPushButton(AddCardsDlg)
        self.preview_button.setAutoDefault(False)
        self.preview_button.setObjectName(_fromUtf8("preview_button"))
        self.hboxlayout1.addWidget(self.preview_button)
        spacerItem = QtGui.QSpacerItem(101, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.exit_button = QtGui.QPushButton(AddCardsDlg)
        self.exit_button.setAutoDefault(False)
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.hboxlayout1.addWidget(self.exit_button)
        self.vbox_layout.addLayout(self.hboxlayout1)
        self.horizontalLayout_2.addLayout(self.vbox_layout)

        self.retranslateUi(AddCardsDlg)
        QtCore.QObject.connect(self.exit_button, QtCore.SIGNAL(_fromUtf8("clicked()")), AddCardsDlg.reject)
        QtCore.QObject.connect(self.preview_button, QtCore.SIGNAL(_fromUtf8("clicked()")), AddCardsDlg.preview)
        QtCore.QMetaObject.connectSlotsByName(AddCardsDlg)

    def retranslateUi(self, AddCardsDlg):
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

import mnemosyne_rc
