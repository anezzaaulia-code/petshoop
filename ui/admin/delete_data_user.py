# -*- coding: utf-8 -*-

from models.User import Admin
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        
        # --- UKURAN WINDOW (SAMA DENGAN UPDATE/ADD) ---
        w_win = 850
        h_win = 600
        MainWindow.resize(w_win, h_win)
        
        # --- GLOBAL STYLE ---
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #FFFFFF;
            }
            QLabel {
                font-family: 'Segoe UI', sans-serif;
                color: #1E293B;
            }
            QWidget {
                font-family: 'Segoe UI', sans-serif;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, w_win, h_win))
        self.frame.setStyleSheet("background: transparent; border: none;")

        # --- JUDUL (BESAR & TEGAS) ---
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 20, w_win, 60))
        font_judul = QtGui.QFont("Segoe UI", 25, QtGui.QFont.Bold)
        self.label.setFont(font_judul)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Hapus Data User")
        self.label.setStyleSheet("color: #0F172A;")

        # --- STYLES ---
        # Style Input (Untuk Search)
        style_input = """
            QLineEdit {
                border: 2px solid #E2E8F0;
                border-radius: 10px;
                padding: 5px 15px;
                font-size: 18px; 
                font-weight: 500;
                color: #334155;
                background-color: #F8FAFC; 
            }
            QLineEdit:focus {
                border: 2px solid #4338CA; 
                background-color: #FFFFFF;
            }
        """
        
        # Style Data Display (Label yang didesain mirip Input agar rapi)
        style_display = """
            QLabel {
                border: 2px solid #E2E8F0;
                border-radius: 10px;
                padding: 5px 15px;
                font-size: 18px;
                color: #64748B; /* Warna teks agak abu menandakan Read-Only */
                background-color: #F1F5F9; /* Background agak gelap */
            }
        """
        
        style_label_judul = """
            QLabel {
                font-weight: bold; 
                font-size: 20px; 
                color: #1E293B;
            }
        """

        # --- LAYOUT LOGIC ---
        w_label = 200
        w_input_full = 500
        gap_h = 20
        
        # Hitung Center
        total_width = w_label + gap_h + w_input_full
        start_x = (w_win - total_width) // 2
        
        x_label = start_x
        x_input = start_x + w_label + gap_h
        
        start_y = 110
        row_height = 60
        gap_v = 85 

        current_y = start_y

        # === BARIS 1: USERNAME & CARI ===
        w_btn_cari = 130
        w_input_username = w_input_full - w_btn_cari - 10 

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_4.setText("Username")
        self.label_4.setStyleSheet(style_label_judul)
        self.label_4.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        # Input Search
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(x_input, current_y, w_input_username, row_height))
        self.lineEdit_2.setStyleSheet(style_input)
        self.lineEdit_2.setPlaceholderText("Cari username...")

        # Tombol Cari
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(x_input + w_input_username + 10, current_y, w_btn_cari, row_height))
        self.pushButton.setText("CARI")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #1E293B; 
                color: white; 
                font-weight: bold; 
                font-size: 16px;
                border-radius: 10px;
            }
            QPushButton:hover { background-color: #334155; }
        """)

        current_y += gap_v

        # === BARIS 2: NAMA (READ ONLY) ===
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_5.setText("Nama Lengkap")
        self.label_5.setStyleSheet(style_label_judul)
        self.label_5.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(x_input, current_y, w_input_full, row_height))
        self.label_7.setStyleSheet(style_display)
        self.label_7.setText("-") # Default placeholder

        current_y += gap_v

        # === BARIS 3: PASSWORD (READ ONLY) ===
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_3.setText("Password")
        self.label_3.setStyleSheet(style_label_judul)
        self.label_3.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(x_input, current_y, w_input_full, row_height))
        self.label_8.setStyleSheet(style_display)
        self.label_8.setText("-")

        current_y += gap_v

        # === BARIS 4: ROLE (READ ONLY) ===
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_6.setText("Role Access")
        self.label_6.setStyleSheet(style_label_judul)
        self.label_6.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(x_input, current_y, w_input_full, row_height))
        self.label_9.setStyleSheet(style_display)
        self.label_9.setText("-")

        current_y += 100 # Jarak ke tombol

        # === TOMBOL AKSI ===
        btn_width = 240
        btn_height = 65

        # Tombol DELETE (MERAH - Danger Zone)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(x_input, current_y, btn_width, btn_height))
        self.pushButton_2.setText("HAPUS")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: #DC2626; /* Merah */
                color: white; 
                font-weight: bold; 
                font-size: 20px;
                border-radius: 10px;
                border: none;
            }
            QPushButton:hover { background-color: #B91C1C; }
            QPushButton:pressed { background-color: #991B1B; }
        """)

        # Tombol BACK
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(x_input + btn_width + 20, current_y, btn_width, btn_height))
        self.pushButton_3.setText("BATAL")
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("""
            QPushButton {
                background-color: white; 
                color: #64748B; 
                font-weight: bold; 
                font-size: 20px;
                border: 3px solid #E2E8F0; 
                border-radius: 10px;
            }
            QPushButton:hover { 
                background-color: #F1F5F9; 
                color: #334155; 
                border-color: #CBD5E1; 
            }
        """)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, w_win, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # AKSI
        self.pushButton.clicked.connect(self.CariUser)
        self.pushButton_2.clicked.connect(self.HapusUser)
        self.pushButton_3.clicked.connect(self.back)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin Panel - Delete User"))

    def CariUser(self):
        username = self.lineEdit_2.text().strip()

        if username == "":
            QMessageBox.warning(None, "Peringatan", "Username tidak boleh kosong!")
            return

        data = Admin().select_by_username(username)

        if not data:
            QMessageBox.warning(None, "Tidak Ditemukan", "User tidak ditemukan!")
            self.label_7.setText("-")
            self.label_8.setText("-")
            self.label_9.setText("-")
            return

        if len(data) != 4:
            QMessageBox.warning(None, "Error", "Format data user tidak valid!")
            return

        nama, user, password, role = data

        # TAMPILKAN KE LABEL
        self.label_7.setText(nama)
        self.label_8.setText(password)
        self.label_9.setText(role)

    def HapusUser(self):
        username = self.lineEdit_2.text().strip()

        if username == "":
            QMessageBox.warning(None, "Peringatan", "Cari user terlebih dahulu!")
            return
        
        # Cek apakah data sudah tampil (validasi ganda)
        if self.label_7.text() == "-" or self.label_7.text() == "":
             QMessageBox.warning(None, "Peringatan", "Silahkan klik tombol CARI terlebih dahulu.")
             return

        confirm = QMessageBox.question(None, "Konfirmasi", 
                                     f"Apakah Anda yakin ingin menghapus user '{username}'?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if confirm == QMessageBox.Yes:
            cek = Admin().select_by_username(username)
            if not cek:
                QMessageBox.warning(None, "Error", "User tidak ditemukan di database!")
                return

            Admin().delete_user(username)

            QMessageBox.information(None, "Berhasil", "User berhasil dihapus.")

            # CLEAR
            self.lineEdit_2.setText("")
            self.label_7.setText("-")
            self.label_8.setText("-")
            self.label_9.setText("-")

    def back(self):
        try:
            from dashboard.dashboard_admin import Ui_MainWindow
            self.dashboard_window = QtWidgets.QMainWindow()
            self.dashboard = Ui_MainWindow()
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