# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard_admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is

import ui.form_login as login
import ui.admin.tambah_data_user as tu
import ui.admin.edit_data_user as eu
import ui.admin.delete_data_user as du
import ui.admin.lihat_data_user as lu
from PyQt5 import QtWidgets, QtCore, QtGui

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                self.MainWindow = MainWindow
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(240, 20, 351, 51))
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(140, 170, 231, 121))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("background: qlineargradient(\n"
        "    x1:0, y1:0, x2:1, y2:1,\n"
        "    stop:0 #66d9a3,\n"
        "    stop:1 #33cc88\n"
        ");\n"
        "color: white;\n"
        "border-radius: 8px;\n"
        "")
                self.pushButton.setObjectName("pushButton")
                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_2.setGeometry(QtCore.QRect(140, 330, 231, 121))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_2.setFont(font)
                self.pushButton_2.setStyleSheet("QPushButton {\n"
        "    background: qlineargradient(\n"
        "        x1:0, y1:0, x2:1, y2:1,\n"
        "        stop:0 #ff9aa2,   /* soft pink-ish red */\n"
        "        stop:1 #ff6f6f    /* soft coral red */\n"
        "    );\n"
        "    color: white;\n"
        "    border: none;\n"
        "    border-radius: 8px;\n"
        "    padding: 6px 14px;\n"
        "    font-weight: bold;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qlineargradient(\n"
        "        x1:0, y1:0, x2:1, y2:1,\n"
        "        stop:0 #ff8c99,\n"
        "        stop:1 #ff5f5f\n"
        "    );\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background: #e85c5c;\n"
        "}\n"
        "")
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_3.setGeometry(QtCore.QRect(410, 330, 231, 121))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_3.setFont(font)
                self.pushButton_3.setStyleSheet("background: qlineargradient(\n"
        "    x1:0, y1:0, x2:1, y2:1,\n"
        "    stop:0 #d9d9d9,\n"
        "    stop:1 #bfbfbf\n"
        ");\n"
        "color: black;\n"
        "border-radius: 8px;\n"
        "")
                self.pushButton_3.setObjectName("pushButton_3")
                self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_logout.setGeometry(QtCore.QRect(640, 20, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_logout.setFont(font)
                self.pushButton_logout.setStyleSheet("QPushButton {\n"
        "    background-color: #4A4A4A;\n"
        "    color: white;\n"
        "    border: none;\n"
        "    border-radius: 8px;\n"
        "    padding: 6px 14px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: #3A3A3A;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: #2E2E2E;\n"
        "}\n"
        "")
                self.pushButton_logout.setObjectName("pushButton_logout")
                self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_4.setGeometry(QtCore.QRect(410, 170, 231, 121))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_4.setFont(font)
                self.pushButton_4.setStyleSheet("background: qlineargradient(\n"
        "    x1:0, y1:0, x2:1, y2:1,\n"
        "    stop:0 #4da6ff,\n"
        "    stop:1 #1a75ff\n"
        ");\n"
        "color: white;\n"
        "border-radius: 8px;\n"
        "padding: 6px 14px;\n"
        "")
                self.pushButton_4.setObjectName("pushButton_4")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                # aksi
                self.pushButton.clicked.connect(self.openInsertDataUser)        
                self.pushButton_2.clicked.connect(self.openDeleteDataUser)       
                self.pushButton_3.clicked.connect(self.openTampilDataUser)        
                self.pushButton_4.clicked.connect(self.openEditDataUser)   
                self.pushButton_logout.clicked.connect(self.logout)    

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "DASHBOARD ADMIN"))
                self.pushButton.setText(_translate("MainWindow", "INSERT DATA USER"))
                self.pushButton_2.setText(_translate("MainWindow", "DELETE DATA USER"))
                self.pushButton_3.setText(_translate("MainWindow", "LIHAT DATA USER"))
                self.pushButton_logout.setText(_translate("MainWindow", "LOGOUT"))
                self.pushButton_4.setText(_translate("MainWindow", "UPDATE DATA USER"))

        def openInsertDataUser(self):
                self.window = QtWidgets.QMainWindow()
                self.ui_other = tu.Ui_MainWindow()
                self.ui_other.setupUi(self.window)
                self.ui_other.dashboard = self.MainWindow    
                self.window.show()
                self.centralwidget.window().hide()

        def openEditDataUser(self):
                self.window = QtWidgets.QMainWindow()
                self.ui_other = eu.Ui_MainWindow()
                self.ui_other.setupUi(self.window)
                self.ui_other.dashboard = self.MainWindow    
                self.window.show()
                self.centralwidget.window().hide()

        def openDeleteDataUser(self):
                self.window = QtWidgets.QMainWindow()
                self.ui_other = du.Ui_MainWindow() 
                self.ui_other.setupUi(self.window)
                self.ui_other.dashboard = self.MainWindow   
                self.window.show()
                self.centralwidget.window().hide()

        def openTampilDataUser(self):
                self.window = QtWidgets.QMainWindow()
                self.ui_other = lu.Ui_MainWindow()
                self.ui_other.setupUi(self.window)
                self.ui_other.dashboard = self.MainWindow   
                self.window.show()
                self.centralwidget.window().hide()

        def logout(self):
                self.window = QtWidgets.QMainWindow()
                self.login = login.Ui_MainWindow()
                self.login.setupUi(self.window)
                self.window.show()
                self.centralwidget.window().hide()

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
