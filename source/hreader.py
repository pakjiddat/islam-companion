# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hreader.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hadithText = QtWidgets.QTextEdit(self.centralwidget)
        self.hadithText.setGeometry(QtCore.QRect(20, 100, 701, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hadithText.sizePolicy().hasHeightForWidth())
        self.hadithText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nafees [PYRS]")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.hadithText.setFont(font)
        self.hadithText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hadithText.setStyleSheet("")
        self.hadithText.setLocale(QtCore.QLocale(QtCore.QLocale.Urdu, QtCore.QLocale.Pakistan))
        self.hadithText.setReadOnly(True)
        self.hadithText.setObjectName("hadithText")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 701, 79))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.bookComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.bookComboBox.setBaseSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Nafees [PYRS]")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.bookComboBox.setFont(font)
        self.bookComboBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.bookComboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Urdu, QtCore.QLocale.Pakistan))
        self.bookComboBox.setObjectName("bookComboBox")
        self.gridLayout.addWidget(self.bookComboBox, 5, 9, 1, 1)
        self.sourceLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sourceLabel.setFont(font)
        self.sourceLabel.setLocale(QtCore.QLocale(QtCore.QLocale.Urdu, QtCore.QLocale.Pakistan))
        self.sourceLabel.setObjectName("sourceLabel")
        self.gridLayout.addWidget(self.sourceLabel, 2, 10, 1, 1)
        self.randomButton = QtWidgets.QToolButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.randomButton.setFont(font)
        self.randomButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.randomButton.setLocale(QtCore.QLocale(QtCore.QLocale.Urdu, QtCore.QLocale.Pakistan))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/local/share/islamcompanion/random.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.randomButton.setIcon(icon)
        self.randomButton.setArrowType(QtCore.Qt.NoArrow)
        self.randomButton.setObjectName("randomButton")
        self.gridLayout.addWidget(self.randomButton, 5, 4, 1, 1)
        self.sourceComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.sourceComboBox.setBaseSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Nafees [PYRS]")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.sourceComboBox.setFont(font)
        self.sourceComboBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sourceComboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Urdu, QtCore.QLocale.Pakistan))
        self.sourceComboBox.setObjectName("sourceComboBox")
        self.gridLayout.addWidget(self.sourceComboBox, 5, 10, 1, 1)
        self.titleComboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nafees [PYRS]")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.titleComboBox.setFont(font)
        self.titleComboBox.setToolTip("")
        self.titleComboBox.setWhatsThis("")
        self.titleComboBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.titleComboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Urdu, QtCore.QLocale.Pakistan))
        self.titleComboBox.setEditable(False)
        self.titleComboBox.setObjectName("titleComboBox")
        self.gridLayout.addWidget(self.titleComboBox, 5, 5, 1, 1)
        self.nextButton = QtWidgets.QToolButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nextButton.setFont(font)
        self.nextButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.nextButton.setLocale(QtCore.QLocale(QtCore.QLocale.Urdu, QtCore.QLocale.Pakistan))
        self.nextButton.setArrowType(QtCore.Qt.LeftArrow)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 5, 1, 1, 1)
        self.bookLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bookLabel.setFont(font)
        self.bookLabel.setLocale(QtCore.QLocale(QtCore.QLocale.Urdu, QtCore.QLocale.Pakistan))
        self.bookLabel.setObjectName("bookLabel")
        self.gridLayout.addWidget(self.bookLabel, 2, 9, 1, 1)
        self.prevButton = QtWidgets.QToolButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.prevButton.setFont(font)
        self.prevButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.prevButton.setLocale(QtCore.QLocale(QtCore.QLocale.Urdu, QtCore.QLocale.Pakistan))
        self.prevButton.setArrowType(QtCore.Qt.RightArrow)
        self.prevButton.setObjectName("prevButton")
        self.gridLayout.addWidget(self.prevButton, 5, 3, 1, 1)
        self.titleLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setLocale(QtCore.QLocale(QtCore.QLocale.Urdu, QtCore.QLocale.Pakistan))
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 2, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 744, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuLanguage = QtWidgets.QMenu(self.menuBar)
        self.menuLanguage.setToolTip("")
        self.menuLanguage.setStatusTip("")
        self.menuLanguage.setObjectName("menuLanguage")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.langGroup = QtWidgets.QActionGroup(MainWindow)
        self.langGroup.setObjectName("langGroup")
        self.actionUrdu = QtWidgets.QAction(self.langGroup)
        self.actionUrdu.setCheckable(True)
        self.actionUrdu.setChecked(True)
        self.actionUrdu.setObjectName("actionUrdu")
        self.actionEnglish = QtWidgets.QAction(self.langGroup)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionArabic = QtWidgets.QAction(self.langGroup)
        self.actionArabic.setCheckable(True)
        self.actionArabic.setObjectName("actionArabic")
        self.menuLanguage.addAction(self.actionUrdu)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionArabic)
        self.menuBar.addAction(self.menuLanguage.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hadithText.setStatusTip(_translate("MainWindow", "Hadith Text"))
        self.bookComboBox.setStatusTip(_translate("MainWindow", "Hadith Book"))
        self.sourceLabel.setText(_translate("MainWindow", "Source"))
        self.randomButton.setStatusTip(_translate("MainWindow", "(Ctrl+R) Random Hadith"))
        self.randomButton.setText(_translate("MainWindow", "Random"))
        self.randomButton.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.sourceComboBox.setStatusTip(_translate("MainWindow", "Hadith Source"))
        self.titleComboBox.setStatusTip(_translate("MainWindow", "Hadith Title"))
        self.nextButton.setStatusTip(_translate("MainWindow", "(Ctrl+N) Next Hadith"))
        self.nextButton.setText(_translate("MainWindow", "..."))
        self.nextButton.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.bookLabel.setText(_translate("MainWindow", "Book"))
        self.prevButton.setStatusTip(_translate("MainWindow", "(Ctrl+P) Previous Hadith"))
        self.prevButton.setText(_translate("MainWindow", "..."))
        self.prevButton.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.titleLabel.setText(_translate("MainWindow", "Title"))
        self.statusbar.setStatusTip(_translate("MainWindow", "Hadith Reader"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.actionExit.setText(_translate("MainWindow", "Settings"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionUrdu.setText(_translate("MainWindow", "Urdu"))
        self.actionUrdu.setStatusTip(_translate("MainWindow", "Change language to Urdu"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionEnglish.setStatusTip(_translate("MainWindow", "Change language to English"))
        self.actionArabic.setText(_translate("MainWindow", "Arabic"))
        self.actionArabic.setStatusTip(_translate("MainWindow", "Change language to Arabic"))
