import mysql.connector

# === Koneksi Database ===
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="petshop"
)
mycursor = mydb.cursor()

class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.role = None
        self.nama = None 


    def login(self):
        sql = "SELECT nama, username, role FROM user WHERE username=%s AND password=%s"
        mycursor.execute(sql, (self.username, self.password))
        data = mycursor.fetchone()

        if data:
            self.nama = data[0]
            self.username = data[1]
            self.role = data[2]
            return True
        return False

    def logout(self):
        self.username = None
        self.role = None

    def info(self):
        sql = "SELECT username, role FROM user WHERE username=%s"
        mycursor.execute(sql, (self.username,))
        return mycursor.fetchone()


class Admin(User):
    def __init__(self, username=None, password=None):
        super().__init__(username, password)

    def select_all(self):
        sql = "SELECT nama, username, password, role FROM user"
        mycursor.execute(sql)
        return mycursor.fetchall()

    def search(self, keyword):
        sql = """
            SELECT nama, username, password, role
            FROM user
            WHERE nama LIKE %s OR username LIKE %s OR role LIKE %s
        """
        like = f"%{keyword}%"
        mycursor.execute(sql, (like, like, like))
        return mycursor.fetchall()

    def tambah_user(self, nama, username, password, role):
        try:
            sql = "INSERT INTO user (nama, username, password, role) VALUES (%s, %s, %s, %s)"
            mycursor.execute(sql, (nama, username, password, role))
            mydb.commit()
            return True
        except mysql.connector.Error:
            return False

    def select_by_username(self, username):
        sql = "SELECT nama, username, password, role FROM user WHERE username=%s"
        mycursor.execute(sql, (username,))
        return mycursor.fetchone()

    def update_user(self, nama, username, password, role, old_username):
        sql = "UPDATE user SET nama=%s, username=%s, password=%s, role=%s WHERE username=%s"
        mycursor.execute(sql, (nama, username, password, role, old_username))
        mydb.commit()
        return True

    def delete_user(self, username):
        sql = "DELETE FROM user WHERE username=%s"
        mycursor.execute(sql, (username,))
        mydb.commit()

class Supervisor(User):
    def __init__(self, username=None, password=None):
        super().__init__(username, password)

    def tambah_produk(self, nama, harga, stok):
        sql = "INSERT INTO barang (nama_barang, harga, stok) VALUES (%s, %s, %s)"
        mycursor.execute(sql, (nama, harga, stok))
        mydb.commit()

    def update_produk(self, id_barang, nama, harga, stok):
        sql = "UPDATE barang SET nama_barang=%s, harga=%s, stok=%s WHERE id=%s"
        mycursor.execute(sql, (nama, harga, stok, id_barang))
        mydb.commit()

    def delete_produk(self, id_barang):
        sql = "DELETE FROM barang WHERE id=%s"
        mycursor.execute(sql, (id_barang,))
        mydb.commit()

    def lihat_produk(self):
        sql = "SELECT id, nama_barang, harga, stok FROM barang"
        mycursor.execute(sql)
        return mycursor.fetchall()


class Kasir(User):
    def __init__(self, username=None, password=None):
        super().__init__(username, password)

    def melihat_daftar_barang(self):
        sql = "SELECT id, nama_barang, harga, stok FROM barang"
        mycursor.execute(sql)
        return mycursor.fetchall()

    def transaksi(self, id_barang, qty):
        sql = "SELECT harga, stok FROM barang WHERE id=%s"
        mycursor.execute(sql, (id_barang,))
        data = mycursor.fetchone()

        if not data:
            return "Barang tidak ditemukan"

        harga, stok = data

        if qty > stok:
            return "Stok tidak cukup"

        total = harga * qty

        sql = "UPDATE barang SET stok = stok - %s WHERE id=%s"
        mycursor.execute(sql, (qty, id_barang))
        mydb.commit()

        return f"Transaksi berhasil. Total Rp {total}"

