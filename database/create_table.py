import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="petshop"
)

mycursor = mydb.cursor()

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="petshop"
)

mycursor = mydb.cursor()

# === TABEL PRODUK (induk) ===
mycursor.execute("""
CREATE TABLE IF NOT EXISTS produk (
    id_produk INT PRIMARY KEY,      -- manual input, tidak auto increment
    nama_produk VARCHAR(100),
    harga FLOAT,
    stok INT,
    jenis_hewan VARCHAR(50)
)
""")
print("Tabel 'produk' dibuat ✔")


# === TABEL MAKANAN HEWAN (extends produk) ===
mycursor.execute("""
CREATE TABLE IF NOT EXISTS makanan_hewan (
    id_produk INT PRIMARY KEY,      -- sama dengan produk.id_produk
    merk_produk VARCHAR(100),
    masa_exp DATE,
    jenis_makanan VARCHAR(50),
    FOREIGN KEY (id_produk) REFERENCES produk(id_produk)
)
""")
print("Tabel 'makanan_hewan' dibuat ✔")


# === TABEL AKSESORIS HEWAN (extends produk) ===
mycursor.execute("""
CREATE TABLE IF NOT EXISTS aksesoris_hewan (
    id_produk INT PRIMARY KEY,      -- sama dengan produk.id_produk
    warna_aksesoris VARCHAR(50),
    ukuran_aksesoris VARCHAR(50),
    FOREIGN KEY (id_produk) REFERENCES produk(id_produk)
)
""")
print("Tabel 'aksesoris_hewan' dibuat ✔")

mydb.commit()


mycursor.execute("""
CREATE TABLE kategori (
    id INT(11) PRIMARY KEY AUTO_INCREMENT,
    kategori VARCHAR(50)
)
""")

print("Tabel 'kategori' berhasil dibuat.")
