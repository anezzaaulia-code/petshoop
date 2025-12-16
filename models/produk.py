import mysql.connector
from database.connect import get_connection


class Produk:
    def __init__(self, id_produk, nama_produk, harga, stok, jenis_hewan, kategori):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.harga = harga
        self.stok = stok
        self.jenis_hewan = jenis_hewan
        self.kategori = kategori

    # =====================================================
    # SUPERVISOR - LIHAT SEMUA PRODUK (STOK AMAN)
    # =====================================================
    @staticmethod
    def select_all():
        db, cursor = get_connection()
        cursor.execute("""
            SELECT id_produk, nama_produk, harga,
                   CASE WHEN stok < 0 THEN 0 ELSE stok END AS stok,
                   jenis_hewan, kategori
            FROM produk
        """)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    # =====================================================
    # KASIR - HANYA PRODUK STOK TERSEDIA
    # =====================================================
    @staticmethod
    def select_for_kasir():
        db, cursor = get_connection()
        cursor.execute("""
            SELECT id_produk, nama_produk, harga, stok
            FROM produk
            WHERE stok > 0
        """)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    # =====================================================
    # SEARCH SUPERVISOR
    # =====================================================
    @staticmethod
    def search(keyword):
        db, cursor = get_connection()
        cursor.execute("""
            SELECT id_produk, nama_produk, harga,
                   CASE WHEN stok < 0 THEN 0 ELSE stok END AS stok,
                   jenis_hewan, kategori
            FROM produk
            WHERE nama_produk LIKE %s
        """, (f"%{keyword}%",))
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    # =====================================================
    # INSERT PRODUK (STOK MINIMAL 0)
    # =====================================================
    def insert(self):
        if self.stok < 0:
            self.stok = 0

        db, cursor = get_connection()
        cursor.execute("""
            INSERT INTO produk (id_produk, nama_produk, harga, stok, jenis_hewan, kategori)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            self.id_produk,
            self.nama_produk,
            self.harga,
            self.stok,
            self.jenis_hewan,
            self.kategori
        ))
        db.commit()
        cursor.close()
        db.close()
        return self.id_produk

    # =====================================================
    # UPDATE PRODUK (ANTI STOK MINUS)
    # =====================================================
    def update(self):
        stok_fix = self.stok if self.stok >= 0 else 0

        db, cursor = get_connection()
        cursor.execute("""
            UPDATE produk
            SET nama_produk=%s, harga=%s, stok=%s,
                jenis_hewan=%s, kategori=%s
            WHERE id_produk=%s
        """, (
            self.nama_produk,
            self.harga,
            stok_fix,
            self.jenis_hewan,
            self.kategori,
            self.id_produk
        ))
        db.commit()
        cursor.close()
        db.close()

    # =====================================================
    # KURANGI STOK (SATU-SATUNYA CARA KURANG STOK)
    # =====================================================
    @staticmethod
    def kurangi_stok(id_produk, qty):
        db, cursor = get_connection()

        cursor.execute(
            "SELECT stok FROM produk WHERE id_produk=%s",
            (id_produk,)
        )
        row = cursor.fetchone()

        if not row:
            cursor.close()
            db.close()
            raise Exception("Produk tidak ditemukan")

        stok = row[0]

        if stok < qty:
            cursor.close()
            db.close()
            raise Exception("Stok tidak cukup")

        cursor.execute("""
            UPDATE produk
            SET stok = stok - %s
            WHERE id_produk = %s
        """, (qty, id_produk))

        db.commit()
        cursor.close()
        db.close()

    # =====================================================
    # DELETE PRODUK
    # =====================================================
    @staticmethod
    def delete_by_id(id_produk):
        db, cursor = get_connection()
        cursor.execute("DELETE FROM makanan_hewan WHERE id_produk=%s", (id_produk,))
        cursor.execute("DELETE FROM aksesoris_hewan WHERE id_produk=%s", (id_produk,))
        cursor.execute("DELETE FROM produk WHERE id_produk=%s", (id_produk,))
        db.commit()
        cursor.close()
        db.close()

# =====================================================
#               AKSESORIS HEWAN
# =====================================================
class AksesorisHewan(Produk):
    def __init__(self, id_produk, nama_produk, harga, stok,
                 jenis_hewan, warna, ukuran):

        super().__init__(
            id_produk=id_produk,
            nama_produk=nama_produk,
            harga=harga,
            stok=stok if stok >= 0 else 0,
            jenis_hewan=jenis_hewan,
            kategori="Aksesoris Hewan"
        )

        self.warna = warna
        self.ukuran = ukuran

    def insert(self):
        super().insert()

        db, cursor = get_connection()
        cursor.execute("""
            INSERT INTO aksesoris_hewan 
            (id_produk, warna_aksesoris, ukuran_aksesoris)
            VALUES (%s, %s, %s)
        """, (self.id_produk, self.warna, self.ukuran))

        db.commit()
        cursor.close()
        db.close()

    def update_child(self, warna_baru, ukuran_baru):
        db, cursor = get_connection()
        cursor.execute("""
            UPDATE aksesoris_hewan
            SET warna_aksesoris=%s, ukuran_aksesoris=%s
            WHERE id_produk=%s
        """, (warna_baru, ukuran_baru, self.id_produk))

        db.commit()
        cursor.close()
        db.close()


# =====================================================
#               MAKANAN HEWAN
# =====================================================
class MakananHewan(Produk):
    def __init__(self, id_produk, nama_produk, harga, stok,
                 jenis_hewan, masa_exp, jenis_makanan):

        super().__init__(
            id_produk=id_produk,
            nama_produk=nama_produk,
            harga=harga,
            stok=stok if stok >= 0 else 0,
            jenis_hewan=jenis_hewan,
            kategori="Makanan Hewan"
        )

        self.masa_exp = masa_exp
        self.jenis_makanan = jenis_makanan

    def insert(self):
        db, cursor = get_connection()

        cursor.execute(
            "SELECT stok FROM produk WHERE id_produk=%s",
            (self.id_produk,)
        )
        row = cursor.fetchone()

        if row:
            cursor.execute("""
                UPDATE produk
                SET stok = stok + %s
                WHERE id_produk = %s
            """, (self.stok, self.id_produk))
        else:
            cursor.execute("""
                INSERT INTO produk
                (id_produk, nama_produk, harga, stok, jenis_hewan, kategori)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                self.id_produk,
                self.nama_produk,
                self.harga,
                self.stok,
                self.jenis_hewan,
                self.kategori
            ))

        db.commit()
        cursor.close()
        db.close()

    def update_child(self, masa_exp_baru, jenis_makanan_baru):
        db, cursor = get_connection()
        cursor.execute("""
            UPDATE makanan_hewan
            SET masa_exp=%s, jenis_makanan=%s
            WHERE id_produk=%s
        """, (masa_exp_baru, jenis_makanan_baru, self.id_produk))

        db.commit()
        cursor.close()
        db.close()