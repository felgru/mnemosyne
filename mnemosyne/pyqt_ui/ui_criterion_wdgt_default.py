# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'criterion_wdgt_default.ui'
#
# Created: Mon Apr 15 14:30:20 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DefaultCriterionWdgt(object):
    def setupUi(self, DefaultCriterionWdgt):
        DefaultCriterionWdgt.setObjectName(_fromUtf8("DefaultCriterionWdgt"))
        DefaultCriterionWdgt.resize(583, 427)
        self.verticalLayout = QtGui.QVBoxLayout(DefaultCriterionWdgt)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(DefaultCriterionWdgt)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.active_or_forbidden = QtGui.QComboBox(DefaultCriterionWdgt)
        self.active_or_forbidden.setObjectName(_fromUtf8("active_or_forbidden"))
        self.active_or_forbidden.addItem(_fromUtf8(""))
        self.active_or_forbidden.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.active_or_forbidden, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(DefaultCriterionWdgt)
        QtCore.QObject.connect(self.active_or_forbidden, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), DefaultCriterionWdgt.criterion_changed)
        QtCore.QMetaObject.connectSlotsByName(DefaultCriterionWdgt)

    def retranslateUi(self, DefaultCriterionWdgt):
        self.label.setText(_('Activate cards from these card types:'))
        self.active_or_forbidden.setItemText(0, _('having any of these tags:'))
        self.active_or_forbidden.setItemText(1, _('not having any of these tags:'))

