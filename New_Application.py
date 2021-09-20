# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Application.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Application(object):
    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(954, 387)
        font = QtGui.QFont()
        font.setPointSize(9)
        Application.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Application)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 60, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 70, 431, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(790, 70, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 210, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(420, 280, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(20, 320, 281, 31))
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(310, 150, 161, 41))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEdit.setObjectName("dateEdit")
        self.label2_2 = QtWidgets.QLabel(self.centralwidget)
        self.label2_2.setGeometry(QtCore.QRect(20, 150, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label2_2.setFont(font)
        self.label2_2.setObjectName("label2_2")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(310, 211, 171, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        
        Application.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(Application)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 954, 18))
        self.menuBar.setObjectName("menuBar")
        Application.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(Application)
        self.statusbar.setObjectName("statusbar")
        Application.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(Application)
        self.actionAbout.setCheckable(False)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(Application)
        QtCore.QMetaObject.connectSlotsByName(Application)

    def retranslateUi(self, Application):
        _translate = QtCore.QCoreApplication.translate
        Application.setWindowTitle(_translate("Application", "MainWindow"))
        self.label1.setText(_translate("Application", "   Select the Configuration File"))
        self.button1.setText(_translate("Application", "Browse"))
        self.label2.setText(_translate("Application", "   Select Graph Type"))
        self.button2.setText(_translate("Application", "Download"))
        self.dateEdit.setDisplayFormat(_translate("Application", "yyyy-MM-dd"))
        self.label2_2.setText(_translate("Application", "   Select Date"))
        self.comboBox.setItemText(0, _translate("Application", "MAB Graphs"))
        self.comboBox.setItemText(1, _translate("Application", "WGC Graphs"))
        self.comboBox.setItemText(2, _translate("Application", "DMDC Graphs"))
        self.actionAbout.setText(_translate("Application", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Application = QtWidgets.QMainWindow()
    ui = Ui_Application()
    ui.setupUi(Application)
    Application.show()
    sys.exit(app.exec_())
