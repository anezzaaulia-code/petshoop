# -*- coding: utf-8 -*-
import sys
import ui.form_login as login
import ui.supervisor.form_insert_data_barang as tb
import ui.supervisor.form_edit_data_barang as eb
import ui.supervisor.form_delete_data_barang as db
import ui.supervisor.form_lihat_data_barang as lb
from PyQt5 import QtCore, QtGui, QtWidgets

# =================================================================
# 🎨 STYLESHEET DASHBOARD (PREV. VERSI TERAKHIR)
# =================================================================
DASHBOARD_STYLE = """
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
    /* Hilangkan text-align di sini, biarkan layout yang menangani */
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

/* Tombol 1: INSERT (Create) - HIJAU */
QPushButton#pushButton { 
    background-color: #4CAF50; 
}
QPushButton#pushButton:hover {
    background-color: #388E3C;
}

/* Tombol 4: UPDATE (Update) - BIRU */
QPushButton#pushButton_4 { 
    background-color: #2196F3; 
}
QPushButton#pushButton_4:hover {
    background-color: #1976D2;
}

/* Tombol 2: DELETE (Danger) - MERAH */
QPushButton#pushButton_2 { 
    background-color: #F44336; 
}
QPushButton#pushButton_2:hover {
    background-color: #D32F2F;
}

/* Tombol 3: LIHAT (View/Secondary) - TEAL */
QPushButton#pushButton_3 { 
    background-color: #00BCD4; 
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
    def setupUi(self, MainWindow):
        self.main_window = MainWindow 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.centralwidget.setStyleSheet(DASHBOARD_STYLE)

        # -----------------------------------------------------
        # PERBAIKAN UTAMA: Pusatkan Konten Menggunakan QVBoxLayout
        # -----------------------------------------------------
        
        # Layout Utama CentralWidget (untuk menampung semuanya)
        root_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        root_layout.setContentsMargins(0, 0, 0, 0)
        
        # Tambahkan stretch di atas untuk centering vertikal
        root_layout.addStretch(1) 

        # --- CONTENT CONTAINER (Wadah semua elemen yang akan di-center) ---
        content_container = QtWidgets.QWidget(self.centralwidget)
        # Gunakan QVBoxLayout untuk menumpuk header dan grid tombol
        content_layout = QtWidgets.QVBoxLayout(content_container)
        content_layout.setContentsMargins(50, 20, 50, 20)
        content_layout.setSpacing(25) # Tambah jarak antar elemen

        # 1. HEADER (Judul + Logout)
        header_layout = QtWidgets.QHBoxLayout()
        header_layout.setAlignment(QtCore.Qt.AlignTop) 
        
        self.label = QtWidgets.QLabel(content_container)
        self.label.setObjectName("label")
        self.label.setText("DASHBOARD SUPERVISOR")
        self.label.setAlignment(QtCore.Qt.AlignCenter) # Centerkan teks di label
        
        # Tambahkan stretch di kiri label agar label yang sudah dicenter sendiri ini berada di tengah-tengah layout
        header_layout.addStretch(1) 
        header_layout.addWidget(self.label, 3) # Beri proporsi lebih besar (3)
        
        self.pushButton_logout = QtWidgets.QPushButton(content_container)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.pushButton_logout.setFixedSize(120, 40)
        
        header_layout.addWidget(self.pushButton_logout, 0) # Beri proporsi kecil (0)
        
        content_layout.addLayout(header_layout)
        
        # 2. Grid Tombol CRUD
        crud_grid = QtWidgets.QGridLayout()
        crud_grid.setSpacing(20)
        crud_grid.setAlignment(QtCore.Qt.AlignCenter) # CENTERKAN GRID CRUD

        # Ukuran Fixed Tombol
        FIXED_WIDTH = 250
        FIXED_HEIGHT = 120

        # INSERT (ROW 0, COL 0)
        self.pushButton = QtWidgets.QPushButton(content_container)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFixedSize(FIXED_WIDTH, FIXED_HEIGHT) 
        crud_grid.addWidget(self.pushButton, 0, 0)
        
        # UPDATE (ROW 0, COL 1)
        self.pushButton_4 = QtWidgets.QPushButton(content_container)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFixedSize(FIXED_WIDTH, FIXED_HEIGHT)
        crud_grid.addWidget(self.pushButton_4, 0, 1)

        # DELETE (ROW 1, COL 0)
        self.pushButton_2 = QtWidgets.QPushButton(content_container)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFixedSize(FIXED_WIDTH, FIXED_HEIGHT)
        crud_grid.addWidget(self.pushButton_2, 1, 0)

        # LIHAT (ROW 1, COL 1)
        self.pushButton_3 = QtWidgets.QPushButton(content_container)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFixedSize(FIXED_WIDTH, FIXED_HEIGHT)
        crud_grid.addWidget(self.pushButton_3, 1, 1)

        content_layout.addLayout(crud_grid)
        
        # Tambahkan content container ke root layout
        root_layout.addWidget(content_container, 0, QtCore.Qt.AlignCenter) # CENTERKAN content_container HORIZONTAL

        # Tambahkan stretch di bawah untuk centering vertikal
        root_layout.addStretch(1)

        # ======================= End Layout Setup =======================

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard Supervisor - Pets Hoob"))

        self.label.setText(_translate("MainWindow", "DASHBOARD SUPERVISOR"))

        self.pushButton.setText(_translate("MainWindow", "INSERT DATA PRODUK"))
        self.pushButton_4.setText(_translate("MainWindow", "UPDATE DATA PRODUK"))
        self.pushButton_2.setText(_translate("MainWindow", "DELETE DATA PRODUK"))
        self.pushButton_3.setText(_translate("MainWindow", "LIHAT DATA PRODUK"))
        self.pushButton_logout.setText(_translate("MainWindow", "LOGOUT 🚪"))

        # ---- EVENT KLIK ----
        self.pushButton.clicked.connect(self.openTambahProduk)
        self.pushButton_2.clicked.connect(self.openDeleteProduk)
        self.pushButton_3.clicked.connect(self.openLihatProduk)
        self.pushButton_4.clicked.connect(self.openEditProduk)
        self.pushButton_logout.clicked.connect(self.logout)


    def openTambahProduk(self):
        self.window = QtWidgets.QMainWindow()
        self.ui_other = tb.Ui_MainWindow()
        self.ui_other.setupUi(self.window)
        self.window.show()
        self.main_window.hide()

    def openEditProduk(self):
        self.window = QtWidgets.QMainWindow()
        self.ui_other = eb.Ui_MainWindow()
        self.ui_other.setupUi(self.window)
        self.window.show()
        self.main_window.hide()

    def openDeleteProduk(self):
        self.window = QtWidgets.QMainWindow()
        self.ui_other = db.Ui_MainWindow()
        self.ui_other.setupUi(self.window)
        self.window.show()
        self.main_window.hide()

    def openLihatProduk(self):
        self.window = QtWidgets.QMainWindow()
        self.ui_other = lb.Ui_MainWindow()
        self.ui_other.setupUi(self.window)
        self.window.show()
        self.main_window.hide()

    def logout(self):
        self.window = QtWidgets.QMainWindow()
        self.login = login.Ui_MainWindow()
        self.login.setupUi(self.window)
        self.window.show()
        self.main_window.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())