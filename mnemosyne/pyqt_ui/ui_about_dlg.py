# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDlg(object):
    def setupUi(self, AboutDlg):
        AboutDlg.setObjectName("AboutDlg")
        AboutDlg.resize(452, 226)
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutDlg)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setContentsMargins(5, 11, 5, 11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setContentsMargins(11, 11, 11, 11)
        self._2.setSpacing(6)
        self._2.setObjectName("_2")
        self.watermark = QtWidgets.QLabel(AboutDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.watermark.sizePolicy().hasHeightForWidth())
        self.watermark.setSizePolicy(sizePolicy)
        self.watermark.setPixmap(QtGui.QPixmap("image0"))
        self.watermark.setScaledContents(True)
        self.watermark.setWordWrap(False)
        self.watermark.setObjectName("watermark")
        self._2.addWidget(self.watermark)
        self._3 = QtWidgets.QVBoxLayout()
        self._3.setContentsMargins(11, 11, 11, 11)
        self._3.setSpacing(6)
        self._3.setObjectName("_3")
        self.about_label = QtWidgets.QLabel(AboutDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_label.sizePolicy().hasHeightForWidth())
        self.about_label.setSizePolicy(sizePolicy)
        self.about_label.setText("")
        self.about_label.setTextFormat(QtCore.Qt.RichText)
        self.about_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.about_label.setWordWrap(True)
        self.about_label.setOpenExternalLinks(True)
        self.about_label.setObjectName("about_label")
        self._3.addWidget(self.about_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self._3.addItem(spacerItem)
        self._2.addLayout(self._3)
        self.vboxlayout.addLayout(self._2)
        self.line1 = QtWidgets.QFrame(AboutDlg)
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.vboxlayout.addWidget(self.line1)
        self._4 = QtWidgets.QHBoxLayout()
        self._4.setContentsMargins(11, 11, 11, 11)
        self._4.setSpacing(6)
        self._4.setObjectName("_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._4.addItem(spacerItem1)
        self.OK_button = QtWidgets.QPushButton(AboutDlg)
        self.OK_button.setDefault(True)
        self.OK_button.setObjectName("OK_button")
        self._4.addWidget(self.OK_button)
        self.vboxlayout.addLayout(self._4)
        self.verticalLayout.addLayout(self.vboxlayout)

        self.retranslateUi(AboutDlg)
        self.OK_button.clicked.connect(AboutDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(AboutDlg)

    def retranslateUi(self, AboutDlg):
        _translate = QtCore.QCoreApplication.translate
        AboutDlg.setWindowTitle(_('About Mnemosyne'))
        self.OK_button.setText(_('&OK'))
        self.OK_button.setShortcut(_('Alt+C'))

