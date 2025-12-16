from dashboard.dashboard_supervisor import Ui_MainWindow as UiDashboard
from models.produk import AksesorisHewan
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object): 
    def setupUi(self, MainWindow, kategori="Aksesoris Hewan"):
        self.kategori = kategori  # kategori otomatis, tidak dipilih dari dropdown

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # ===== UI LABEL DAN INPUT =====
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("INSERT AKSESORIS HEWAN")

        # ===== INPUT ID =====
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 100, 55, 16))
        self.label_2.setFont(QtGui.QFont("Arial", 11))
        self.label_2.setText("ID")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 90, 291, 41))
        self.lineEdit.setFont(QtGui.QFont("Arial", 12))

        # ===== INPUT NAMA =====
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 150, 55, 16))
        self.label_3.setFont(QtGui.QFont("Arial", 11))
        self.label_3.setText("Nama")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 140, 291, 41))
        self.lineEdit_2.setFont(QtGui.QFont("Arial", 12))

        # ===== INPUT STOK =====
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 200, 55, 16))
        self.label_4.setFont(QtGui.QFont("Arial", 11))
        self.label_4.setText("Stok")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 190, 291, 41))
        self.lineEdit_3.setFont(QtGui.QFont("Arial", 12))

        # ===== INPUT HARGA =====
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 240, 51, 31))
        self.label_5.setFont(QtGui.QFont("Arial", 11))
        self.label_5.setText("Harga")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 240, 291, 41))
        self.lineEdit_4.setFont(QtGui.QFont("Arial", 12))

        # ===== INPUT JENIS HEWAN =====
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 290, 101, 41))
        self.label_6.setFont(QtGui.QFont("Arial", 11))
        self.label_6.setText("Jenis Hewan")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 290, 291, 41))
        self.lineEdit_5.setFont(QtGui.QFont("Arial", 12))

        # ===== INPUT WARNA =====
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 340, 101, 41))
        self.label_7.setFont(QtGui.QFont("Arial", 11))
        self.label_7.setText("Warna")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 340, 291, 41))
        self.lineEdit_6.setFont(QtGui.QFont("Arial", 12))

        # ===== INPUT UKURAN =====
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 390, 121, 41))
        self.label_8.setFont(QtGui.QFont("Arial", 11))
        self.label_8.setText("Ukuran")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(300, 390, 291, 41))
        self.lineEdit_7.setFont(QtGui.QFont("Arial", 12))

        # ===== LABEL KATEGORI (AUTOMATIC, NO DROPDOWN) =====
        self.label_kategori = QtWidgets.QLabel(self.centralwidget)
        self.label_kategori.setGeometry(QtCore.QRect(170, 430, 121, 41))
        self.label_kategori.setFont(QtGui.QFont("Arial", 11))
        self.label_kategori.setText("Kategori")

        self.kategori_text = QtWidgets.QLineEdit(self.centralwidget)
        self.kategori_text.setGeometry(QtCore.QRect(300, 430, 291, 41))
        self.kategori_text.setFont(QtGui.QFont("Arial", 12))
        self.kategori_text.setText(self.kategori)
        self.kategori_text.setReadOnly(True)

        # ===== BUTTON INSERT =====
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 500, 191, 51))
        self.pushButton.setFont(QtGui.QFont("Arial", 11))
        self.pushButton.setText("Insert")

        # ===== BUTTON BACK =====
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 500, 191, 51))
        self.pushButton_2.setFont(QtGui.QFont("Arial", 11))
        self.pushButton_2.setText("Back")

        MainWindow.setCentralWidget(self.centralwidget)

        # Event handler
        self.pushButton.clicked.connect(self.insertData)
        self.pushButton_2.clicked.connect(self.backToDashboard)

    # ====================
    # INSERT DATA
    # ====================
    def insertData(self):
        try:
            id_produk = self.lineEdit.text()
            nama = self.lineEdit_2.text()
            stok = int(self.lineEdit_3.text())
            harga = float(self.lineEdit_4.text())
            jenis_hewan = self.lineEdit_5.text()
            warna = self.lineEdit_6.text()
            ukuran = self.lineEdit_7.text()

            aksesoris = AksesorisHewan(
                id_produk=id_produk,
                nama_produk=nama,
                harga=harga,
                stok=stok,
                jenis_hewan=jenis_hewan,
                warna=warna,
                ukuran=ukuran
            )

            aksesoris.insert()

            QMessageBox.information(None, "Success", "Data berhasil ditambahkan!")

            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()

        except Exception as e:
            QMessageBox.warning(None, "ERROR", str(e))

    # ====================
    # BACK TO DASHBOARD
    # ====================
    def backToDashboard(self):
        self.dashboard_window = QtWidgets.QMainWindow()
        ui = UiDashboard()
        ui.setupUi(self.dashboard_window)
        self.dashboard_window.show()
        self.centralwidget.window().close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
