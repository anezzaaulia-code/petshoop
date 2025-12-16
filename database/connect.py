import mysql.connector

def get_connection():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="petshop"
        )
        cursor = db.cursor(buffered=True)  # ← FIX PALING PENTING
        return db, cursor

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None
