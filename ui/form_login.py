# -*- coding: utf-8 -*-

from models.User import User
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700) 
        
        # --- BACKGROUND WINDOW UTAMA: Teal Sangat Muda (Hangat) ---
        MainWindow.setStyleSheet("background-color: #e0f7fa;") 
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Layout Root untuk Centering Card (Horizontal dan Vertikal)
        root_layout = QVBoxLayout(self.centralwidget)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setAlignment(QtCore.Qt.AlignCenter) 

        # --- CONTAINER (CARD) ---
        self.frame_login = QtWidgets.QFrame(self.centralwidget)
        self.frame_login.setFixedSize(450, 550) # Diperbesar sedikit agar lega
        self.frame_login.setStyleSheet("""
            QFrame {
                background-color: #FFFFFF;
                border-radius: 30px; /* Lebih membulat */
            }
        """)
        self.frame_login.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_login.setObjectName("frame_login")

        # Efek Bayangan pada Card
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(40)
        shadow.setXOffset(0)
        shadow.setYOffset(15)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        self.frame_login.setGraphicsEffect(shadow)
        
        # --- Layout Internal Card (QVBoxLayout) ---
        card_layout = QVBoxLayout(self.frame_login)
        card_layout.setContentsMargins(60, 50, 60, 50)
        card_layout.setSpacing(15)
        
        # --- JUDUL UTAMA ---
        self.label_title = QtWidgets.QLabel(self.frame_login)
        # Font Lembut
        self.label_title.setFont(QtGui.QFont("Tahoma", 26, QtGui.QFont.Bold))
        self.label_title.setStyleSheet("color: #00bcd4; background: transparent;") # Teal
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_title.setText("PETSHOP 🐾")
        card_layout.addWidget(self.label_title)

        # --- SUB JUDUL ---
        self.label_subtitle = QtWidgets.QLabel(self.frame_login)
        self.label_subtitle.setFont(QtGui.QFont("Arial", 12))
        self.label_subtitle.setStyleSheet("color: #7f8c8d; background: transparent;")
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setText("Silakan masuk untuk melanjutkan")
        card_layout.addWidget(self.label_subtitle)
        
        card_layout.addSpacing(30) 

        # --- STYLE INPUT FIELD (CSS) ---
        input_style = """
            QLineEdit {
                background-color: #f5f5f5; /* Abu-abu sangat muda */
                border: 1px solid #cfd8dc; 
                border-radius: 18px; /* Lebih membulat */
                padding: 10px 20px;
                color: #4a4a4a;
                font-size: 15px;
                font-family: Arial;
            }
            QLineEdit:focus {
                border: 2px solid #ff9800; /* Orange Ceria saat fokus */
                background-color: #FFFFFF;
            }
        """

        # --- INPUT USERNAME ---
        self.label_user = QtWidgets.QLabel(self.frame_login)
        self.label_user.setFont(QtGui.QFont("Arial", 11, QtGui.QFont.Bold))
        self.label_user.setStyleSheet("color: #4a4a4a;")
        self.label_user.setText("Username")
        card_layout.addWidget(self.label_user)

        self.input_username = QtWidgets.QLineEdit(self.frame_login)
        self.input_username.setFixedSize(330, 50)
        self.input_username.setStyleSheet(input_style)
        self.input_username.setPlaceholderText("Masukkan Username Anda")
        card_layout.addWidget(self.input_username, 0, QtCore.Qt.AlignCenter)

        # --- INPUT PASSWORD ---
        self.label_pass = QtWidgets.QLabel(self.frame_login)
        self.label_pass.setFont(QtGui.QFont("Arial", 11, QtGui.QFont.Bold))
        self.label_pass.setStyleSheet("color: #4a4a4a;")
        self.label_pass.setText("Password")
        card_layout.addWidget(self.label_pass)

        self.input_password = QtWidgets.QLineEdit(self.frame_login)
        self.input_password.setFixedSize(330, 50)
        self.input_password.setStyleSheet(input_style)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setPlaceholderText("Masukkan Password Anda")
        card_layout.addWidget(self.input_password, 0, QtCore.Qt.AlignCenter)
        
        card_layout.addSpacing(30) 

        # --- TOMBOL LOGIN ---
        self.btn_login = QtWidgets.QPushButton(self.frame_login)
        self.btn_login.setFixedSize(330, 55)
        self.btn_login.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setStyleSheet("""
            QPushButton {
                background-color: #00bcd4; /* Teal Solid */
                color: white;
                border-radius: 27px; 
                box-shadow: 0 5px 15px rgba(0, 188, 212, 0.4); 
            }
            QPushButton:hover {
                background-color: #0097a7;
            }
            QPushButton:pressed {
                background-color: #00838f;
            }
        """)
        self.btn_login.setText("LOGIN")
        card_layout.addWidget(self.btn_login, 0, QtCore.Qt.AlignCenter)

        # Tambahkan Card ke Root Layout (sudah di-center)
        root_layout.addWidget(self.frame_login)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        # --- EVENT HANDLING ---
        self.btn_login.clicked.connect(self.login)
        self.input_password.returnPressed.connect(self.login)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login System - Petshop"))

    # ================= LOGIN LOGIC =================
    def login(self):
        # NOTE: Mengganti QMessageBox standar dengan pesan yang lebih lucu/ramah
        
        username = self.input_username.text()
        password = self.input_password.text()

        if not username or not password:
            QMessageBox.warning(None, "Waduh, Kosong!", "Harap isi username dan password dulu ya!")
            return

        try:
            user = User(username, password)

            if user.login():
                self.user_login = user  
                
                # Navigasi berdasarkan role
                if user.role == "admin":
                    self.openDashboardAdmin()
                elif user.role == "supervisor":
                    self.openDashboardSupervisor()
                else:
                    self.openDashboardKasir()

                self.main_window.hide()
            else:
                QMessageBox.warning(
                    None, "Login Gagal 😿", "Username atau password salah! Coba lagi."
                )
        except Exception as e:
             QMessageBox.critical(None, "Error System 🚨", f"Terjadi kesalahan koneksi/sistem: {e}")

    # ================= DASHBOARD NAV =================
    def openDashboardAdmin(self):
        try:
            import dashboard.dashboard_admin as dashboard_admin
            self.window = QtWidgets.QMainWindow()
            self.ui = dashboard_admin.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        except ImportError:
            print("Module dashboard_admin tidak ditemukan")

    def openDashboardSupervisor(self):
        try:
            import dashboard.dashboard_supervisor as dashboard_supervisor
            self.window = QtWidgets.QMainWindow()
            self.ui = dashboard_supervisor.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        except ImportError:
             print("Module dashboard_supervisor tidak ditemukan")

    def openDashboardKasir(self):
        try:
            import dashboard.dashboard_kasir as dashboard_kasir
            self.window = QtWidgets.QMainWindow()
            self.ui = dashboard_kasir.Ui_MainWindow()
            self.ui.setupUi(self.window, self.user_login)
            self.window.show()
        except ImportError:
             print("Module dashboard_kasir tidak ditemukan")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())