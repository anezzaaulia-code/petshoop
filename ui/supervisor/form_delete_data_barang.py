# -*- coding: utf-8 -*-

from database.connect import get_connection   
from models.produk import Produk
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)

                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")

                # ============================
                #  TITLE
                # ============================
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(260, 30, 321, 51))
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setObjectName("label")

                # ============================
                #  INPUT ID + BUTTON CARI
                # ============================
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(200, 140, 55, 16))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")

                self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit.setGeometry(QtCore.QRect(260, 130, 201, 41))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.lineEdit.setFont(font)
                self.lineEdit.setStyleSheet(
                        "QLineEdit {\n"
                        "    background-color: #FFFFFF;\n"
                        "    color: #000000;\n"
                        "    border: 2px solid #888888;\n"
                        "    border-radius: 6px;\n"
                        "    padding: 4px;\n"
                        "}\n"
                        "QLineEdit:focus {\n"
                        "    border: 2px solid #AAAAAA;\n"
                        "}"
                )
                self.lineEdit.setObjectName("lineEdit")

                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_2.setGeometry(QtCore.QRect(480, 130, 81, 41))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.pushButton_2.setFont(font)
                self.pushButton_2.setStyleSheet(
                        "QPushButton {\n"
                        "    background-color: #555555;\n"
                        "    color: white;\n"
                        "    border-radius: 8px;\n"
                        "    padding: 6px 12px;\n"
                        "}\n"
                        "QPushButton:hover {\n"
                        "    background-color: #666666;\n"
                        "}\n"
                        "QPushButton:pressed {\n"
                        "    background-color: #777777;\n"
                        "}"
                )
                self.pushButton_2.setObjectName("pushButton_2")

                # ============================
                #  LABEL KIRI (RAPI)
                # ============================
                font_label = QtGui.QFont()
                font_label.setPointSize(11)

                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(200, 200, 100, 30))  # Nama
                self.label_3.setFont(font_label)

                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(200, 240, 100, 30))  # Stok
                self.label_4.setFont(font_label)

                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(200, 280, 100, 30))  # Harga
                self.label_5.setFont(font_label)

                self.label_11 = QtWidgets.QLabel(self.centralwidget)
                self.label_11.setGeometry(QtCore.QRect(200, 320, 100, 30)) # Jenis Hewan
                self.label_11.setFont(font_label)

                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(200, 360, 100, 30))  # Kategori
                self.label_6.setFont(font_label)

                # ============================
                #  LABEL VALUE KANAN (RAPI)
                # ============================
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(320, 200, 300, 30))
                self.label_7.setFont(font_label)
                self.label_7.setText("")

                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(320, 240, 300, 30))
                self.label_8.setFont(font_label)
                self.label_8.setText("")

                self.label_9 = QtWidgets.QLabel(self.centralwidget)
                self.label_9.setGeometry(QtCore.QRect(320, 280, 300, 30))
                self.label_9.setFont(font_label)
                self.label_9.setText("")

                self.label_10 = QtWidgets.QLabel(self.centralwidget)
                self.label_10.setGeometry(QtCore.QRect(320, 320, 300, 30))
                self.label_10.setFont(font_label)
                self.label_10.setText("")

                self.label_kategori_value = QtWidgets.QLabel(self.centralwidget)
                self.label_kategori_value.setGeometry(QtCore.QRect(320, 360, 300, 30))
                self.label_kategori_value.setFont(font_label)
                self.label_kategori_value.setText("")

                # ============================
                # BUTTON DELETE
                # ============================
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(170, 460, 181, 51))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet(
                        "QPushButton {\n"
                        "    background-color: #555555;\n"
                        "    color: white;\n"
                        "    border-radius: 8px;\n"
                        "    padding: 6px 12px;\n"
                        "}\n"
                        "QPushButton:hover {\n"
                        "    background-color: #666666;\n"
                        "}\n"
                        "QPushButton:pressed {\n"
                        "    background-color: #777777;\n"
                        "}"
                )
                self.pushButton.setObjectName("pushButton")

                # ============================
                # BUTTON BACK
                # ============================
                self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_3.setGeometry(QtCore.QRect(400, 460, 181, 51))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.pushButton_3.setFont(font)
                self.pushButton_3.setStyleSheet(
                        "QPushButton {\n"
                        "    background-color: #555555;\n"
                        "    color: white;\n"
                        "    border-radius: 8px;\n"
                        "    padding: 6px 12px;\n"
                        "}\n"
                        "QPushButton:hover {\n"
                        "    background-color: #666666;\n"
                        "}\n"
                        "QPushButton:pressed {\n"
                        "    background-color: #777777;\n"
                        "}"
                )
                self.pushButton_3.setObjectName("pushButton_3")

                MainWindow.setCentralWidget(self.centralwidget)

                # Menu Bar
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
                MainWindow.setMenuBar(self.menubar)

                # Statusbar
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                MainWindow.setStatusBar(self.statusbar)

                # ACTION BUTTON
                self.pushButton_2.clicked.connect(self.cari_data)
                self.pushButton.clicked.connect(self.delete_data)
                self.pushButton_3.clicked.connect(self.back)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "Delete Data Barang"))
                self.label_2.setText(_translate("MainWindow", "ID"))
                self.label_3.setText(_translate("MainWindow", "Nama"))
                self.label_4.setText(_translate("MainWindow", "Stok"))
                self.label_5.setText(_translate("MainWindow", "Harga"))
                self.label_6.setText(_translate("MainWindow", "Kategori"))
                self.label_11.setText(_translate("MainWindow", "Jenis Hewan"))
                self.pushButton.setText(_translate("MainWindow", "Delete"))
                self.pushButton_2.setText(_translate("MainWindow", "Cari"))
                self.pushButton_3.setText(_translate("MainWindow", "Back"))

        # ==============================
        #  CARI DATA
        # ==============================
        def cari_data(self):
                id_produk = self.lineEdit.text().strip()

                if not id_produk.isdigit():
                        self.label_7.setText("ID tidak valid!")
                        return

                db, cursor = get_connection()
                sql = "SELECT id_produk, nama_produk, harga, stok, jenis_hewan, kategori FROM produk WHERE id_produk=%s"
                cursor.execute(sql, (id_produk,))
                result = cursor.fetchone()

                if result:
                        self.label_7.setText(result[1])      # nama
                        self.label_8.setText(str(result[3])) # stok
                        self.label_9.setText(str(result[2])) # harga
                        self.label_10.setText(result[4])     # jenis hewan
                        self.label_kategori_value.setText(result[5]) # kategori
                else:
                        self.label_7.setText("Tidak ditemukan")
                        self.label_8.clear()
                        self.label_9.clear()
                        self.label_10.clear()
                        self.label_kategori_value.clear()

                cursor.close()
                db.close()

        # ==============================
        #  DELETE DATA
        # ==============================
        def delete_data(self):
                id_produk = self.lineEdit.text().strip()

                if not id_produk.isdigit():
                        self.label_7.setText("ID tidak valid!")
                        return

                konfirmasi = QtWidgets.QMessageBox.question(
                        None,
                        "Konfirmasi",
                        f"Yakin ingin menghapus ID {id_produk}?",
                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
                )

                if konfirmasi == QtWidgets.QMessageBox.No:
                        return

                try:
                        Produk.delete_by_id(id_produk)
                        self.label_7.setText("Berhasil dihapus!")
                        self.label_8.clear()
                        self.label_9.clear()
                        self.label_10.clear()
                        self.label_kategori_value.clear()

                except Exception as e:
                        self.label_7.setText(f"Error: {str(e)}")

        # ==============================
        #  BACK
        # ==============================
        def back(self):
                from dashboard.dashboard_supervisor import Ui_MainWindow as Dashboard
                self.window = QtWidgets.QMainWindow()
                self.ui = Dashboard()
                self.ui.setupUi(self.window)
                self.window.show()
                QtWidgets.QApplication.activeWindow().close()


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
