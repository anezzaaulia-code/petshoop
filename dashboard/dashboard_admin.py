# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard_admin.ui'
# Created by: PyQt5 UI code generator 5.15.11

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
        
        # --- BACKGROUND ---
        # Warna background abu-abu soft
        MainWindow.setStyleSheet("QMainWindow { background-color: #f4f7f6; }")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # --- TOMBOL LOGOUT (POSISI DI ATAS SENDIRI) ---
        # Posisi Y=20 (Pojok Kanan Atas)
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(630, 20, 140, 45))
        self.pushButton_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        # Style Logout
        self.pushButton_logout.setStyleSheet("""
            QPushButton {
                background-color: #455a64;
                color: white;
                border-radius: 8px;
                font-family: 'Segoe UI';
                font-weight: 600;
                font-size: 13px;
                border: 1px solid #37474f;
            }
            QPushButton:hover {
                background-color: #607d8b;
                border: 1px solid #78909c;
            }
            QPushButton:pressed {
                background-color: #37474f;
            }
        """)
        self.pushButton_logout.setObjectName("pushButton_logout")

        # --- LABEL JUDUL (ADA JARAK DENGAN LOGOUT) ---
        # Posisi Y=90 (Turun ke bawah agar ada jarak dengan tombol logout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 90, 800, 50)) 
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24) # Font judul besar
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #2c3e50; letter-spacing: 1px;") 
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # --- STYLE DASAR TOMBOL UTAMA ---
        # Font diperbesar menjadi 16px (Request: sedikit besarkan)
        base_btn_style = """
            QPushButton {
                border-radius: 15px;
                color: white;
                font-family: 'Segoe UI', sans-serif;
                font-size: 16px; 
                font-weight: bold;
                letter-spacing: 0.5px;
                padding-bottom: 4px; /* Agar teks pas di tengah */
            }
            QPushButton:pressed {
                padding-top: 2px;
                padding-left: 2px;
            }
        """

        # --- BARIS 1: INSERT & UPDATE (Posisi Y=180 -> 210) ---
        # Diturunkan agar tidak mepet judul

        # TOMBOL INSERT (HIJAU GRADASI)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 231, 120))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(base_btn_style + """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y1:1, stop:0 #11998e, stop:1 #38ef7d);
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y1:1, stop:0 #13a69a, stop:1 #4df18c);
                border: 2px solid #baffc9;
            }
        """)
        self.pushButton.setObjectName("pushButton")

        # TOMBOL UPDATE (BIRU GRADASI)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 210, 231, 120))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(base_btn_style + """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y1:1, stop:0 #2193b0, stop:1 #6dd5ed);
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y1:1, stop:0 #25a2c2, stop:1 #7ce0f5);
                border: 2px solid #cceeff;
            }
        """)
        self.pushButton_4.setObjectName("pushButton_4")

        # --- BARIS 2: DELETE & VIEW (Posisi Y=340 -> 360) ---
        
        # TOMBOL DELETE (MERAH GRADASI)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 360, 231, 120))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(base_btn_style + """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y1:1, stop:0 #cb2d3e, stop:1 #ef473a);
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y1:1, stop:0 #d63041, stop:1 #ff5e50);
                border: 2px solid #ffb3b3;
            }
        """)
        self.pushButton_2.setObjectName("pushButton_2")

        # TOMBOL LIHAT DATA (UNGU GRADASI)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 360, 231, 120))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(base_btn_style + """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y1:1, stop:0 #834d9b, stop:1 #d04ed6);
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y1:1, stop:0 #9054aa, stop:1 #e05ee6);
                border: 2px solid #f3ccff;
            }
        """)
        self.pushButton_3.setObjectName("pushButton_3")

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

        # AKSI
        self.pushButton.clicked.connect(self.openInsertDataUser)
        self.pushButton_2.clicked.connect(self.openDeleteDataUser)
        self.pushButton_3.clicked.connect(self.openTampilDataUser)
        self.pushButton_4.clicked.connect(self.openEditDataUser)
        self.pushButton_logout.clicked.connect(self.logout)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard Admin"))
        self.label.setText(_translate("MainWindow", "DASHBOARD ADMIN"))
        
        # Teks tombol dengan spasi agar font besar tetap terlihat proporsional
        self.pushButton.setText(_translate("MainWindow", "INSERT DATA"))
        self.pushButton_2.setText(_translate("MainWindow", "DELETE DATA"))
        self.pushButton_3.setText(_translate("MainWindow", "LIHAT DATA"))
        self.pushButton_logout.setText(_translate("MainWindow", "LOGOUT"))
        self.pushButton_4.setText(_translate("MainWindow", "UPDATE DATA"))

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