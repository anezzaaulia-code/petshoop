# -*- coding: utf-8 -*-
from dashboard.dashboard_supervisor import Ui_MainWindow as UiDashboard
from models.produk import MakananHewan
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    # =========================
    #  SETUP UI + KATEGORI
    # =========================
    def setupUi(self, MainWindow, kategori="Makanan Hewan"):
        self.kategori = kategori  # simpan kategori yg dikirim
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # ===== UI LABEL DAN INPUT =====
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 471, 51))
        font = QtGui.QFont(); font.setPointSize(18); font.setBold(True)
        self.label.setFont(font)

        # ==== ID ====
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 55, 16))
        self.label_2.setFont(QtGui.QFont("Arial", 11))

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 100, 291, 41))
        self.lineEdit.setFont(QtGui.QFont("Arial", 12))

        # ==== Nama ====
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 160, 55, 16))
        self.label_3.setFont(QtGui.QFont("Arial", 11))

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 150, 291, 41))
        self.lineEdit_2.setFont(QtGui.QFont("Arial", 12))

        # ==== Stok ====
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 210, 55, 16))
        self.label_4.setFont(QtGui.QFont("Arial", 11))

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 200, 291, 41))
        self.lineEdit_3.setFont(QtGui.QFont("Arial", 12))

        # ==== Harga ====
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 250, 51, 31))
        self.label_5.setFont(QtGui.QFont("Arial", 11))

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 250, 291, 41))
        self.lineEdit_4.setFont(QtGui.QFont("Arial", 12))

        # ==== Jenis Hewan ====
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 300, 101, 41))
        self.label_6.setFont(QtGui.QFont("Arial", 11))

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 300, 291, 41))
        self.lineEdit_5.setFont(QtGui.QFont("Arial", 12))

        # ==== Masa Exp ====
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 350, 101, 41))
        self.label_7.setFont(QtGui.QFont("Arial", 11))

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(260, 350, 291, 41))
        self.lineEdit_6.setFont(QtGui.QFont("Arial", 12))

        # ==== Jenis Makanan ====
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 400, 121, 41))
        self.label_8.setFont(QtGui.QFont("Arial", 11))

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(260, 400, 291, 41))
        self.lineEdit_7.setFont(QtGui.QFont("Arial", 12))

        # ==== LABEL KATEGORI (READONLY, NO COMBOBOX) ====
        self.label_kategori = QtWidgets.QLabel(self.centralwidget)
        self.label_kategori.setGeometry(QtCore.QRect(100, 450, 151, 41))
        self.label_kategori.setFont(QtGui.QFont("Arial", 11))
        self.label_kategori.setText("Kategori")

        self.kategori_text = QtWidgets.QLineEdit(self.centralwidget)
        self.kategori_text.setGeometry(QtCore.QRect(260, 450, 291, 41))
        self.kategori_text.setFont(QtGui.QFont("Arial", 12))
        self.kategori_text.setText(self.kategori)
        self.kategori_text.setReadOnly(True)

        # ===== BUTTONS =====
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 520, 191, 51))
        self.pushButton.setFont(QtGui.QFont("Arial", 11))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 520, 191, 51))
        self.pushButton_2.setFont(QtGui.QFont("Arial", 11))

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        # EVENTS
        self.pushButton.clicked.connect(self.insertData)
        self.pushButton_2.clicked.connect(self.backToDashboard)

    # ========================
    #  INSERT DATA PRODUK
    # ========================
    def insertData(self):
        id_produk = self.lineEdit.text()
        if not id_produk:
            QMessageBox.warning(None, "ERROR", "ID harus diisi!")
            return

        try:
            nama = self.lineEdit_2.text()
            stok = int(self.lineEdit_3.text())
            harga = float(self.lineEdit_4.text())
            jenis_hewan = self.lineEdit_5.text()
            masa_exp = self.lineEdit_6.text()
            jenis_makanan = self.lineEdit_7.text()

            makanan = MakananHewan(
                id_produk=id_produk,
                nama_produk=nama,
                harga=harga,
                stok=stok,
                jenis_hewan=jenis_hewan,
                masa_exp=masa_exp,
                jenis_makanan=jenis_makanan
            )

            makanan.insert()

            QMessageBox.information(None, "Success", "Data berhasil ditambahkan!")
            self.clearFields()

        except ValueError:
            QMessageBox.warning(None, "ERROR", "Harga atau stok harus angka!")
        except Exception as e:
            QMessageBox.warning(None, "ERROR", str(e))

    def clearFields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()

    # ========================
    #  BACK TO DASHBOARD
    # ========================
    def backToDashboard(self):
        self.dashboard_window = QtWidgets.QMainWindow()
        ui = UiDashboard()
        ui.setupUi(self.dashboard_window)
        self.dashboard_window.show()
        self.centralwidget.window().close()

    # ========================
    #  LABEL TRANSLATION
    # ========================
    def retranslateUi(self, MainWindow):
        _ = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_("MainWindow", "Input Makanan Hewan"))
        self.label.setText(_("MainWindow", "INSERT MAKANAN HEWAN"))
        self.label_2.setText(_("MainWindow", "ID"))
        self.label_3.setText(_("MainWindow", "Nama"))
        self.label_4.setText(_("MainWindow", "Stok"))
        self.label_5.setText(_("MainWindow", "Harga"))
        self.label_6.setText(_("MainWindow", "Jenis Hewan"))
        self.label_7.setText(_("MainWindow", "Masa Exp"))
        self.label_8.setText(_("MainWindow", "Jenis Makanan"))
        self.pushButton.setText(_("MainWindow", "Insert"))
        self.pushButton_2.setText(_("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
