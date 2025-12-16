# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_login):
        self.user_login = user_login
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.MainWindow = MainWindow  # simpan referensi window

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ==================== BUTTON MULAI TRANSAKSI ====================
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 230, 231, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("""
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #66d9a3,
                stop:1 #33cc88
            );
            color: white;
            border-radius: 8px;
        """)

        # ==================== LABEL JUDUL ====================
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        # ==================== BUTTON LIHAT LAPORAN ====================
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 230, 231, 121))
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("""
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #d9d9d9,
                stop:1 #bfbfbf
            );
            color: black;
            border-radius: 8px;
        """)

        # ==================== BUTTON LOGOUT ====================
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(630, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_logout.setFont(font)
        self.pushButton_logout.setStyleSheet("""
            QPushButton {
                background-color: #4A4A4A;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #3A3A3A;
            }
        """)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ================= EVENTS =================
        self.pushButton.clicked.connect(self.openFormTransaksi)
        self.pushButton_3.clicked.connect(self.openLaporan)
        self.pushButton_logout.clicked.connect(self.logout)  # <--- logika logout aktif

    def retranslateUi(self, MainWindow):
        _ = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_("MainWindow", "Dashboard Kasir"))
        self.pushButton.setText(_("MainWindow", "MULAI TRANSAKSI"))
        self.label.setText(_("MainWindow", "DASHBOARD KASIR"))
        self.pushButton_3.setText(_("MainWindow", "LIHAT LAPORAN"))
        self.pushButton_logout.setText(_("MainWindow", "LOGOUT"))

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
        print("Logout clicked!")

        # Pastikan path benar
        import os, sys
        base_path = os.path.dirname(os.path.dirname(__file__))
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
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
