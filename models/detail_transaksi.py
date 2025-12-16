from database.connect import get_connection

class DetailTransaksi:
    def __init__(self, id_produk, qty, id_detail=None, id_transaksi=None):
        self.id_detail = id_detail
        self.id_transaksi = id_transaksi
        self.id_produk = id_produk
        self.qty = qty

        self.harga = self.get_harga_produk(id_produk)
        self.subtotal = self.harga * self.qty


    @staticmethod
    def get_harga_produk(id_produk):
        db, cursor = get_connection()
        cursor.execute("SELECT harga FROM produk WHERE id_produk=%s", (id_produk,))
        result = cursor.fetchone()
        cursor.close()
        db.close()

        if not result:
            return 0

        # pastikan harga integer
        try:
            return int(result[0])
        except:
            return int(float(result[0]))


    def insert(self, cursor):
        # Insert detail transaksi
        sql = """
            INSERT INTO detail_transaksi (id_transaksi, id_produk, qty, subtotal)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (
            self.id_transaksi,
            self.id_produk,
            self.qty,
            self.subtotal
        ))

        # Kurangi stok produk
        cursor.execute("""
            UPDATE produk SET stok = stok - %s WHERE id_produk = %s
        """, (self.qty, self.id_produk))
