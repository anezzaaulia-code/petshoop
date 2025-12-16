import mysql.connector
from datetime import datetime
from database.connect import get_connection

class Transaksi:
    def __init__(self, id_transaksi=None, kasir=""):
        self.id_transaksi = id_transaksi
        self.tanggal = datetime.now()
        self.kasir = kasir
        self.total = 0
        self.detail_list = []

    # Tambah detail transaksi
    def tambah_detail(self, detail):
        self.detail_list.append(detail)
        self.hitung_total()

    # Hitung total otomatis
    def hitung_total(self):
        self.total = sum(d.subtotal for d in self.detail_list)

    # Simpan transaksi utama + detail
    def simpan(self):
        db, cursor = get_connection()
        if not db or not cursor:
            print("❌ Koneksi database gagal.")
            return None

        # Simpan transaksi utama
        sql_tr = """
            INSERT INTO transaksi (tanggal, kasir, total)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql_tr, (self.tanggal, self.kasir, self.total))

        # Ambil ID transaksi baru
        self.id_transaksi = cursor.lastrowid

        # Simpan detail transaksi
        for d in self.detail_list:
            d.id_transaksi = self.id_transaksi
            d.insert(cursor)   # memakai cursor dari transaksi

        db.commit()
        cursor.close()
        db.close()

        return self.id_transaksi
