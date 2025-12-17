# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QWidget

# Import form-form yang dibutuhkan (dibiarkan seperti di kode asli)
# from ui.kasir.form_transaksi import Ui_FormTransaksi
# from ui.kasir.form_laporan import Ui_FormLaporan
# from ui.form_login import Ui_MainWindow as LoginForm


# =================================================================
# 🎨 STYLESHEET DASHBOARD KASIR (MINIMALIS & CERIA)
# =================================================================
KASIR_DASHBOARD_STYLE = """
/* Background Utama */
QWidget#centralwidget {
    background-color: #fcfcfc; /* Putih Krem */
}

/* Judul Utama */
QLabel#label { 
    color: #00796b; /* Teal Gelap */
    font-size: 28px;
    font-weight: bold;
    padding-bottom: 10px;
    margin-bottom: 20px; 
    border-bottom: 3px solid #b2dfdb; 
}

/* Styling Tombol Aksi (General) */
QPushButton {
    color: white;
    border: none;
    border-radius: 12px; 
    padding: 20px;
    font-weight: bold;
    font-size: 16px;
    transition: background-color 0.3s;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}

/* Tombol Transaksi (Aksi Utama) - HIJAU */
QPushButton#pushButton { 
    background-color: #4CAF50; /* Hijau Cerah */
}
QPushButton#pushButton:hover {
    background-color: #388E3C;
}

/* Tombol Laporan (Aksi Sekunder) - TEAL */
QPushButton#pushButton_3 { 
    background-color: #00BCD4; /* Teal Cerah */
    color: white;
}
QPushButton#pushButton_3:hover {
    background-color: #0097A7;
}


/* Tombol Logout */
QPushButton#pushButton_logout {
    background-color: #607d8b; /* Abu-abu Kebiruan */
    color: white;
    font-size: 14px;
    border-radius: 8px;
    padding: 5px 10px; 
}
QPushButton#pushButton_logout:hover {
    background-color: #455a64;
}
"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_login):
        self.user_login = user_login
        self.MainWindow = MainWindow 
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(KASIR_DASHBOARD_STYLE) # Terapkan Stylesheet

        # -----------------------------------------------------
        # PERBAIKAN UTAMA: Pusatkan Konten Menggunakan QVBoxLayout
        # -----------------------------------------------------
        
        root_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        root_layout.setContentsMargins(50, 20, 50, 20)
        
        # Tambahkan stretch di atas untuk centering vertikal
        root_layout.addStretch(1) 

        # --- CONTENT CONTAINER (Wadah semua elemen yang akan di-center) ---
        content_container = QtWidgets.QWidget(self.centralwidget)
        content_layout = QtWidgets.QVBoxLayout(content_container)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(40) # Jarak antar elemen utama

        # 1. HEADER (Judul + Logout)
        header_layout = QtWidgets.QHBoxLayout()
        header_layout.setAlignment(QtCore.Qt.AlignTop) 
        
        self.label = QtWidgets.QLabel(content_container)
        self.label.setObjectName("label")
        self.label.setText("DASHBOARD KASIR")
        self.label.setAlignment(QtCore.Qt.AlignCenter) # Centerkan teks di label
        
        # Tambahkan ruang kosong di kiri judul (untuk mengimbangi tombol logout)
        header_layout.addSpacing(150) 
        
        # Tambahkan label judul (center)
        header_layout.addWidget(self.label, 1) 
        
        # Tombol Logout
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.pushButton_logout.setFixedSize(140, 40)
        header_layout.addWidget(self.pushButton_logout)

        content_layout.addLayout(header_layout)
        
        # 2. Kontainer Tombol Utama (Pusatkan Horizontal)
        button_container = QtWidgets.QHBoxLayout()
        button_container.setAlignment(QtCore.Qt.AlignCenter)
        button_container.setSpacing(40)

        # Ukuran Fixed Tombol
        FIXED_WIDTH = 230
        FIXED_HEIGHT = 120

        # BUTTON MULAI TRANSAKSI
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFixedSize(FIXED_WIDTH, FIXED_HEIGHT)
        button_container.addWidget(self.pushButton)

        # BUTTON LIHAT LAPORAN
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFixedSize(FIXED_WIDTH, FIXED_HEIGHT)
        button_container.addWidget(self.pushButton_3)

        content_layout.addLayout(button_container)
        
        # Tambahkan content container ke root layout
        root_layout.addWidget(content_container, 0, QtCore.Qt.AlignCenter) 

        # Tambahkan stretch di bawah untuk centering vertikal
        root_layout.addStretch(1)

        # ======================= End Layout Setup =======================

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ================= EVENTS =================
        self.pushButton.clicked.connect(self.openFormTransaksi)
        self.pushButton_3.clicked.connect(self.openLaporan)
        self.pushButton_logout.clicked.connect(self.logout)

    def retranslateUi(self, MainWindow):
        _ = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_("MainWindow", "Dashboard Kasir"))
        self.pushButton.setText(_("MainWindow", "MULAI TRANSAKSI 🛒"))
        self.label.setText(_("MainWindow", "DASHBOARD KASIR"))
        self.pushButton_3.setText(_("MainWindow", "LIHAT LAPORAN 📈"))
        self.pushButton_logout.setText(_("MainWindow", "LOGOUT 🚪"))

    # ==================== FORM TRANSAKSI ====================
    def openFormTransaksi(self):
        from ui.kasir.form_transaksi import Ui_FormTransaksi
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FormTransaksi()
        self.ui.setupUi(self.window, self.user_login)
        self.window.show()

    # ==================== FORM LAPORAN ====================
    def openLaporan(self):
        from ui.kasir.form_laporan import Ui_FormLaporan
        self.window_laporan = QtWidgets.QMainWindow()
        self.ui_laporan = Ui_FormLaporan()
        self.ui_laporan.setupUi(self.window_laporan)
        self.window_laporan.show()

    # ==================== LOGOUT ====================
    def logout(self):
        # Pastikan path benar
        import os, sys
        base_path = os.path.dirname(os.path.dirname(__file__))
        if base_path not in sys.path:
            sys.path.append(base_path)

        # Import form login
        from ui.form_login import Ui_MainWindow as LoginForm

        # Buka form login baru
        self.loginWindow = QtWidgets.QMainWindow()
        self.login_ui = LoginForm()
        self.login_ui.setupUi(self.loginWindow)
        self.loginWindow.show()

        # Tutup dashboard
        self.MainWindow.close()


# ================= MAIN RUN =================
if __name__ == "__main__":
    import sys
    
    # Dummy user login for testing
    class DummyUser:
        def __init__(self):
            self.nama = "Kasir Test"
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, DummyUser())
    MainWindow.show()
    sys.exit(app.exec_())