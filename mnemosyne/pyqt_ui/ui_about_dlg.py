# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_dlg.ui'
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

class Ui_AboutDlg(object):
    def setupUi(self, AboutDlg):
        AboutDlg.setObjectName(_fromUtf8("AboutDlg"))
        AboutDlg.resize(435, 212)
        self.verticalLayout = QtGui.QVBoxLayout(AboutDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setContentsMargins(5, -1, 5, -1)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self._2 = QtGui.QHBoxLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.watermark = QtGui.QLabel(AboutDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.watermark.sizePolicy().hasHeightForWidth())
        self.watermark.setSizePolicy(sizePolicy)
        self.watermark.setPixmap(QtGui.QPixmap(_fromUtf8("image0")))
        self.watermark.setScaledContents(True)
        self.watermark.setWordWrap(False)
        self.watermark.setObjectName(_fromUtf8("watermark"))
        self._2.addWidget(self.watermark)
        self._3 = QtGui.QVBoxLayout()
        self._3.setObjectName(_fromUtf8("_3"))
        self.about_label = QtGui.QLabel(AboutDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_label.sizePolicy().hasHeightForWidth())
        self.about_label.setSizePolicy(sizePolicy)
        self.about_label.setText(_fromUtf8(""))
        self.about_label.setTextFormat(QtCore.Qt.RichText)
        self.about_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.about_label.setWordWrap(True)
        self.about_label.setOpenExternalLinks(True)
        self.about_label.setObjectName(_fromUtf8("about_label"))
        self._3.addWidget(self.about_label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self._3.addItem(spacerItem)
        self._2.addLayout(self._3)
        self.vboxlayout.addLayout(self._2)
        self.line1 = QtGui.QFrame(AboutDlg)
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName(_fromUtf8("line1"))
        self.vboxlayout.addWidget(self.line1)
        self._4 = QtGui.QHBoxLayout()
        self._4.setObjectName(_fromUtf8("_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self._4.addItem(spacerItem1)
        self.OK_button = QtGui.QPushButton(AboutDlg)
        self.OK_button.setDefault(True)
        self.OK_button.setObjectName(_fromUtf8("OK_button"))
        self._4.addWidget(self.OK_button)
        self.vboxlayout.addLayout(self._4)
        self.verticalLayout.addLayout(self.vboxlayout)

        self.retranslateUi(AboutDlg)
        QtCore.QObject.connect(self.OK_button, QtCore.SIGNAL(_fromUtf8("clicked()")), AboutDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(AboutDlg)

    def retranslateUi(self, AboutDlg):
        AboutDlg.setWindowTitle(_('About Mnemosyne'))
        self.OK_button.setText(_('&OK'))
        self.OK_button.setShortcut(_('Alt+C'))

