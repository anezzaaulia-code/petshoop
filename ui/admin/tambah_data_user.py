# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# Pastikan struktur folder Anda sesuai agar import ini berjalan
from models.User import Admin 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # --- LABEL JUDUL ---
        self.label_judul = QtWidgets.QLabel(self.centralwidget)
        self.label_judul.setGeometry(QtCore.QRect(270, 40, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_judul.setFont(font)
        self.label_judul.setObjectName("label_judul")

        # --- INPUT NAMA ---
        self.label_nama = QtWidgets.QLabel(self.centralwidget)
        self.label_nama.setGeometry(QtCore.QRect(180, 170, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_nama.setFont(font)
        self.label_nama.setObjectName("label_nama")

        self.input_nama = QtWidgets.QLineEdit(self.centralwidget)
        self.input_nama.setGeometry(QtCore.QRect(280, 160, 291, 41))
        font.setPointSize(10)
        self.input_nama.setFont(font)
        self.input_nama.setStyleSheet(self.get_input_style())
        self.input_nama.setObjectName("input_nama")

        # --- INPUT USERNAME ---
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(150, 220, 91, 21))
        font.setPointSize(11)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")

        self.input_username = QtWidgets.QLineEdit(self.centralwidget)
        self.input_username.setGeometry(QtCore.QRect(280, 210, 291, 41))
        font.setPointSize(10)
        self.input_username.setFont(font)
        self.input_username.setStyleSheet(self.get_input_style())
        self.input_username.setObjectName("input_username")

        # --- INPUT PASSWORD ---
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(150, 270, 81, 20))
        font.setPointSize(11)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")

        self.input_password = QtWidgets.QLineEdit(self.centralwidget)
        self.input_password.setGeometry(QtCore.QRect(280, 260, 291, 41))
        font.setPointSize(10)
        self.input_password.setFont(font)
        self.input_password.setStyleSheet(self.get_input_style())
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password) # Agar password tersembunyi
        self.input_password.setObjectName("input_password")

        # --- COMBOBOX ROLE ---
        self.label_role = QtWidgets.QLabel(self.centralwidget)
        self.label_role.setGeometry(QtCore.QRect(180, 320, 55, 16))
        font.setPointSize(11)
        self.label_role.setFont(font)
        self.label_role.setObjectName("label_role")

        self.combo_role = QtWidgets.QComboBox(self.centralwidget)
        self.combo_role.setGeometry(QtCore.QRect(280, 310, 291, 41))
        self.combo_role.setObjectName("combo_role")
        self.combo_role.addItem("Admin")
        self.combo_role.addItem("Supervisor")
        self.combo_role.addItem("Kasir")
        self.combo_role.setStyleSheet("""
            QComboBox {
                background-color: #FFFFFF;
                border: 2px solid #555555;
                border-radius: 6px;
                padding: 4px;
                color: #333333;
                font-size: 16px;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)

        # --- BUTTON INSERT ---
        self.btn_insert = QtWidgets.QPushButton(self.centralwidget)
        self.btn_insert.setGeometry(QtCore.QRect(190, 380, 171, 41))
        font.setPointSize(11)
        self.btn_insert.setFont(font)
        self.btn_insert.setStyleSheet(self.get_button_style())
        self.btn_insert.setObjectName("btn_insert")

        # --- BUTTON BACK ---
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(400, 380, 171, 41))
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet(self.get_button_style())
        self.btn_back.setObjectName("btn_back")

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

        # --- EVENTS / AKSI ---
        self.btn_insert.clicked.connect(self.InsertDataUser)
        self.btn_back.clicked.connect(self.back)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Insert User Data"))
        self.label_judul.setText(_translate("MainWindow", "Insert Data User"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.label_username.setText(_translate("MainWindow", "Username"))
        self.label_nama.setText(_translate("MainWindow", "Nama"))
        self.label_role.setText(_translate("MainWindow", "Role"))
        self.btn_insert.setText(_translate("MainWindow", "Insert"))
        self.btn_back.setText(_translate("MainWindow", "Back"))

    # Helper untuk style agar kode setupUi tidak penuh
    def get_input_style(self):
        return """
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #555555;
                border-radius: 6px;
                padding: 4px;
            }
            QLineEdit:focus {
                border: 2px solid #333333;
            }
        """

    def get_button_style(self):
        return """
            QPushButton {
                background-color: #444444;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #333333;
            }
            QPushButton:pressed {
                background-color: #222222;
            }
        """

    def InsertDataUser(self):
        # Mengambil data dari input yang sudah di-rename
        nama = self.input_nama.text()
        username = self.input_username.text()
        password = self.input_password.text()
        role = self.combo_role.currentText()

        # Validasi sederhana
        if not nama or not username or not password:
            QtWidgets.QMessageBox.warning(None, "Peringatan", "Semua kolom harus diisi!")
            return

        try:
            # Gunakan class Admin karena hanya admin yg punya CRUD user
            admin = Admin()
            status = admin.tambah_user(nama, username, password, role)
            
            msg = QtWidgets.QMessageBox()
            if status:
                msg.setWindowTitle("Success")
                msg.setText("User berhasil ditambahkan.")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.exec_()

                # Clear input setelah sukses
                self.input_nama.clear()
                self.input_username.clear()
                self.input_password.clear()
                self.combo_role.setCurrentIndex(0)
            else:
                msg.setWindowTitle("Error")
                msg.setText("Gagal menambahkan user! Username mungkin sudah ada.")
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.exec_()
                
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error System", f"Terjadi kesalahan: {str(e)}")

    def back(self):
        # Import di dalam fungsi untuk menghindari circular import jika dashboard_admin juga mengimport file ini
        try:
            from dashboard.dashboard_admin import Ui_MainWindow as DashboardAdmin
            self.dashboard_window = QtWidgets.QMainWindow()
            self.dashboard = DashboardAdmin()
            self.dashboard.setupUi(self.dashboard_window)
            self.dashboard_window.show()
            self.main_window.close()
        except ImportError:
            print("File dashboard/dashboard_admin.py tidak ditemukan.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())