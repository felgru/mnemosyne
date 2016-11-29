# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getting_started_dlg.ui'
#
# Created: Mon Apr 15 14:30:22 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from mnemosyne.libmnemosyne.translator import _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GettingStartedDlg(object):
    def setupUi(self, GettingStartedDlg):
        GettingStartedDlg.setObjectName(_fromUtf8("GettingStartedDlg"))
        GettingStartedDlg.resize(693, 450)
        GettingStartedDlg.setMinimumSize(QtCore.QSize(600, 450))
        GettingStartedDlg.setWizardStyle(QtGui.QWizard.ClassicStyle)
        GettingStartedDlg.setOptions(QtGui.QWizard.IgnoreSubTitles)
        GettingStartedDlg.setTitleFormat(QtCore.Qt.PlainText)
        self.intro = QtGui.QWizardPage()
        self.intro.setObjectName(_fromUtf8("intro"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.intro)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.intro_lbl = QtGui.QLabel(self.intro)
        self.intro_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.intro_lbl.setWordWrap(True)
        self.intro_lbl.setMargin(12)
        self.intro_lbl.setObjectName(_fromUtf8("intro_lbl"))
        self.verticalLayout_3.addWidget(self.intro_lbl)
        GettingStartedDlg.addPage(self.intro)
        self.grades02 = QtGui.QWizardPage()
        self.grades02.setObjectName(_fromUtf8("grades02"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.grades02)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.grades02_lbl = QtGui.QLabel(self.grades02)
        self.grades02_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.grades02_lbl.setWordWrap(True)
        self.grades02_lbl.setMargin(12)
        self.grades02_lbl.setObjectName(_fromUtf8("grades02_lbl"))
        self.verticalLayout_4.addWidget(self.grades02_lbl)
        GettingStartedDlg.addPage(self.grades02)
        self.grades35 = QtGui.QWizardPage()
        self.grades35.setObjectName(_fromUtf8("grades35"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.grades35)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.grades35_lbl = QtGui.QLabel(self.grades35)
        self.grades35_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.grades35_lbl.setWordWrap(True)
        self.grades35_lbl.setMargin(12)
        self.grades35_lbl.setObjectName(_fromUtf8("grades35_lbl"))
        self.verticalLayout_5.addWidget(self.grades35_lbl)
        GettingStartedDlg.addPage(self.grades35)
        self.statistics = QtGui.QWizardPage()
        self.statistics.setObjectName(_fromUtf8("statistics"))
        self.verticalLayout = QtGui.QVBoxLayout(self.statistics)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.statistics_lbl = QtGui.QLabel(self.statistics)
        self.statistics_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.statistics_lbl.setWordWrap(True)
        self.statistics_lbl.setMargin(12)
        self.statistics_lbl.setObjectName(_fromUtf8("statistics_lbl"))
        self.verticalLayout.addWidget(self.statistics_lbl)
        self.upload_box = QtGui.QCheckBox(self.statistics)
        self.upload_box.setEnabled(True)
        self.upload_box.setChecked(True)
        self.upload_box.setObjectName(_fromUtf8("upload_box"))
        self.verticalLayout.addWidget(self.upload_box)
        GettingStartedDlg.addPage(self.statistics)
        self.ready = QtGui.QWizardPage()
        self.ready.setObjectName(_fromUtf8("ready"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.ready)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ready_lbl = QtGui.QLabel(self.ready)
        self.ready_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ready_lbl.setWordWrap(True)
        self.ready_lbl.setMargin(12)
        self.ready_lbl.setObjectName(_fromUtf8("ready_lbl"))
        self.verticalLayout_2.addWidget(self.ready_lbl)
        GettingStartedDlg.addPage(self.ready)

        self.retranslateUi(GettingStartedDlg)
        QtCore.QMetaObject.connectSlotsByName(GettingStartedDlg)

    def retranslateUi(self, GettingStartedDlg):
        GettingStartedDlg.setWindowTitle(_('Wizard'))
        self.intro.setTitle(_('Introduction'))
        self.intro_lbl.setText(_('Welcome to Mnemosyne, a flash card program named both after the Greek goddess of Memory and a type of butterfly.\n\nMnemosyne makes it more efficient to study, focusing on the cards you\'re most likely to forget and not wasting your time on things you know well.\n\nFor that, Mnemosyne decides when to show you the cards, and you\'ll need to rate how well you remember them.\n\nLet\'s look at the meaning of these ratings now.'))
        self.grades02.setTitle(_('Memorising new cards'))
        self.grades02_lbl.setText(_('Grades range from 0 to 5.\n\nWhen you are learning new cards, use grades 0 and 1 to signal that you have not yet memorised them. Grade 1 cards are becoming more familiar than grade 0 cards, and will be repeated less often.\n\nThese cards will be repeatedly shown until you give them a grade 2 or higher. This means that you\'ve memorised the card and that you\'ll be able to remember it for one or two days. The \'Not memorised\' counter will decrease by one.\n\nThis card will be scheduled at some future date, when you\'re likely still be able to remember it with some effort, without having forgotten it completely. This is most efficient for the learning process.\n'))
        self.grades35.setTitle(_('Reviewing previously memorised cards'))
        self.grades35_lbl.setText(_('If you study these cards again tomorrow, the \'Scheduled\' counter will tell you how many previously memorised cards you need to review. These are grade 2 to 5 cards.\n\nIf a card reappears too soon, and you\'re able to remember it without any effort, rate the card a 5. The interval to see this card again will be a lot longer.\n\nIf the interval is just right, so that you remember it, albeit with some effort, use grade 4.\n\nIf, however, it takes you significant effort to remember the answer, and you think the interval was too long, then rate the card 3 or even 2.\n\nIf you fail to remember it altogether, rate it either 0 or 1, and after you have finished reviewing all the scheduled cards, it will appear repeatedly until you think you\'ll be able to remember it again for a few days.'))
        self.statistics.setTitle(_('Statistics'))
        self.statistics_lbl.setText(_('If you\'re into statistics, Mnemosyne keeps detailed logs of your revisions.\n\nNot only that, but if you want, Mnemosyne can upload transparently a completely anonymous version of these logs to a central site for analysis, so that you can help making the scheduling algorithm better. In this way, you also contribute to scientific research on long-term memory.\n\nUncheck the following box if you do not want to do this.'))
        self.upload_box.setText(_('Upload anonymous logs (can be changed later)'))
        self.ready.setTitle(_('Ready to start'))
        self.ready_lbl.setText(_('Now you\'re ready to start!\n\nAdd new cards by clicking on the icon with the \'plus\' sign in the top left.\n\nRemember, there is no need to worry about saving your work, this will be done automatically.\n\nFor best results, it\'s suggested to do your revisions every day, although Mnemosyne will try to cope if you\'ve missed a few days.\n\nFor more documentation, see http://www.mnemosyne-proj.org.\n\nHappy learning!'))

