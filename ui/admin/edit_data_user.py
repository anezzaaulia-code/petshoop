# -*- coding: utf-8 -*-

from models.User import Admin
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main_window = MainWindow 
        self.admin = Admin()    
        MainWindow.setObjectName("MainWindow")
        
        # --- UKURAN WINDOW (SAMA DENGAN TAMBAH USER) ---
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
        self.label.setText("Update Data User")
        self.label.setStyleSheet("color: #0F172A;")

        # --- STYLES (KONSISTEN DENGAN DESAIN SEBELUMNYA) ---
        style_input = """
            QLineEdit, QComboBox {
                border: 2px solid #E2E8F0;
                border-radius: 10px;
                padding: 5px 15px;
                font-size: 18px; /* Font Besar */
                font-weight: 500;
                color: #334155;
                background-color: #F8FAFC; 
            }
            QLineEdit:focus, QComboBox:focus {
                border: 2px solid #4338CA; 
                background-color: #FFFFFF;
            }
            QComboBox::drop-down { border:0; margin-right: 20px; }
        """
        
        style_label = """
            QLabel {
                font-weight: bold; 
                font-size: 20px; /* Font Label Besar */
                color: #1E293B;
            }
        """

        # --- LAYOUT LOGIC ---
        w_label = 200
        w_input_full = 500 # Lebar input normal
        gap_h = 20
        
        # Hitung Center
        total_width = w_label + gap_h + w_input_full
        start_x = (w_win - total_width) // 2
        
        x_label = start_x
        x_input = start_x + w_label + gap_h
        
        start_y = 110
        row_height = 60
        gap_v = 85 # Spacing vertikal

        current_y = start_y

        # === BARIS 1: USERNAME & TOMBOL CARI ===
        w_btn_cari = 130
        w_input_username = w_input_full - w_btn_cari - 10 

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_4.setText("Username")
        self.label_4.setStyleSheet(style_label)
        self.label_4.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        # Input Username (TETAP ADA PLACEHOLDER)
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

        # === BARIS 2: NAMA ===
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_5.setText("Nama Lengkap")
        self.label_5.setStyleSheet(style_label)
        self.label_5.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(x_input, current_y, w_input_full, row_height))
        self.lineEdit_3.setStyleSheet(style_input)

        current_y += gap_v

        # === BARIS 3: PASSWORD ===
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_3.setText("Password Baru")
        self.label_3.setStyleSheet(style_label)
        self.label_3.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        # Input Password (PLACEHOLDER DIHILANGKAN)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(x_input, current_y, w_input_full, row_height))
        self.lineEdit_4.setStyleSheet(style_input)
        # self.lineEdit_4.setPlaceholderText("Isi jika ingin mengubah password") # Baris ini dihapus

        current_y += gap_v

        # === BARIS 4: ROLE ===
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_6.setText("Role Access")
        self.label_6.setStyleSheet(style_label)
        self.label_6.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.comboBox_level = QtWidgets.QComboBox(self.frame)
        self.comboBox_level.setGeometry(QtCore.QRect(x_input, current_y, w_input_full, row_height))
        self.comboBox_level.addItems(["Admin", "Supervisor", "Kasir"])
        self.comboBox_level.setStyleSheet(style_input)

        current_y += 100 # Jarak ke tombol bawah

        # === TOMBOL AKSI (BESAR & SEIMBANG) ===
        btn_width = 240
        btn_height = 65

        # Tombol Update
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(x_input, current_y, btn_width, btn_height))
        self.pushButton_3.setText("UPDATE")
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("""
            QPushButton {
                background-color: #4F46E5; 
                color: white; 
                font-weight: bold; 
                font-size: 20px;
                border-radius: 10px;
                border: none;
            }
            QPushButton:hover { background-color: #4338CA; }
            QPushButton:pressed { background-color: #3730A3; }
        """)

        # Tombol Kembali
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(x_input + btn_width + 20, current_y, btn_width, btn_height))
        self.pushButton_2.setText("BATAL")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("""
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, w_win, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # AKSI
        self.pushButton.clicked.connect(self.CariUser)
        self.pushButton_3.clicked.connect(self.UpdateUser)
        self.pushButton_2.clicked.connect(self.back)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin Panel - Update User"))

    # ================= LOGIC (TETAP SAMA) =================

    def CariUser(self):
        username = self.lineEdit_2.text().strip()
        if username == "":
            QtWidgets.QMessageBox.warning(self.main_window, "Error", "Masukkan username yang ingin dicari!")
            return

        data = self.admin.select_by_username(username)
        if not data:
            QtWidgets.QMessageBox.warning(self.main_window, "Error", "User tidak ditemukan!")
            return

        self.lineEdit_3.setText(str(data[0]))  # nama
        self.lineEdit_2.setText(str(data[1]))  # username
        self.lineEdit_4.setText(str(data[2]))  # password
        self.comboBox_level.setCurrentText(str(data[3]).capitalize())
        self.old_username = data[1]

    def UpdateUser(self):
        if not hasattr(self, "old_username") or self.old_username is None:
            QtWidgets.QMessageBox.warning(self.main_window, "Error", "Cari user dulu sebelum update!")
            return

        new_username = self.lineEdit_2.text().strip()
        new_nama = self.lineEdit_3.text().strip()
        new_password = self.lineEdit_4.text().strip()
        new_role = self.comboBox_level.currentText()

        if not new_username or not new_nama or not new_password:
            QtWidgets.QMessageBox.warning(self.main_window, "Error", "Semua field harus diisi!")
            return

        try:
            self.admin.update_user(
                nama=new_nama,
                username=new_username,
                password=new_password,
                role=new_role,
                old_username=self.old_username
            )
            QtWidgets.QMessageBox.information(self.main_window, "Success", "Data user berhasil diperbarui!")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self.main_window, "Error", f"Gagal update user: {e}")

    def back(self):
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