# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preview_cards_dlg.ui'
#
# Created: Mon Apr 15 14:30:24 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from qwebview2 import *
from qpushbutton2 import *
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PreviewCardsDlg(object):
    def setupUi(self, PreviewCardsDlg):
        PreviewCardsDlg.setObjectName(_fromUtf8("PreviewCardsDlg"))
        PreviewCardsDlg.resize(369, 332)
        self.verticalLayout_4 = QtGui.QVBoxLayout(PreviewCardsDlg)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.vertical_layout = QtGui.QVBoxLayout()
        self.vertical_layout.setObjectName(_fromUtf8("vertical_layout"))
        self.fact_view_name = QtGui.QLabel(PreviewCardsDlg)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fact_view_name.setFont(font)
        self.fact_view_name.setText(_fromUtf8(""))
        self.fact_view_name.setObjectName(_fromUtf8("fact_view_name"))
        self.vertical_layout.addWidget(self.fact_view_name)
        self.question_box = QtGui.QVBoxLayout()
        self.question_box.setObjectName(_fromUtf8("question_box"))
        self.question_label = QtGui.QLabel(PreviewCardsDlg)
        self.question_label.setMaximumSize(QtCore.QSize(320, 16777215))
        self.question_label.setObjectName(_fromUtf8("question_label"))
        self.question_box.addWidget(self.question_label)
        self.question = QWebView2(PreviewCardsDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question.sizePolicy().hasHeightForWidth())
        self.question.setSizePolicy(sizePolicy)
        self.question.setMinimumSize(QtCore.QSize(295, 50))
        self.question.setAcceptDrops(False)
        self.question.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.question.setObjectName(_fromUtf8("question"))
        self.question_box.addWidget(self.question)
        self.vertical_layout.addLayout(self.question_box)
        self.answer_box = QtGui.QVBoxLayout()
        self.answer_box.setObjectName(_fromUtf8("answer_box"))
        self.answer_label = QtGui.QLabel(PreviewCardsDlg)
        self.answer_label.setObjectName(_fromUtf8("answer_label"))
        self.answer_box.addWidget(self.answer_label)
        self.answer = QWebView2(PreviewCardsDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer.sizePolicy().hasHeightForWidth())
        self.answer.setSizePolicy(sizePolicy)
        self.answer.setMinimumSize(QtCore.QSize(295, 50))
        self.answer.setAcceptDrops(False)
        self.answer.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.answer.setObjectName(_fromUtf8("answer"))
        self.answer_box.addWidget(self.answer)
        self.vertical_layout.addLayout(self.answer_box)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.previous_button = QPushButton2(PreviewCardsDlg)
        self.previous_button.setObjectName(_fromUtf8("previous_button"))
        self.horizontalLayout.addWidget(self.previous_button)
        self.next_button = QPushButton2(PreviewCardsDlg)
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.horizontalLayout.addWidget(self.next_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.OK_button = QPushButton2(PreviewCardsDlg)
        self.OK_button.setAutoDefault(True)
        self.OK_button.setDefault(True)
        self.OK_button.setObjectName(_fromUtf8("OK_button"))
        self.horizontalLayout.addWidget(self.OK_button)
        self.vertical_layout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.vertical_layout)

        self.retranslateUi(PreviewCardsDlg)
        QtCore.QObject.connect(self.previous_button, QtCore.SIGNAL(_fromUtf8("clicked()")), PreviewCardsDlg.previous)
        QtCore.QObject.connect(self.next_button, QtCore.SIGNAL(_fromUtf8("clicked()")), PreviewCardsDlg.next)
        QtCore.QObject.connect(self.OK_button, QtCore.SIGNAL(_fromUtf8("clicked()")), PreviewCardsDlg.close)
        QtCore.QMetaObject.connectSlotsByName(PreviewCardsDlg)

    def retranslateUi(self, PreviewCardsDlg):
        PreviewCardsDlg.setWindowTitle(_('Preview cards'))
        self.question_label.setText(_('Question:'))
        self.answer_label.setText(_('Answer:'))
        self.previous_button.setText(_('&Previous sister card'))
        self.next_button.setText(_('&Next sister card'))
        self.OK_button.setText(_('&OK'))

from PyQt4 import QtWebKit
