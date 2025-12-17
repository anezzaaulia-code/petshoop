# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView, QFormLayout, QFrame

from database.connect import get_connection
from models.produk import Produk
from models.transaksi import Transaksi
from models.detail_transaksi import DetailTransaksi
from ui.kasir.form_struk import Ui_MainWindow as StrukWindow


class Ui_FormTransaksi(object):

    # =====================================================
    # STYLESHEET MODERN & CERIA
    # =====================================================
    TRANSACTION_STYLE = """
        /* GLOBAL STYLE */
        QWidget {
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 14px;
            color: #333333; /* Teks gelap netral */
        }
        QMainWindow, QWidget#centralwidget {
            background-color: #fcfcfc; /* Background Putih Krem */
        }
        QFrame {
            background-color: #ffffff;
            border-radius: 12px; /* Sudut lebih lembut */
            border: 1px solid #e0e0e0; /* Border halus */
        }
        
        /* INPUT & SPINBOX */
        QLineEdit, QSpinBox {
            padding: 10px;
            border: 1px solid #cfd8dc; /* Abu-abu Teal */
            border-radius: 8px;
            background-color: #f7f7f7;
        }
        QLineEdit:focus, QSpinBox:focus {
            border: 2px solid #00bcd4; /* Teal Cerah saat fokus */
            background-color: white;
        }
        
        /* TABLES */
        QTableWidget {
            border: 1px solid #e0e0e0;
            gridline-color: #f0f0f0;
            selection-background-color: #b2ebf2; /* Teal muda saat dipilih */
            selection-color: #333333;
            border-radius: 8px;
        }
        QHeaderView::section {
            background-color: #e0f2f1; /* Teal Pastel */
            color: #004d40;
            padding: 8px;
            border: 1px solid #b2dfdb;
            font-weight: bold;
            font-size: 15px;
        }
        
        /* BUTTONS (GENERAL) */
        QPushButton {
            padding: 12px;
            border-radius: 10px;
            font-weight: bold;
            border: none;
            color: white;
            min-height: 35px;
        }
        QPushButton:hover {
            opacity: 0.9;
        }

        /* BUTTONS (SPECIFIC COLORS) */
        #btnCariProduk { 
            background-color: #ff9800; /* Orange Ceria */
        }
        #btnTambahKeranjang {
            background-color: #4CAF50; /* Hijau Cerah */
        }
        #btnHapusItem { 
            background-color: #F44336; /* Merah */
        }
        #btnReset { 
            background-color: #90a4ae; /* Abu-abu netral */
        }
        #btnSimpanTransaksi {
            background-color: #00BCD4; /* Teal Utama */
            font-size: 18px;
            min-height: 50px;
        }
        #btnKembali {
            background-color: #607d8b; /* Abu-abu Kebiruan */
            color: white;
        }

        /* TOTAL FRAME */
        QFrame#totalBox {
            background-color: #e0f7fa; /* Teal Sangat Muda */
            border: 2px solid #00bcd4;
            border-radius: 10px;
        }
    """

    # =====================================================
    # SETUP UI 
    # =====================================================
    def setupUi(self, FormTransaksi, user_login):
        self.user_login = user_login
        FormTransaksi.setObjectName("FormTransaksi")
        FormTransaksi.resize(1150, 780) # Diperlebar agar nyaman
        FormTransaksi.setStyleSheet(self.TRANSACTION_STYLE) # Terapkan Stylesheet

        self.centralwidget = QtWidgets.QWidget(FormTransaksi)
        self.mainLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(30, 30, 30, 30)
        self.mainLayout.setSpacing(30)

        # ================= LEFT PANEL =================
        self.leftPanel = QtWidgets.QFrame()
        self.leftLayout = QtWidgets.QVBoxLayout(self.leftPanel)
        self.leftLayout.setSpacing(15)

        lblProduk = QtWidgets.QLabel("📦 Daftar Produk Tersedia")
        lblProduk.setStyleSheet("font-size:20px;font-weight:bold;color:#00796b;")
        self.leftLayout.addWidget(lblProduk)

        searchLayout = QtWidgets.QHBoxLayout()
        self.inputSearchProduk = QtWidgets.QLineEdit()
        self.inputSearchProduk.setPlaceholderText("Cari nama / ID produk...")
        self.btnCariProduk = QtWidgets.QPushButton("Cari 🔎")
        self.btnCariProduk.setObjectName("btnCariProduk") 

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
        lblQty = QtWidgets.QLabel("Jumlah Item:")
        lblQty.setStyleSheet("font-weight:bold;")
        self.spinQty = QtWidgets.QSpinBox()
        self.spinQty.setMinimum(1)
        self.spinQty.setFixedWidth(100)
        self.spinQty.setMaximum(9999) # Batas maksimum

        self.btnTambahKeranjang = QtWidgets.QPushButton("+ Tambah ke Keranjang")
        self.btnTambahKeranjang.setObjectName("btnTambahKeranjang")

        qtyLayout.addWidget(lblQty)
        qtyLayout.addWidget(self.spinQty)
        qtyLayout.addStretch()
        qtyLayout.addWidget(self.btnTambahKeranjang)
        self.leftLayout.addLayout(qtyLayout)

        # ================= RIGHT PANEL =================
        self.rightPanel = QtWidgets.QFrame()
        self.rightLayout = QtWidgets.QVBoxLayout(self.rightPanel)
        self.rightLayout.setSpacing(15)

        lblKeranjang = QtWidgets.QLabel("🛒 Keranjang Belanja Anda")
        lblKeranjang.setAlignment(QtCore.Qt.AlignCenter)
        lblKeranjang.setStyleSheet("font-size:20px;font-weight:bold;color:#00796b;")
        self.rightLayout.addWidget(lblKeranjang)

        self.tableKeranjang = QtWidgets.QTableWidget()
        self.tableKeranjang.setColumnCount(4)
        self.tableKeranjang.setHorizontalHeaderLabels(
            ["Nama Item", "Qty", "Harga (Rp)", "Subtotal (Rp)"]
        )
        self.tableKeranjang.verticalHeader().setVisible(False)
        self.tableKeranjang.setAlternatingRowColors(True)
        self.tableKeranjang.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableKeranjang.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableKeranjang.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableKeranjang.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.rightLayout.addWidget(self.tableKeranjang)

        # ===== TOTAL =====
        self.totalBox = QtWidgets.QFrame()
        self.totalBox.setObjectName("totalBox")
        totalLayout = QtWidgets.QHBoxLayout(self.totalBox)

        lblTotalText = QtWidgets.QLabel("TOTAL BELANJA")
        lblTotalText.setStyleSheet("font-weight:bold;font-size:16px;")

        self.lblTotal = QtWidgets.QLabel("Rp 0")
        self.lblTotal.setStyleSheet("font-size:30px;font-weight:bold;color:#e74c3c;") # Merah cerah untuk Total
        self.lblTotal.setAlignment(QtCore.Qt.AlignRight)

        totalLayout.addWidget(lblTotalText)
        totalLayout.addWidget(self.lblTotal)
        self.rightLayout.addWidget(self.totalBox)

        # ===== BAYAR =====
        bayarLayout = QtWidgets.QFormLayout()
        self.inputBayar = QtWidgets.QLineEdit()
        self.inputBayar.setValidator(QtGui.QIntValidator())
        self.inputBayar.setPlaceholderText("Masukkan jumlah uang tunai...")

        self.lblKembalian = QtWidgets.QLabel("Rp 0")
        self.lblKembalian.setStyleSheet("font-weight:bold;font-size:16px;color:#27ae60;") # Hijau untuk Kembalian

        bayarLayout.addRow("Uang Bayar (Rp):", self.inputBayar)
        bayarLayout.addRow("Kembalian:", self.lblKembalian)
        self.rightLayout.addLayout(bayarLayout)

        # ===== BUTTON =====
        btnGrid = QtWidgets.QGridLayout()

        self.btnHapusItem = QtWidgets.QPushButton("Hapus Item 🗑️")
        self.btnHapusItem.setObjectName("btnHapusItem")

        self.btnReset = QtWidgets.QPushButton("Reset Semua")
        self.btnReset.setObjectName("btnReset")

        self.btnSimpanTransaksi = QtWidgets.QPushButton("Simpan & Cetak Struk 🖨️")
        self.btnSimpanTransaksi.setObjectName("btnSimpanTransaksi")
        self.btnSimpanTransaksi.setMinimumHeight(60)

        self.btnKembali = QtWidgets.QPushButton("Kembali ke Dashboard")
        self.btnKembali.setObjectName("btnKembali")

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
                # Format Harga di kolom 2
                if j == 2:
                    text = f"Rp {float(val):,.0f}"
                else:
                    text = str(val)
                self.tableProduk.setItem(i, j, QTableWidgetItem(text))

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
                # Format Harga di kolom 2
                if j == 2:
                    text = f"Rp {float(val):,.0f}"
                else:
                    text = str(val)
                self.tableProduk.setItem(i, j, QTableWidgetItem(text))

    # =====================================================
    # TAMBAH KE KERANJANG (STOK REALTIME UI)
    # =====================================================
    def tambahKeranjang(self):
        row = self.tableProduk.currentRow()
        if row < 0:
            QMessageBox.warning(None, "Peringatan", "Pilih produk dari daftar terlebih dahulu.")
            return

        nama = self.tableProduk.item(row, 1).text()
        # Ekstrak harga dari format "Rp 12,345"
        try:
            harga_str = self.tableProduk.item(row, 2).text().replace("Rp ", "").replace(",", "")
            harga = int(float(harga_str))
        except ValueError:
             QMessageBox.critical(None, "Error Data", "Format harga di tabel produk tidak valid.")
             return

        stok = int(self.tableProduk.item(row, 3).text())
        qty = self.spinQty.value()

        if qty > stok:
            QMessageBox.warning(None, "Stok Kurang", "Stok produk tidak cukup untuk jumlah yang diminta.")
            return

        # Cari item di keranjang
        item_found = False
        for i in range(self.tableKeranjang.rowCount()):
            if self.tableKeranjang.item(i, 0).text() == nama:
                old_qty = int(self.tableKeranjang.item(i, 1).text())
                # Ekstrak subtotal dari format "Rp 12,345"
                old_sub_str = self.tableKeranjang.item(i, 3).text().replace("Rp ", "").replace(",", "")
                old_sub = int(old_sub_str)
                
                new_qty = old_qty + qty
                new_sub = new_qty * harga

                self.tableKeranjang.setItem(i, 1, QTableWidgetItem(str(new_qty)))
                self.tableKeranjang.setItem(i, 3, QTableWidgetItem(f"Rp {new_sub:,.0f}"))

                self.total += (new_sub - old_sub)
                self.lblTotal.setText(f"Rp {self.total:,.0f}")

                # Update stok di tabel produk
                self.tableProduk.setItem(row, 3, QTableWidgetItem(str(stok - qty)))
                item_found = True
                break
        
        if not item_found:
            subtotal = harga * qty
            r = self.tableKeranjang.rowCount()
            self.tableKeranjang.insertRow(r)
            
            self.tableKeranjang.setItem(r, 0, QTableWidgetItem(nama))
            self.tableKeranjang.setItem(r, 1, QTableWidgetItem(str(qty)))
            self.tableKeranjang.setItem(r, 2, QTableWidgetItem(f"Rp {harga:,.0f}"))
            self.tableKeranjang.setItem(r, 3, QTableWidgetItem(f"Rp {subtotal:,.0f}"))

            self.total += subtotal
            self.lblTotal.setText(f"Rp {self.total:,.0f}")
            self.tableProduk.setItem(row, 3, QTableWidgetItem(str(stok - qty)))


    # =====================================================
    # HAPUS ITEM (STOK BALIK)
    # =====================================================
    def hapusItem(self):
        row = self.tableKeranjang.currentRow()
        if row < 0:
            QMessageBox.warning(None, "Peringatan", "Pilih item di keranjang untuk dihapus.")
            return

        nama = self.tableKeranjang.item(row, 0).text()
        qty = int(self.tableKeranjang.item(row, 1).text())
        subtotal_str = self.tableKeranjang.item(row, 3).text().replace("Rp ", "").replace(",", "")
        subtotal = int(subtotal_str)

        for i in range(self.tableProduk.rowCount()):
            if self.tableProduk.item(i, 1).text() == nama:
                # Update stok di tabel produk
                stok = int(self.tableProduk.item(i, 3).text())
                self.tableProduk.setItem(i, 3, QTableWidgetItem(str(stok + qty)))
                break

        self.total -= subtotal
        self.lblTotal.setText(f"Rp {self.total:,.0f}")
        self.tableKeranjang.removeRow(row)
        self.hitungKembalian()

    # =====================================================
    # RESET
    # =====================================================
    def resetKeranjang(self):
        # Kembalikan stok yang tersisa di keranjang
        if self.tableKeranjang.rowCount() > 0:
            # Iterasi keranjang untuk mengembalikan stok ke tabel produk
            for r in range(self.tableKeranjang.rowCount()):
                nama = self.tableKeranjang.item(r, 0).text()
                qty = int(self.tableKeranjang.item(r, 1).text())

                for i in range(self.tableProduk.rowCount()):
                    if self.tableProduk.item(i, 1).text() == nama:
                        stok = int(self.tableProduk.item(i, 3).text())
                        self.tableProduk.setItem(i, 3, QTableWidgetItem(str(stok + qty)))
                        break
        
        self.tableKeranjang.setRowCount(0)
        self.total = 0
        self.lblTotal.setText("Rp 0")
        self.lblKembalian.setText("Rp 0")
        self.inputBayar.clear()
        # Tidak perlu loadProduk penuh, stok sudah dikembalikan di UI.
        
    # =====================================================
    # KEMBALIAN
    # =====================================================
    def hitungKembalian(self):
        try:
            bayar = int(self.inputBayar.text().replace(".", "")) # Hapus titik jika ada
            kembali = bayar - self.total
            self.lblKembalian.setText(f"Rp {kembali:,.0f}")
            if kembali < 0:
                 self.lblKembalian.setStyleSheet("font-weight:bold;font-size:16px;color:#F44336;")
            else:
                 self.lblKembalian.setStyleSheet("font-weight:bold;font-size:16px;color:#27ae60;")

        except:
            self.lblKembalian.setText("Rp 0")
            self.lblKembalian.setStyleSheet("font-weight:bold;font-size:16px;color:#27ae60;")


    # =====================================================
    # SIMPAN TRANSAKSI (DATABASE)
    # =====================================================
    def simpanTransaksi(self):
        if self.tableKeranjang.rowCount() == 0:
            QMessageBox.warning(None, "Error", "Keranjang belanja masih kosong!")
            return

        try:
            bayar = int(self.inputBayar.text().replace(".", ""))
        except:
            QMessageBox.warning(None, "Error", "Masukkan jumlah uang bayar yang valid!")
            return

        if bayar < self.total:
            QMessageBox.warning(None, "Error", "Uang yang dibayarkan tidak cukup.")
            return

        kembali = bayar - self.total

        tr = Transaksi(kasir=self.user_login.nama)
        list_struk = []

        db, cursor = get_connection()
        try:
            for i in range(self.tableKeranjang.rowCount()):
                nama = self.tableKeranjang.item(i, 0).text()
                qty = int(self.tableKeranjang.item(i, 1).text())
                
                # Mendapatkan ID dan harga dari DB
                cursor.execute(
                    "SELECT id_produk, harga FROM produk WHERE nama_produk=%s",
                    (nama,)
                )
                row = cursor.fetchone()

                if not row:
                    raise Exception(f"Produk '{nama}' tidak ditemukan di database.")

                idp, harga_db = row
                harga_db = int(float(harga_db))
                subtotal = harga_db * qty

                # detail transaksi
                det = DetailTransaksi(id_produk=idp, qty=qty)
                tr.tambah_detail(det)

                # data struk
                list_struk.append({
                    "produk": nama,
                    "qty": qty,
                    "harga": harga_db,
                    "subtotal": subtotal
                })

            # simpan transaksi + detail (stok DB berkurang di model)
            id_trx = tr.simpan()

            QMessageBox.information(
                None,
                "Sukses!",
                f"Transaksi #{id_trx} berhasil disimpan! Struk akan dicetak."
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
                nama_kasir=self.user_login.nama,
            )

            self.struk_window.exec_()

            # setelah struk ditutup → reset
            self.resetKeranjang()

        except Exception as e:
            db.rollback()
            QMessageBox.critical(None, "Error Transaksi", f"Gagal menyimpan transaksi: {str(e)}")

        finally:
            cursor.close()
            db.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    
    # Dummy user login for testing
    class DummyUser:
        def __init__(self):
            self.nama = "Kasir Test"
    
    ui = Ui_FormTransaksi()
    ui.setupUi(Form, DummyUser())
    Form.show()
    sys.exit(app.exec_())