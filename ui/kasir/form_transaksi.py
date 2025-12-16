# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView

from database.connect import get_connection
from models.produk import Produk
from models.transaksi import Transaksi
from models.detail_transaksi import DetailTransaksi
from ui.kasir.form_struk import Ui_MainWindow as StrukWindow


class Ui_FormTransaksi(object):

    # =====================================================
    # SETUP UI (DESIGN ASLI — TIDAK DIUBAH)
    # =====================================================
    def setupUi(self, FormTransaksi, user_login):
        self.user_login = user_login
        FormTransaksi.setObjectName("FormTransaksi")
        FormTransaksi.resize(1100, 750)

        # ================= GLOBAL STYLE =================
        FormTransaksi.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI';
                font-size: 14px;
                color: #2c3e50;
            }
            QMainWindow {
                background-color: #f4f6f9;
            }
            QFrame {
                background-color: #ffffff;
                border-radius: 10px;
            }
            QLineEdit, QSpinBox {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 6px;
            }
            QLineEdit:focus, QSpinBox:focus {
                border: 1px solid #3498db;
            }
            QTableWidget {
                border: 1px solid #ddd;
                gridline-color: #eee;
                selection-background-color: #3498db;
                selection-color: white;
            }
            QHeaderView::section {
                background-color: #ecf0f1;
                padding: 6px;
                border: none;
                font-weight: bold;
            }
            QPushButton {
                padding: 10px;
                border-radius: 6px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover {
                opacity: 0.85;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(FormTransaksi)
        self.mainLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.mainLayout.setSpacing(20)

        # ================= LEFT PANEL =================
        self.leftPanel = QtWidgets.QFrame()
        self.leftLayout = QtWidgets.QVBoxLayout(self.leftPanel)
        self.leftLayout.setSpacing(15)

        lblProduk = QtWidgets.QLabel("📦 Daftar Produk")
        lblProduk.setStyleSheet("font-size:18px;font-weight:bold;")
        self.leftLayout.addWidget(lblProduk)

        searchLayout = QtWidgets.QHBoxLayout()
        self.inputSearchProduk = QtWidgets.QLineEdit()
        self.inputSearchProduk.setPlaceholderText("Cari nama / ID produk...")
        self.btnCariProduk = QtWidgets.QPushButton("Cari")
        self.btnCariProduk.setStyleSheet("background-color:#3498db;color:white;")

        searchLayout.addWidget(self.inputSearchProduk)
        searchLayout.addWidget(self.btnCariProduk)
        self.leftLayout.addLayout(searchLayout)

        self.tableProduk = QtWidgets.QTableWidget()
        self.tableProduk.setColumnCount(4)
        self.tableProduk.setHorizontalHeaderLabels(
            ["ID", "Nama Produk", "Harga", "Stok"]
        )
        self.tableProduk.verticalHeader().setVisible(False)
        self.tableProduk.setAlternatingRowColors(True)
        self.tableProduk.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableProduk.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableProduk.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableProduk.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableProduk.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)

        self.leftLayout.addWidget(self.tableProduk)

        qtyLayout = QtWidgets.QHBoxLayout()
        lblQty = QtWidgets.QLabel("Jumlah:")
        self.spinQty = QtWidgets.QSpinBox()
        self.spinQty.setMinimum(1)
        self.spinQty.setFixedWidth(80)

        self.btnTambahKeranjang = QtWidgets.QPushButton("+ Tambah ke Keranjang")
        self.btnTambahKeranjang.setStyleSheet(
            "background-color:#27ae60;color:white;"
        )

        qtyLayout.addWidget(lblQty)
        qtyLayout.addWidget(self.spinQty)
        qtyLayout.addStretch()
        qtyLayout.addWidget(self.btnTambahKeranjang)
        self.leftLayout.addLayout(qtyLayout)

        # ================= RIGHT PANEL =================
        self.rightPanel = QtWidgets.QFrame()
        self.rightLayout = QtWidgets.QVBoxLayout(self.rightPanel)
        self.rightLayout.setSpacing(15)

        lblKeranjang = QtWidgets.QLabel("🛒 Keranjang Belanja")
        lblKeranjang.setAlignment(QtCore.Qt.AlignCenter)
        lblKeranjang.setStyleSheet("font-size:18px;font-weight:bold;")
        self.rightLayout.addWidget(lblKeranjang)

        self.tableKeranjang = QtWidgets.QTableWidget()
        self.tableKeranjang.setColumnCount(4)
        self.tableKeranjang.setHorizontalHeaderLabels(
            ["Nama Item", "Qty", "Harga", "Subtotal"]
        )
        self.tableKeranjang.verticalHeader().setVisible(False)
        self.tableKeranjang.setAlternatingRowColors(True)
        self.tableKeranjang.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableKeranjang.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableKeranjang.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableKeranjang.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.rightLayout.addWidget(self.tableKeranjang)

        # ===== TOTAL =====
        totalBox = QtWidgets.QFrame()
        totalBox.setStyleSheet("background-color:#f8f9fa;border-radius:8px;")
        totalLayout = QtWidgets.QHBoxLayout(totalBox)

        lblTotalText = QtWidgets.QLabel("TOTAL")
        lblTotalText.setStyleSheet("font-weight:bold;font-size:16px;")

        self.lblTotal = QtWidgets.QLabel("Rp 0")
        self.lblTotal.setStyleSheet("font-size:26px;font-weight:bold;color:#e74c3c;")
        self.lblTotal.setAlignment(QtCore.Qt.AlignRight)

        totalLayout.addWidget(lblTotalText)
        totalLayout.addWidget(self.lblTotal)
        self.rightLayout.addWidget(totalBox)

        # ===== BAYAR =====
        bayarLayout = QtWidgets.QFormLayout()
        self.inputBayar = QtWidgets.QLineEdit()
        self.inputBayar.setValidator(QtGui.QIntValidator())

        self.lblKembalian = QtWidgets.QLabel("Rp 0")
        self.lblKembalian.setStyleSheet("font-weight:bold;color:#27ae60;")

        bayarLayout.addRow("Bayar (Rp):", self.inputBayar)
        bayarLayout.addRow("Kembalian:", self.lblKembalian)
        self.rightLayout.addLayout(bayarLayout)

        # ===== BUTTON =====
        btnGrid = QtWidgets.QGridLayout()

        self.btnHapusItem = QtWidgets.QPushButton("Hapus Item")
        self.btnHapusItem.setStyleSheet("background-color:#e74c3c;color:white;")

        self.btnReset = QtWidgets.QPushButton("Reset")
        self.btnReset.setStyleSheet("background-color:#95a5a6;color:white;")

        self.btnSimpanTransaksi = QtWidgets.QPushButton("Simpan & Cetak")
        self.btnSimpanTransaksi.setMinimumHeight(45)
        self.btnSimpanTransaksi.setStyleSheet(
            "background-color:#2980b9;color:white;font-size:16px;"
        )

        self.btnKembali = QtWidgets.QPushButton("Kembali")

        btnGrid.addWidget(self.btnHapusItem, 0, 0)
        btnGrid.addWidget(self.btnReset, 0, 1)
        btnGrid.addWidget(self.btnSimpanTransaksi, 1, 0, 1, 2)
        btnGrid.addWidget(self.btnKembali, 2, 0, 1, 2)

        self.rightLayout.addLayout(btnGrid)

        # ================= FINAL =================
        self.mainLayout.addWidget(self.leftPanel, 1)
        self.mainLayout.addWidget(self.rightPanel, 1)
        FormTransaksi.setCentralWidget(self.centralwidget)

        # ===== LOGIC (TIDAK DIUBAH) =====
        self.total = 0
        self.loadProduk()

        self.btnCariProduk.clicked.connect(self.searchProduk)
        self.btnTambahKeranjang.clicked.connect(self.tambahKeranjang)
        self.btnHapusItem.clicked.connect(self.hapusItem)
        self.btnReset.clicked.connect(self.resetKeranjang)
        self.btnSimpanTransaksi.clicked.connect(self.simpanTransaksi)
        self.btnKembali.clicked.connect(FormTransaksi.close)
        self.inputBayar.textChanged.connect(self.hitungKembalian)


    # =====================================================
    # LOAD PRODUK
    # =====================================================
    def loadProduk(self):
        rows = Produk.select_for_kasir()
        self.tableProduk.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.tableProduk.setItem(i, j, QTableWidgetItem(str(val)))

    # =====================================================
    # SEARCH PRODUK
    # =====================================================
    def searchProduk(self):
        keyword = self.inputSearchProduk.text()
        db, cursor = get_connection()
        cursor.execute("""
            SELECT id_produk, nama_produk, harga, stok
            FROM produk
            WHERE stok > 0 AND (nama_produk LIKE %s OR id_produk LIKE %s)
        """, (f"%{keyword}%", f"%{keyword}%"))
        rows = cursor.fetchall()
        cursor.close()
        db.close()

        self.tableProduk.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.tableProduk.setItem(i, j, QTableWidgetItem(str(val)))

    # =====================================================
    # TAMBAH KE KERANJANG (STOK REALTIME UI)
    # =====================================================
    def tambahKeranjang(self):
        row = self.tableProduk.currentRow()
        if row < 0:
            return

        nama = self.tableProduk.item(row, 1).text()
        harga = int(float(self.tableProduk.item(row, 2).text()))
        stok = int(self.tableProduk.item(row, 3).text())
        qty = self.spinQty.value()

        if qty > stok:
            QMessageBox.warning(None, "Error", "Stok tidak cukup")
            return

        for i in range(self.tableKeranjang.rowCount()):
            if self.tableKeranjang.item(i, 0).text() == nama:
                old_qty = int(self.tableKeranjang.item(i, 1).text())
                old_sub = int(self.tableKeranjang.item(i, 3).text())
                new_qty = old_qty + qty
                new_sub = new_qty * harga

                self.tableKeranjang.setItem(i, 1, QTableWidgetItem(str(new_qty)))
                self.tableKeranjang.setItem(i, 3, QTableWidgetItem(str(new_sub)))

                self.total += (new_sub - old_sub)
                self.lblTotal.setText(f"Rp {self.total}")

                self.tableProduk.setItem(row, 3, QTableWidgetItem(str(stok - qty)))
                return

        subtotal = harga * qty
        r = self.tableKeranjang.rowCount()
        self.tableKeranjang.insertRow(r)
        self.tableKeranjang.setItem(r, 0, QTableWidgetItem(nama))
        self.tableKeranjang.setItem(r, 1, QTableWidgetItem(str(qty)))
        self.tableKeranjang.setItem(r, 2, QTableWidgetItem(str(harga)))
        self.tableKeranjang.setItem(r, 3, QTableWidgetItem(str(subtotal)))

        self.total += subtotal
        self.lblTotal.setText(f"Rp {self.total}")
        self.tableProduk.setItem(row, 3, QTableWidgetItem(str(stok - qty)))

    # =====================================================
    # HAPUS ITEM (STOK BALIK)
    # =====================================================
    def hapusItem(self):
        row = self.tableKeranjang.currentRow()
        if row < 0:
            return

        nama = self.tableKeranjang.item(row, 0).text()
        qty = int(self.tableKeranjang.item(row, 1).text())
        subtotal = int(self.tableKeranjang.item(row, 3).text())

        for i in range(self.tableProduk.rowCount()):
            if self.tableProduk.item(i, 1).text() == nama:
                stok = int(self.tableProduk.item(i, 3).text())
                self.tableProduk.setItem(i, 3, QTableWidgetItem(str(stok + qty)))
                break

        self.total -= subtotal
        self.lblTotal.setText(f"Rp {self.total}")
        self.tableKeranjang.removeRow(row)

    # =====================================================
    # RESET
    # =====================================================
    def resetKeranjang(self):
        self.tableKeranjang.setRowCount(0)
        self.total = 0
        self.lblTotal.setText("Rp 0")
        self.lblKembalian.setText("Rp 0")
        self.inputBayar.clear()
        self.loadProduk()

    # =====================================================
    # KEMBALIAN
    # =====================================================
    def hitungKembalian(self):
        try:
            bayar = int(self.inputBayar.text())
            self.lblKembalian.setText(f"Rp {bayar - self.total}")
        except:
            self.lblKembalian.setText("Rp 0")

    # =====================================================
    # SIMPAN TRANSAKSI (DATABASE)
    # =====================================================
    def simpanTransaksi(self):
        if self.tableKeranjang.rowCount() == 0:
            return

        try:
            bayar = int(self.inputBayar.text())
        except:
            QMessageBox.warning(None, "Error", "Masukkan uang bayar!")
            return

        if bayar < self.total:
            QMessageBox.warning(None, "Error", "Uang tidak cukup")
            return

        kembali = bayar - self.total

        tr = Transaksi(kasir=self.user_login.nama)
        list_struk = []

        db, cursor = get_connection()
        try:
            for i in range(self.tableKeranjang.rowCount()):
                nama = self.tableKeranjang.item(i, 0).text()
                qty = int(self.tableKeranjang.item(i, 1).text())

                cursor.execute(
                    "SELECT id_produk, harga FROM produk WHERE nama_produk=%s",
                    (nama,)
                )
                row = cursor.fetchone()

                if not row:
                    raise Exception(f"Produk '{nama}' tidak ditemukan")

                idp, harga = row
                harga = int(float(harga))
                subtotal = harga * qty

                # detail transaksi
                det = DetailTransaksi(id_produk=idp, qty=qty)
                tr.tambah_detail(det)

                # data struk
                list_struk.append({
                    "produk": nama,
                    "qty": qty,
                    "harga": harga,
                    "subtotal": subtotal
                })

            # simpan transaksi + detail (stok DB berkurang di model)
            id_trx = tr.simpan()

            QMessageBox.information(
                None,
                "Sukses",
                f"Transaksi #{id_trx} berhasil disimpan!"
            )

            # =========================
            # TAMPILKAN STRUK
            # =========================
            self.struk_window = QtWidgets.QDialog()
            self.struk_ui = StrukWindow()
            self.struk_ui.setupUi(self.struk_window)
            self.struk_ui.loadData(
                list_struk,
                tr.total,
                bayar,
                kembali,
                nama_kasir=self.user_login.nama
            )

            # dialog modal (harus ditutup dulu)
            self.struk_window.exec_()

            # setelah struk ditutup → reset
            self.resetKeranjang()

        except Exception as e:
            db.rollback()
            QMessageBox.critical(None, "Error", str(e))

        finally:
            cursor.close()
            db.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_FormTransaksi()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
