# -*- coding: utf-8 -*-
import datetime
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("StrukWindow")
        Dialog.resize(380, 500)
        Dialog.setStyleSheet("background-color: #263238;") 

        self.layout = QtWidgets.QVBoxLayout(Dialog)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setAlignment(QtCore.Qt.AlignTop)

        # ===============================
        # FRAME PREVIEW
        # ===============================
        self.paperFrame = QtWidgets.QFrame(Dialog)
        self.paperFrame.setFixedWidth(340) # Frame sedikit diperkecil
        self.paperFrame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-bottom: 5px solid #90A4AE; 
            }
        """)
        
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0, 4)
        self.paperFrame.setGraphicsEffect(shadow)

        self.paperLayout = QtWidgets.QVBoxLayout(self.paperFrame)
        self.paperLayout.setContentsMargins(0, 0, 0, 0)

        # TEXT EDIT
        self.txtStruk = QtWidgets.QTextEdit(self.paperFrame)
        self.txtStruk.setReadOnly(True)
        self.txtStruk.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txtStruk.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtStruk.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        self.txtStruk.setStyleSheet("""
            QTextEdit {
                background-color: transparent;
                padding: 10px; 
            }
        """)

        self.paperLayout.addWidget(self.txtStruk)
        self.layout.addWidget(self.paperFrame, alignment=QtCore.Qt.AlignCenter)

        # ===============================
        # TOMBOL
        # ===============================
        self.btnLayout = QtWidgets.QHBoxLayout()
        self.btnLayout.setContentsMargins(0, 15, 0, 0)

        self.btnCetak = QtWidgets.QPushButton("🖨️ Simpan PDF")
        self.btnCetak.setMinimumHeight(45)
        self.btnCetak.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnCetak.setStyleSheet("""
            QPushButton {
                background-color: #00897B; color: white; font-weight: bold; border-radius: 5px; font-size: 12px;
            }
            QPushButton:hover { background-color: #00695C; }
        """)
        self.btnCetak.clicked.connect(self.cetakPDF)

        self.btnClose = QtWidgets.QPushButton("Tutup")
        self.btnClose.setMinimumHeight(45)
        self.btnClose.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnClose.setStyleSheet("""
            QPushButton {
                background-color: #CFD8DC; color: #37474F; font-weight: bold; border-radius: 5px; font-size: 12px;
            }
            QPushButton:hover { background-color: #B0BEC5; }
        """)
        self.btnClose.clicked.connect(Dialog.close)

        self.btnLayout.addWidget(self.btnCetak)
        self.btnLayout.addWidget(self.btnClose)
        self.layout.addLayout(self.btnLayout)

        Dialog.setWindowTitle("Preview Struk")
        self.dialog = Dialog

    # =====================================================
    # LOGIC CETAK PDF (1 PAGE - FIXED)
    # =====================================================
    def cetakPDF(self):
        filename, _ = QFileDialog.getSaveFileName(
            None, "Simpan Struk PDF", 
            f"Struk_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf", 
            "PDF Files (*.pdf)"
        )

        if not filename: return

        try:
            doc = self.txtStruk.document().clone()

            # Mode ScreenResolution agar ukuran pas
            printer = QPrinter(QPrinter.ScreenResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(filename)
            
            # Lebar 300px cukup untuk font kecil
            target_width = 300
            doc.setTextWidth(target_width)
            
            doc.adjustSize()
            content_height = doc.size().height()
            
            # Buffer sedikit saja karena font sudah kecil
            final_height = content_height + 20

            printer.setPaperSize(QtCore.QSizeF(target_width, final_height), QPrinter.DevicePixel)
            printer.setFullPage(True)
            printer.setPageMargins(0, 0, 0, 0, QPrinter.DevicePixel)
            
            doc.setPageSize(QtCore.QSizeF(target_width, final_height))

            doc.print_(printer)
            QMessageBox.information(None, "Sukses", "PDF disimpan!")

        except Exception as e:
            import traceback
            traceback.print_exc()
            QMessageBox.critical(None, "Error", str(e))

    # =====================================================
    # LOAD DATA (FONT 8pt)
    # =====================================================
    def loadData(self, items, total, bayar, kembali, nama_kasir="Admin"):
        tgl = datetime.datetime.now().strftime("%d/%m/%y")
        jam = datetime.datetime.now().strftime("%H:%M")
        
        def rp(n): return f"{n:,.0f}".replace(",", ".")

        # CSS Styling: Font 8pt (Lebih Kecil)
        style = """
        <style>
            body { 
                font-family: 'Consolas', monospace; 
                font-size: 8pt;  /* UKURAN FONT UTAMA 8pt */
                color: #000;
                margin: 5px;
            }
            .center { text-align: center; }
            .right { text-align: right; }
            .bold { font-weight: bold; }
            
            /* Garis Tipis */
            hr.dashed { border: 0; border-top: 1px dashed #333; margin: 2px 0; }
            hr.solid { border: 0; border-top: 1px solid #000; margin: 2px 0; }
            
            table { width: 100%; border-collapse: collapse; }
            /* Padding 0 agar rapat */
            td { vertical-align: top; padding: 0px; } 
            
            .header-title { font-size: 10pt; font-weight: bold; }
            .footer { font-size: 7pt; color: #555; margin-top: 8px; }
        </style>
        """

        html = f"""
        <html><head>{style}</head><body>
            
            <div class="center">
                <span class="header-title">PETSHOP MARNEZNAT</span><br>
                Jl. Hewan Kesayangan No. 1<br>
                Telp: 0812-8723-2739
            </div>
            
            <hr class="dashed">
            
            <table width="100%">
                <tr>
                    <td width="50%">Tgl: {tgl}</td>
                    <td width="50%" class="right">Jam: {jam}</td>
                </tr>
                <tr>
                    <td colspan="2">Kasir: <b>{nama_kasir}</b></td>
                </tr>
            </table>
            
            <hr class="dashed">
            
            <table width="100%">
        """
        
        for item in items:
            html += f"""
            <tr>
                <td colspan="2" class="bold">{item['produk']}</td>
            </tr>
            <tr>
                <td width="65%" style="padding-left:5px;">{item['qty']} x {rp(item['harga'])}</td>
                <td width="35%" class="right">{rp(item['subtotal'])}</td>
            </tr>
            """
            
        html += f"""
            </table>
            
            <hr class="solid">
            
            <table width="100%">
                <tr>
                    <td class="bold" style="font-size:9pt;">TOTAL</td>
                    <td class="right bold" style="font-size:9pt;">Rp {rp(total)}</td>
                </tr>
                <tr>
                    <td>TUNAI</td>
                    <td class="right">{rp(bayar)}</td>
                </tr>
                <tr>
                    <td>KEMBALI</td>
                    <td class="right">{rp(kembali)}</td>
                </tr>
            </table>
            
            <hr class="dashed">
            
            <div class="center footer">
                <i>Terima Kasih</i><br>
                ** Barang tidak dapat ditukar **
            </div>
            
        </body></html>
        """
        
        self.txtStruk.setHtml(html)
        
        # UI Resize
        self.txtStruk.document().adjustSize()
        doc_height = self.txtStruk.document().size().height()
        
        new_height = int(doc_height) + 40
        if new_height < 250: new_height = 250
        if new_height > 800: new_height = 800
        
        self.txtStruk.setFixedHeight(int(doc_height) + 20)
        self.dialog.resize(380, new_height + 40)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # DATA TEST
    data_items = [
        {'produk': 'Whiskas Tuna 1.2kg', 'qty': 1, 'harga': 65000, 'subtotal': 65000},
        {'produk': 'Pasir Kucing 10L', 'qty': 1, 'harga': 45000, 'subtotal': 45000},
        {'produk': 'Shampoo Anti Kutu', 'qty': 1, 'harga': 35000, 'subtotal': 35000},
        {'produk': 'Kalung Kucing', 'qty': 2, 'harga': 15000, 'subtotal': 30000},
        {'produk': 'Snack Creamy', 'qty': 5, 'harga': 5000, 'subtotal': 25000}
    ]
    
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.loadData(data_items, 200000, 200000, 0, nama_kasir="Budi Santoso")
    
    MainWindow.show()
    sys.exit(app.exec_())