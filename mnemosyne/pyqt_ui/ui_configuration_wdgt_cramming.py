# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuration_wdgt_cramming.ui'
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

class Ui_ConfigurationWdgtCramming(object):
    def setupUi(self, ConfigurationWdgtCramming):
        ConfigurationWdgtCramming.setObjectName(_fromUtf8("ConfigurationWdgtCramming"))
        ConfigurationWdgtCramming.resize(349, 299)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(ConfigurationWdgtCramming)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(ConfigurationWdgtCramming)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.order = QtGui.QComboBox(ConfigurationWdgtCramming)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order.sizePolicy().hasHeightForWidth())
        self.order.setSizePolicy(sizePolicy)
        self.order.setObjectName(_fromUtf8("order"))
        self.order.addItem(_fromUtf8(""))
        self.order.addItem(_fromUtf8(""))
        self.order.addItem(_fromUtf8(""))
        self.order.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.order)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.store_state = QtGui.QCheckBox(ConfigurationWdgtCramming)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.store_state.sizePolicy().hasHeightForWidth())
        self.store_state.setSizePolicy(sizePolicy)
        self.store_state.setText(_fromUtf8(""))
        self.store_state.setChecked(True)
        self.store_state.setObjectName(_fromUtf8("store_state"))
        self.horizontalLayout_2.addWidget(self.store_state)
        self.label_2 = QtGui.QLabel(ConfigurationWdgtCramming)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(1, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.label_2.setBuddy(self.store_state)

        self.retranslateUi(ConfigurationWdgtCramming)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationWdgtCramming)

    def retranslateUi(self, ConfigurationWdgtCramming):
        ConfigurationWdgtCramming.setWindowTitle(_('Form'))
        self.label.setText(_('Show cards'))
        self.order.setItemText(0, _('in random order'))
        self.order.setItemText(1, _('earliest scheduled first'))
        self.order.setItemText(2, _('lastest scheduled first'))
        self.order.setItemText(3, _('most lapses first'))
        self.label_2.setText(_('Remember which cards you\'ve seen when restarting Mnemosyne.'))

