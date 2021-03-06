# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preview_cards_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreviewCardsDlg(object):
    def setupUi(self, PreviewCardsDlg):
        PreviewCardsDlg.setObjectName("PreviewCardsDlg")
        PreviewCardsDlg.resize(369, 332)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(PreviewCardsDlg)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.fact_view_name = QtWidgets.QLabel(PreviewCardsDlg)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fact_view_name.setFont(font)
        self.fact_view_name.setText("")
        self.fact_view_name.setObjectName("fact_view_name")
        self.vertical_layout.addWidget(self.fact_view_name)
        self.question_box = QtWidgets.QVBoxLayout()
        self.question_box.setObjectName("question_box")
        self.question_label = QtWidgets.QLabel(PreviewCardsDlg)
        self.question_label.setMaximumSize(QtCore.QSize(320, 16777215))
        self.question_label.setObjectName("question_label")
        self.question_box.addWidget(self.question_label)
        self.question = QWebEngineView2(PreviewCardsDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question.sizePolicy().hasHeightForWidth())
        self.question.setSizePolicy(sizePolicy)
        self.question.setMinimumSize(QtCore.QSize(295, 50))
        self.question.setAcceptDrops(False)
        self.question.setUrl(QtCore.QUrl("about:blank"))
        self.question.setObjectName("question")
        self.question_box.addWidget(self.question)
        self.vertical_layout.addLayout(self.question_box)
        self.answer_box = QtWidgets.QVBoxLayout()
        self.answer_box.setObjectName("answer_box")
        self.answer_label = QtWidgets.QLabel(PreviewCardsDlg)
        self.answer_label.setObjectName("answer_label")
        self.answer_box.addWidget(self.answer_label)
        self.answer = QWebEngineView2(PreviewCardsDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer.sizePolicy().hasHeightForWidth())
        self.answer.setSizePolicy(sizePolicy)
        self.answer.setMinimumSize(QtCore.QSize(295, 50))
        self.answer.setAcceptDrops(False)
        self.answer.setUrl(QtCore.QUrl("about:blank"))
        self.answer.setObjectName("answer")
        self.answer_box.addWidget(self.answer)
        self.vertical_layout.addLayout(self.answer_box)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous_button = QtWidgets.QPushButton(PreviewCardsDlg)
        self.previous_button.setAutoDefault(True)
        self.previous_button.setObjectName("previous_button")
        self.horizontalLayout.addWidget(self.previous_button)
        self.next_button = QtWidgets.QPushButton(PreviewCardsDlg)
        self.next_button.setAutoDefault(True)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.OK_button = QtWidgets.QPushButton(PreviewCardsDlg)
        self.OK_button.setAutoDefault(True)
        self.OK_button.setDefault(True)
        self.OK_button.setObjectName("OK_button")
        self.horizontalLayout.addWidget(self.OK_button)
        self.vertical_layout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.vertical_layout)

        self.retranslateUi(PreviewCardsDlg)
        self.previous_button.clicked.connect(PreviewCardsDlg.previous)
        self.next_button.clicked.connect(PreviewCardsDlg.next)
        self.OK_button.clicked.connect(PreviewCardsDlg.close)
        QtCore.QMetaObject.connectSlotsByName(PreviewCardsDlg)

    def retranslateUi(self, PreviewCardsDlg):
        _translate = QtCore.QCoreApplication.translate
        PreviewCardsDlg.setWindowTitle(_('Preview cards'))
        self.question_label.setText(_('Question:'))
        self.answer_label.setText(_('Answer:'))
        self.previous_button.setText(_('&Previous sister card'))
        self.next_button.setText(_('&Next sister card'))
        self.OK_button.setText(_('&OK'))

from mnemosyne.pyqt_ui.qwebengineview2 import QWebEngineView2
