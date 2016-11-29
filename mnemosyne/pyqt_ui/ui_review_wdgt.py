# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'review_wdgt.ui'
#
# Created: Mon Apr 15 14:30:23 2013
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

class Ui_ReviewWdgt(object):
    def setupUi(self, ReviewWdgt):
        ReviewWdgt.setObjectName(_fromUtf8("ReviewWdgt"))
        ReviewWdgt.resize(315, 352)
        ReviewWdgt.setWindowTitle(_fromUtf8(""))
        self.verticalLayout_5 = QtGui.QVBoxLayout(ReviewWdgt)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.vertical_layout = QtGui.QVBoxLayout()
        self.vertical_layout.setMargin(9)
        self.vertical_layout.setObjectName(_fromUtf8("vertical_layout"))
        self.question_box = QtGui.QVBoxLayout()
        self.question_box.setObjectName(_fromUtf8("question_box"))
        self.question_label = QtGui.QLabel(ReviewWdgt)
        self.question_label.setObjectName(_fromUtf8("question_label"))
        self.question_box.addWidget(self.question_label)
        self.question = QWebView2(ReviewWdgt)
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
        self.answer_label = QtGui.QLabel(ReviewWdgt)
        self.answer_label.setObjectName(_fromUtf8("answer_label"))
        self.answer_box.addWidget(self.answer_label)
        self.answer = QWebView2(ReviewWdgt)
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
        self.show_button = QPushButton2(ReviewWdgt)
        self.show_button.setObjectName(_fromUtf8("show_button"))
        self.vertical_layout.addWidget(self.show_button)
        self.grades = QtGui.QGroupBox(ReviewWdgt)
        self.grades.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grades.setObjectName(_fromUtf8("grades"))
        self._2 = QtGui.QVBoxLayout(self.grades)
        self._2.setObjectName(_fromUtf8("_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.grade_0_button = QPushButton2(self.grades)
        self.grade_0_button.setObjectName(_fromUtf8("grade_0_button"))
        self.horizontalLayout.addWidget(self.grade_0_button)
        self.grade_1_button = QPushButton2(self.grades)
        self.grade_1_button.setObjectName(_fromUtf8("grade_1_button"))
        self.horizontalLayout.addWidget(self.grade_1_button)
        self.line = QtGui.QFrame(self.grades)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.grade_2_button = QPushButton2(self.grades)
        self.grade_2_button.setObjectName(_fromUtf8("grade_2_button"))
        self.horizontalLayout.addWidget(self.grade_2_button)
        self.grade_3_button = QPushButton2(self.grades)
        self.grade_3_button.setObjectName(_fromUtf8("grade_3_button"))
        self.horizontalLayout.addWidget(self.grade_3_button)
        self.grade_4_button = QPushButton2(self.grades)
        self.grade_4_button.setObjectName(_fromUtf8("grade_4_button"))
        self.horizontalLayout.addWidget(self.grade_4_button)
        self.grade_5_button = QPushButton2(self.grades)
        self.grade_5_button.setObjectName(_fromUtf8("grade_5_button"))
        self.horizontalLayout.addWidget(self.grade_5_button)
        self._2.addLayout(self.horizontalLayout)
        self.vertical_layout.addWidget(self.grades)
        self.verticalLayout_5.addLayout(self.vertical_layout)

        self.retranslateUi(ReviewWdgt)
        QtCore.QObject.connect(self.show_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ReviewWdgt.show_answer)
        QtCore.QMetaObject.connectSlotsByName(ReviewWdgt)

    def retranslateUi(self, ReviewWdgt):
        self.question_label.setText(_('Question:'))
        self.answer_label.setText(_('Answer:'))
        self.show_button.setText(_('Show &answer'))
        self.grades.setTitle(_('Grade your answer:'))
        self.grade_0_button.setText(_('0'))
        self.grade_0_button.setShortcut(_('0'))
        self.grade_1_button.setText(_('1'))
        self.grade_1_button.setShortcut(_('1'))
        self.grade_2_button.setText(_('2'))
        self.grade_2_button.setShortcut(_('2'))
        self.grade_3_button.setText(_('3'))
        self.grade_3_button.setShortcut(_('3'))
        self.grade_4_button.setText(_('4'))
        self.grade_4_button.setShortcut(_('4'))
        self.grade_5_button.setText(_('5'))
        self.grade_5_button.setShortcut(_('5'))

from PyQt4 import QtWebKit
