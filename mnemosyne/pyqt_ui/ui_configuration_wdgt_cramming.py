# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuration_wdgt_cramming.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigurationWdgtCramming(object):
    def setupUi(self, ConfigurationWdgtCramming):
        ConfigurationWdgtCramming.setObjectName("ConfigurationWdgtCramming")
        ConfigurationWdgtCramming.resize(349, 299)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(ConfigurationWdgtCramming)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ConfigurationWdgtCramming)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.order = QtWidgets.QComboBox(ConfigurationWdgtCramming)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order.sizePolicy().hasHeightForWidth())
        self.order.setSizePolicy(sizePolicy)
        self.order.setObjectName("order")
        self.order.addItem("")
        self.order.addItem("")
        self.order.addItem("")
        self.order.addItem("")
        self.horizontalLayout.addWidget(self.order)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.store_state = QtWidgets.QCheckBox(ConfigurationWdgtCramming)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.store_state.sizePolicy().hasHeightForWidth())
        self.store_state.setSizePolicy(sizePolicy)
        self.store_state.setText("")
        self.store_state.setChecked(True)
        self.store_state.setObjectName("store_state")
        self.horizontalLayout_2.addWidget(self.store_state)
        self.label_2 = QtWidgets.QLabel(ConfigurationWdgtCramming)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.label_2.setBuddy(self.store_state)

        self.retranslateUi(ConfigurationWdgtCramming)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationWdgtCramming)

    def retranslateUi(self, ConfigurationWdgtCramming):
        _translate = QtCore.QCoreApplication.translate
        ConfigurationWdgtCramming.setWindowTitle(_('Form'))
        self.label.setText(_('Show cards'))
        self.order.setItemText(0, _('in random order'))
        self.order.setItemText(1, _('earliest scheduled first'))
        self.order.setItemText(2, _('lastest scheduled first'))
        self.order.setItemText(3, _('most lapses first'))
        self.label_2.setText(_('Remember which cards you\'ve seen when restarting Mnemosyne.'))

