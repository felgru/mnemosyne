# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tip_dlg.ui'
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

class Ui_TipDlg(object):
    def setupUi(self, TipDlg):
        TipDlg.setObjectName(_fromUtf8("TipDlg"))
        TipDlg.resize(435, 212)
        self.vboxlayout = QtGui.QVBoxLayout(TipDlg)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setContentsMargins(5, -1, 5, -1)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.watermark = QtGui.QLabel(TipDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.watermark.sizePolicy().hasHeightForWidth())
        self.watermark.setSizePolicy(sizePolicy)
        self.watermark.setPixmap(QtGui.QPixmap(_fromUtf8("image0")))
        self.watermark.setScaledContents(True)
        self.watermark.setWordWrap(False)
        self.watermark.setObjectName(_fromUtf8("watermark"))
        self.hboxlayout.addWidget(self.watermark)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.tip_label_2 = QtGui.QLabel(TipDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tip_label_2.sizePolicy().hasHeightForWidth())
        self.tip_label_2.setSizePolicy(sizePolicy)
        self.tip_label_2.setWordWrap(False)
        self.tip_label_2.setObjectName(_fromUtf8("tip_label_2"))
        self.vboxlayout2.addWidget(self.tip_label_2)
        self.tip_label = QtGui.QLabel(TipDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tip_label.sizePolicy().hasHeightForWidth())
        self.tip_label.setSizePolicy(sizePolicy)
        self.tip_label.setText(_fromUtf8(""))
        self.tip_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.tip_label.setWordWrap(True)
        self.tip_label.setOpenExternalLinks(True)
        self.tip_label.setObjectName(_fromUtf8("tip_label"))
        self.vboxlayout2.addWidget(self.tip_label)
        self.hboxlayout.addLayout(self.vboxlayout2)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.line1 = QtGui.QFrame(TipDlg)
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName(_fromUtf8("line1"))
        self.vboxlayout1.addWidget(self.line1)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.show_tips = QtGui.QCheckBox(TipDlg)
        self.show_tips.setChecked(True)
        self.show_tips.setObjectName(_fromUtf8("show_tips"))
        self.hboxlayout1.addWidget(self.show_tips)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.previous_button = QtGui.QPushButton(TipDlg)
        self.previous_button.setObjectName(_fromUtf8("previous_button"))
        self.hboxlayout1.addWidget(self.previous_button)
        self.next_button = QtGui.QPushButton(TipDlg)
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.hboxlayout1.addWidget(self.next_button)
        self.OK_button = QtGui.QPushButton(TipDlg)
        self.OK_button.setDefault(True)
        self.OK_button.setObjectName(_fromUtf8("OK_button"))
        self.hboxlayout1.addWidget(self.OK_button)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(TipDlg)
        QtCore.QObject.connect(self.OK_button, QtCore.SIGNAL(_fromUtf8("clicked()")), TipDlg.close)
        QtCore.QObject.connect(self.previous_button, QtCore.SIGNAL(_fromUtf8("clicked()")), TipDlg.previous)
        QtCore.QObject.connect(self.next_button, QtCore.SIGNAL(_fromUtf8("clicked()")), TipDlg.next)
        QtCore.QMetaObject.connectSlotsByName(TipDlg)

    def retranslateUi(self, TipDlg):
        TipDlg.setWindowTitle(_('Tip of the day'))
        self.tip_label_2.setText(_('<b>Did you know...?</b>'))
        self.show_tips.setText(_('&Show tips on startup'))
        self.show_tips.setShortcut(_('Alt+S'))
        self.previous_button.setText(_('&Previous'))
        self.previous_button.setShortcut(_('Alt+P'))
        self.next_button.setText(_('&Next'))
        self.next_button.setShortcut(_('Alt+N'))
        self.OK_button.setText(_('&Close'))
        self.OK_button.setShortcut(_('Alt+C'))

