# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuration_wdgt_card_appearance.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigurationWdgtCardAppearance(object):
    def setupUi(self, ConfigurationWdgtCardAppearance):
        ConfigurationWdgtCardAppearance.setObjectName("ConfigurationWdgtCardAppearance")
        ConfigurationWdgtCardAppearance.resize(374, 256)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ConfigurationWdgtCardAppearance)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(ConfigurationWdgtCardAppearance)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.card_types_widget = QtWidgets.QComboBox(ConfigurationWdgtCardAppearance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_types_widget.sizePolicy().hasHeightForWidth())
        self.card_types_widget.setSizePolicy(sizePolicy)
        self.card_types_widget.setObjectName("card_types_widget")
        self.horizontalLayout.addWidget(self.card_types_widget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_4 = QtWidgets.QFrame(ConfigurationWdgtCardAppearance)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(ConfigurationWdgtCardAppearance)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontal_layout_bg_colour = QtWidgets.QHBoxLayout()
        self.horizontal_layout_bg_colour.setObjectName("horizontal_layout_bg_colour")
        self.bg_label = QtWidgets.QLabel(ConfigurationWdgtCardAppearance)
        self.bg_label.setObjectName("bg_label")
        self.horizontal_layout_bg_colour.addWidget(self.bg_label)
        self.background_button = QtWidgets.QPushButton(ConfigurationWdgtCardAppearance)
        self.background_button.setObjectName("background_button")
        self.horizontal_layout_bg_colour.addWidget(self.background_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_bg_colour.addItem(spacerItem3)
        self.align_label = QtWidgets.QLabel(ConfigurationWdgtCardAppearance)
        self.align_label.setObjectName("align_label")
        self.horizontal_layout_bg_colour.addWidget(self.align_label)
        self.alignment = QtWidgets.QComboBox(ConfigurationWdgtCardAppearance)
        font = QtGui.QFont()
        font.setItalic(False)
        self.alignment.setFont(font)
        self.alignment.setObjectName("alignment")
        self.alignment.addItem("")
        self.alignment.addItem("")
        self.alignment.addItem("")
        self.horizontal_layout_bg_colour.addWidget(self.alignment)
        self.verticalLayout.addLayout(self.horizontal_layout_bg_colour)
        self.line_non_latin = QtWidgets.QFrame(ConfigurationWdgtCardAppearance)
        self.line_non_latin.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_non_latin.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_non_latin.setObjectName("line_non_latin")
        self.verticalLayout.addWidget(self.line_non_latin)
        self.non_latin_layout = QtWidgets.QHBoxLayout()
        self.non_latin_layout.setObjectName("non_latin_layout")
        self.label_non_latin_1 = QtWidgets.QLabel(ConfigurationWdgtCardAppearance)
        self.label_non_latin_1.setObjectName("label_non_latin_1")
        self.non_latin_layout.addWidget(self.label_non_latin_1)
        self.non_latin_font_size_increase = QtWidgets.QSpinBox(ConfigurationWdgtCardAppearance)
        self.non_latin_font_size_increase.setObjectName("non_latin_font_size_increase")
        self.non_latin_layout.addWidget(self.non_latin_font_size_increase)
        self.label_non_latin_2 = QtWidgets.QLabel(ConfigurationWdgtCardAppearance)
        self.label_non_latin_2.setObjectName("label_non_latin_2")
        self.non_latin_layout.addWidget(self.label_non_latin_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.non_latin_layout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.non_latin_layout)
        self.label_non_latin_3 = QtWidgets.QLabel(ConfigurationWdgtCardAppearance)
        self.label_non_latin_3.setWordWrap(True)
        self.label_non_latin_3.setObjectName("label_non_latin_3")
        self.verticalLayout.addWidget(self.label_non_latin_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.preview_button = QtWidgets.QPushButton(ConfigurationWdgtCardAppearance)
        self.preview_button.setAutoDefault(False)
        self.preview_button.setObjectName("preview_button")
        self.horizontalLayout_5.addWidget(self.preview_button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ConfigurationWdgtCardAppearance)
        self.preview_button.clicked.connect(ConfigurationWdgtCardAppearance.preview)
        self.card_types_widget.currentIndexChanged['QString'].connect(ConfigurationWdgtCardAppearance.card_type_changed)
        self.background_button.clicked.connect(ConfigurationWdgtCardAppearance.update_background_colour)
        self.alignment.activated['int'].connect(ConfigurationWdgtCardAppearance.update_alignment)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationWdgtCardAppearance)

    def retranslateUi(self, ConfigurationWdgtCardAppearance):
        _translate = QtCore.QCoreApplication.translate
        ConfigurationWdgtCardAppearance.setWindowTitle(_('Form'))
        self.label_2.setText(_('Card type:'))
        self.bg_label.setText(_('Background:'))
        self.background_button.setText(_('Set colour'))
        self.align_label.setText(_('Alignment:'))
        self.alignment.setItemText(0, _('Left'))
        self.alignment.setItemText(1, _('Center'))
        self.alignment.setItemText(2, _('Right'))
        self.label_non_latin_1.setText(_('Increase size of non-latin characters by'))
        self.label_non_latin_2.setText(_('points.'))
        self.label_non_latin_3.setText(_('(This setting will be overridden in card types cloned from \'Vocabulary\'.)'))
        self.preview_button.setText(_('&Preview'))

