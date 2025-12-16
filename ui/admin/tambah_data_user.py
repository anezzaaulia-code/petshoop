# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from models.User import Admin 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        
        # --- UKURAN WINDOW (Compact tapi Padat) ---
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
        self.frame.setStyleSheet("background-color: transparent; border: none;")
        
        # --- 1. JUDUL (BESAR & TEGAS) ---
        self.label_judul = QtWidgets.QLabel(self.frame)
        self.label_judul.setGeometry(QtCore.QRect(0, 20, w_win, 60))
        # Font judul diperbesar jadi 32px
        font_judul = QtGui.QFont("Segoe UI", 25, QtGui.QFont.Bold)
        self.label_judul.setFont(font_judul)
        self.label_judul.setAlignment(QtCore.Qt.AlignCenter)
        self.label_judul.setText("Tambah User Baru")
        self.label_judul.setStyleSheet("color: #0F172A;")

        # --- STYLE INPUT (Lebih Besar) ---
        style_input = """
            QLineEdit, QComboBox {
                border: 2px solid #E2E8F0;
                border-radius: 10px;
                padding: 5px 15px;
                font-size: 18px; /* Font Input Besar */
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
        
        # --- STYLE LABEL (Lebih Besar) ---
        style_label = """
            QLabel {
                font-weight: bold; 
                font-size: 20px; /* Font Label Besar */
                color: #1E293B;
            }
        """

        # --- LAYOUT LOGIC (MENGISI RUANG KOSONG) ---
        # Agar tidak banyak space kosong, kita perlebar inputnya.
        
        w_label = 200     # Label lebih lebar
        w_input = 500     # Input sangat lebar
        gap_h = 20        # Jarak horizontal kecil
        
        # Hitung posisi X agar center
        total_content_width = w_label + gap_h + w_input
        start_x = (w_win - total_content_width) // 2
        
        x_label = start_x
        x_input = start_x + w_label + gap_h
        
        # Layout Vertikal (Disebar merata)
        start_y = 110
        row_height = 60   # Tinggi komponen input (lebih gemuk)
        gap_v = 85        # Jarak vertikal antar baris (agar mengisi layar ke bawah)

        current_y = start_y

        # --- FORM INPUT ---

        # 1. NAMA
        self.label_nama = QtWidgets.QLabel(self.frame)
        self.label_nama.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_nama.setText("Nama Lengkap")
        self.label_nama.setStyleSheet(style_label)
        self.label_nama.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter) 

        self.input_nama = QtWidgets.QLineEdit(self.frame)
        self.input_nama.setGeometry(QtCore.QRect(x_input, current_y, w_input, row_height))
        self.input_nama.setStyleSheet(style_input)

        current_y += gap_v

        # 2. USERNAME
        self.label_username = QtWidgets.QLabel(self.frame)
        self.label_username.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_username.setText("Username")
        self.label_username.setStyleSheet(style_label)
        self.label_username.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.input_username = QtWidgets.QLineEdit(self.frame)
        self.input_username.setGeometry(QtCore.QRect(x_input, current_y, w_input, row_height))
        self.input_username.setStyleSheet(style_input)

        current_y += gap_v

        # 3. PASSWORD
        self.label_password = QtWidgets.QLabel(self.frame)
        self.label_password.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_password.setText("Password")
        self.label_password.setStyleSheet(style_label)
        self.label_password.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.input_password = QtWidgets.QLineEdit(self.frame)
        self.input_password.setGeometry(QtCore.QRect(x_input, current_y, w_input, row_height))
        self.input_password.setStyleSheet(style_input)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)

        current_y += gap_v

        # 4. ROLE
        self.label_role = QtWidgets.QLabel(self.frame)
        self.label_role.setGeometry(QtCore.QRect(x_label, current_y, w_label, row_height))
        self.label_role.setText("Role Access")
        self.label_role.setStyleSheet(style_label)
        self.label_role.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.combo_role = QtWidgets.QComboBox(self.frame)
        self.combo_role.setGeometry(QtCore.QRect(x_input, current_y, w_input, row_height))
        self.combo_role.addItems(["Admin", "Supervisor", "Kasir"])
        self.combo_role.setStyleSheet(style_input)

        # --- TOMBOL (BESAR & MEMENUHI) ---
        current_y += 100 # Jarak agak jauh dari form terakhir

        # Kita buat tombolnya selebar input field (dibagi 2)
        # Lebar input = 500. Gap tombol = 20.
        # (500 - 20) / 2 = 240 per tombol
        
        btn_width = 240
        btn_height = 65 # Tombol tinggi dan gagah
        
        # Tombol Simpan
        self.btn_insert = QtWidgets.QPushButton(self.frame)
        self.btn_insert.setGeometry(QtCore.QRect(x_input, current_y, btn_width, btn_height))
        self.btn_insert.setText("SIMPAN")
        self.btn_insert.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_insert.setStyleSheet("""
            QPushButton {
                background-color: #4338CA;
                color: white; 
                font-weight: bold; 
                font-size: 20px; /* Font Tombol Besar */
                border-radius: 10px; 
                border: none;
            }
            QPushButton:hover { background-color: #3730A3; }
            QPushButton:pressed { background-color: #312E81; }
        """)

        # Tombol Batal
        self.btn_back = QtWidgets.QPushButton(self.frame)
        self.btn_back.setGeometry(QtCore.QRect(x_input + btn_width + 20, current_y, btn_width, btn_height))
        self.btn_back.setText("BATAL")
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setStyleSheet("""
            QPushButton {
                background-color: white; 
                color: #64748B; 
                font-weight: bold; 
                font-size: 20px; /* Font Tombol Besar */
                border: 3px solid #E2E8F0; /* Border lebih tebal */
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

        # --- EVENTS ---
        self.btn_insert.clicked.connect(self.InsertDataUser)
        self.btn_back.clicked.connect(self.back)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin Panel - Add User"))

    def InsertDataUser(self):
        nama = self.input_nama.text()
        username = self.input_username.text()
        password = self.input_password.text()
        role = self.combo_role.currentText()

        if not nama or not username or not password:
            QtWidgets.QMessageBox.warning(None, "Peringatan", "Semua kolom harus diisi!")
            return

        try:
            admin = Admin()
            status = admin.tambah_user(nama, username, password, role)
            
            msg = QtWidgets.QMessageBox()
            if status:
                msg.setWindowTitle("Success")
                msg.setText("User berhasil ditambahkan.")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.exec_()
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