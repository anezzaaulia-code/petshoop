# -*- coding: utf-8 -*-

from models.User import User
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700) # Sedikit diperbesar agar lega
        
        # --- BACKGROUND WINDOW UTAMA ---
        # Warna background gelap elegan (Midnight Blue)
        MainWindow.setStyleSheet("background-color: #2c3e50;") 
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # --- CONTAINER (CARD) ---
        # Frame putih di tengah sebagai wadah form
        self.frame_login = QtWidgets.QFrame(self.centralwidget)
        self.frame_login.setGeometry(QtCore.QRect(250, 100, 400, 500))
        self.frame_login.setStyleSheet("""
            QFrame {
                background-color: #FFFFFF;
                border-radius: 20px;
            }
        """)
        self.frame_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login.setObjectName("frame_login")

        # Efek Bayangan pada Card agar terlihat timbul (3D effect)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(5)
        shadow.setColor(QtGui.QColor(0, 0, 0, 80))
        self.frame_login.setGraphicsEffect(shadow)

        # --- JUDUL UTAMA ---
        self.label_title = QtWidgets.QLabel(self.frame_login)
        self.label_title.setGeometry(QtCore.QRect(0, 40, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: #2c3e50; background: transparent;")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_title.setText("WELCOME BACK")

        # --- SUB JUDUL ---
        self.label_subtitle = QtWidgets.QLabel(self.frame_login)
        self.label_subtitle.setGeometry(QtCore.QRect(0, 90, 400, 20))
        font_sub = QtGui.QFont()
        font_sub.setFamily("Segoe UI")
        font_sub.setPointSize(10)
        self.label_subtitle.setFont(font_sub)
        self.label_subtitle.setStyleSheet("color: #7f8c8d; background: transparent;")
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setText("Please sign in to continue")

        # --- STYLE INPUT FIELD (CSS) ---
        input_style = """
            QLineEdit {
                background-color: #ecf0f1;
                border: 2px solid #ecf0f1;
                border-radius: 10px;
                padding-left: 15px;
                color: #2c3e50;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
                background-color: #FFFFFF;
            }
        """

        # --- INPUT USERNAME ---
        self.label_user = QtWidgets.QLabel(self.frame_login)
        self.label_user.setGeometry(QtCore.QRect(50, 150, 100, 20))
        self.label_user.setFont(QtGui.QFont("Segoe UI", 10, QtGui.QFont.Bold))
        self.label_user.setStyleSheet("color: #2c3e50;")
        self.label_user.setText("Username")

        self.input_username = QtWidgets.QLineEdit(self.frame_login)
        self.input_username.setGeometry(QtCore.QRect(50, 175, 300, 45))
        self.input_username.setStyleSheet(input_style)
        self.input_username.setPlaceholderText("Enter your username")

        # --- INPUT PASSWORD ---
        self.label_pass = QtWidgets.QLabel(self.frame_login)
        self.label_pass.setGeometry(QtCore.QRect(50, 240, 100, 20))
        self.label_pass.setFont(QtGui.QFont("Segoe UI", 10, QtGui.QFont.Bold))
        self.label_pass.setStyleSheet("color: #2c3e50;")
        self.label_pass.setText("Password")

        self.input_password = QtWidgets.QLineEdit(self.frame_login)
        self.input_password.setGeometry(QtCore.QRect(50, 265, 300, 45))
        self.input_password.setStyleSheet(input_style)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setPlaceholderText("Enter your password")

        # --- TOMBOL LOGIN ---
        self.btn_login = QtWidgets.QPushButton(self.frame_login)
        self.btn_login.setGeometry(QtCore.QRect(50, 360, 300, 50))
        self.btn_login.setFont(QtGui.QFont("Segoe UI", 12, QtGui.QFont.Bold))
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3498db, stop:1 #2980b9);
                color: white;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2980b9, stop:1 #3498db);
            }
            QPushButton:pressed {
                background-color: #1abc9c;
            }
        """)
        self.btn_login.setText("LOGIN")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        # --- EVENT HANDLING ---
        self.btn_login.clicked.connect(self.login)
        self.input_password.returnPressed.connect(self.login)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login System"))

    # ================= LOGIN LOGIC =================
    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        # Validasi sederhana agar tidak kosong
        if not username or not password:
             QtWidgets.QMessageBox.warning(None, "Peringatan", "Harap isi username dan password!")
             return

        try:
            user = User(username, password)

            if user.login():
                self.user_login = user  

                if user.role == "admin":
                    self.openDashboardAdmin()
                elif user.role == "supervisor":
                    self.openDashboardSupervisor()
                else:
                    self.openDashboardKasir()

                self.main_window.hide()
            else:
                QtWidgets.QMessageBox.warning(
                    None, "Login Gagal", "Username atau password salah!"
                )
        except Exception as e:
             QtWidgets.QMessageBox.critical(None, "Error System", f"Terjadi kesalahan: {e}")

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