# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'review_wdgt.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReviewWdgt(object):
    def setupUi(self, ReviewWdgt):
        ReviewWdgt.setObjectName("ReviewWdgt")
        ReviewWdgt.resize(529, 259)
        ReviewWdgt.setWindowTitle("")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(ReviewWdgt)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setContentsMargins(9, 9, 9, 9)
        self.vertical_layout.setObjectName("vertical_layout")
        self.question_box = QtWidgets.QVBoxLayout()
        self.question_box.setObjectName("question_box")
        self.question_label = QtWidgets.QLabel(ReviewWdgt)
        self.question_label.setObjectName("question_label")
        self.question_box.addWidget(self.question_label)
        self.question = QWebEngineView2(ReviewWdgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question.sizePolicy().hasHeightForWidth())
        self.question.setSizePolicy(sizePolicy)
        self.question.setMinimumSize(QtCore.QSize(295, 50))
        self.question.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.question.setAcceptDrops(False)
        self.question.setProperty("url", QtCore.QUrl("about:blank"))
        self.question.setObjectName("question")
        self.question_box.addWidget(self.question)
        self.vertical_layout.addLayout(self.question_box)
        self.answer_box = QtWidgets.QVBoxLayout()
        self.answer_box.setObjectName("answer_box")
        self.answer_label = QtWidgets.QLabel(ReviewWdgt)
        self.answer_label.setObjectName("answer_label")
        self.answer_box.addWidget(self.answer_label)
        self.answer = QWebEngineView2(ReviewWdgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer.sizePolicy().hasHeightForWidth())
        self.answer.setSizePolicy(sizePolicy)
        self.answer.setMinimumSize(QtCore.QSize(295, 50))
        self.answer.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.answer.setAcceptDrops(False)
        self.answer.setProperty("url", QtCore.QUrl("about:blank"))
        self.answer.setObjectName("answer")
        self.answer_box.addWidget(self.answer)
        self.vertical_layout.addLayout(self.answer_box)
        self.show_button = QtWidgets.QPushButton(ReviewWdgt)
        self.show_button.setObjectName("show_button")
        self.vertical_layout.addWidget(self.show_button)
        self.grades = QtWidgets.QGroupBox(ReviewWdgt)
        self.grades.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grades.setObjectName("grades")
        self._2 = QtWidgets.QVBoxLayout(self.grades)
        self._2.setObjectName("_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grade_0_button = QPushButton2(self.grades)
        self.grade_0_button.setObjectName("grade_0_button")
        self.horizontalLayout.addWidget(self.grade_0_button)
        self.grade_1_button = QPushButton2(self.grades)
        self.grade_1_button.setObjectName("grade_1_button")
        self.horizontalLayout.addWidget(self.grade_1_button)
        self.line = QtWidgets.QFrame(self.grades)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.grade_2_button = QPushButton2(self.grades)
        self.grade_2_button.setObjectName("grade_2_button")
        self.horizontalLayout.addWidget(self.grade_2_button)
        self.grade_3_button = QPushButton2(self.grades)
        self.grade_3_button.setObjectName("grade_3_button")
        self.horizontalLayout.addWidget(self.grade_3_button)
        self.grade_4_button = QPushButton2(self.grades)
        self.grade_4_button.setObjectName("grade_4_button")
        self.horizontalLayout.addWidget(self.grade_4_button)
        self.grade_5_button = QPushButton2(self.grades)
        self.grade_5_button.setObjectName("grade_5_button")
        self.horizontalLayout.addWidget(self.grade_5_button)
        self._2.addLayout(self.horizontalLayout)
        self.vertical_layout.addWidget(self.grades)
        self.verticalLayout_5.addLayout(self.vertical_layout)

        self.retranslateUi(ReviewWdgt)
        self.show_button.clicked.connect(ReviewWdgt.show_answer)
        QtCore.QMetaObject.connectSlotsByName(ReviewWdgt)

    def retranslateUi(self, ReviewWdgt):
        _translate = QtCore.QCoreApplication.translate
        self.question_label.setText(_('Question:'))
        self.answer_label.setText(_('Answer:'))
        self.show_button.setText(_('Show &answer'))
        self.grades.setTitle(_('Grade your answer:'))
        self.grade_0_button.setProperty("text", _('0'))
        self.grade_1_button.setProperty("text", _('1'))
        self.grade_2_button.setProperty("text", _('2'))
        self.grade_3_button.setProperty("text", _('3'))
        self.grade_4_button.setProperty("text", _('4'))
        self.grade_5_button.setProperty("text", _('5'))

from mnemosyne.pyqt_ui.qpushbutton2 import QPushButton2
from mnemosyne.pyqt_ui.qwebengineview2 import QWebEngineView2
