import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="petshop"
)

mycursor = mydb.cursor()

# Menambahkan kolom 'kategori' ke tabel 'barang'
# mycursor.execute("ALTER TABLE produk ADD COLUMN kategori VARCHAR(50)")

# print("Kolom 'kategori' berhasil ditambahkan ke tabel 'produk'.")

# mycursor.execute("ALTER TABLE produk ADD COLUMN kategori VARCHAR(50) AFTER jenis_hewan")
# print("Kolom 'kategori' berhasil ditambahkan ke tabel 'produk' setelah kolom 'jenis_hewan'.")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS transaksi (
    id_transaksi INT AUTO_INCREMENT PRIMARY KEY,
    tanggal DATETIME NOT NULL,
    kasir VARCHAR(100) NOT NULL,
    total INT NOT NULL
)
""")
print("Tabel 'transaksi' siap digunakan.")


# ==========================================
# CREATE TABLE detail_transaksi (jika belum ada)
# ==========================================
mycursor.execute("""
CREATE TABLE IF NOT EXISTS detail_transaksi (
    id_detail INT AUTO_INCREMENT PRIMARY KEY,
    id_transaksi INT NOT NULL,
    id_produk INT NOT NULL,
    qty INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_transaksi
        FOREIGN KEY (id_transaksi)
        REFERENCES transaksi(id_transaksi)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_produk
        FOREIGN KEY (id_produk)
        REFERENCES produk(id_produk)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
ENGINE=InnoDB;
""")

print("Tabel 'detail_transaksi' siap digunakan.")

