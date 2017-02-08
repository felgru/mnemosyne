# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'criterion_wdgt_default.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DefaultCriterionWdgt(object):
    def setupUi(self, DefaultCriterionWdgt):
        DefaultCriterionWdgt.setObjectName("DefaultCriterionWdgt")
        DefaultCriterionWdgt.resize(583, 427)
        self.verticalLayout = QtWidgets.QVBoxLayout(DefaultCriterionWdgt)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(DefaultCriterionWdgt)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.active_or_forbidden = QtWidgets.QComboBox(DefaultCriterionWdgt)
        self.active_or_forbidden.setObjectName("active_or_forbidden")
        self.active_or_forbidden.addItem("")
        self.active_or_forbidden.addItem("")
        self.gridLayout.addWidget(self.active_or_forbidden, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(DefaultCriterionWdgt)
        self.active_or_forbidden.currentIndexChanged['int'].connect(DefaultCriterionWdgt.criterion_changed)
        QtCore.QMetaObject.connectSlotsByName(DefaultCriterionWdgt)

    def retranslateUi(self, DefaultCriterionWdgt):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_('Activate cards from these card types:'))
        self.active_or_forbidden.setItemText(0, _('having any of these tags:'))
        self.active_or_forbidden.setItemText(1, _('not having any of these tags:'))

