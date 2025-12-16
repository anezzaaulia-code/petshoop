# -*- coding: utf-8 -*-

from models.User import Admin
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                self.main_window = MainWindow
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)

                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")

                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(240, 20, 291, 61))
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.label.setFont(font)
                self.label.setText("Lihat Data User")

                self.label_total = QtWidgets.QLabel(self.centralwidget)
                self.label_total.setGeometry(QtCore.QRect(40, 60, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                self.label_total.setFont(font)
                self.label_total.setText("Total User: 0")

                self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit.setGeometry(QtCore.QRect(40, 100, 350, 51))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.lineEdit.setFont(font)
                self.lineEdit.setStyleSheet("""
                        padding: 6px;
                        background: white;
                        border: 2px solid #ccc;
                        border-radius: 8px;
                        font-size: 14px;
                """)

                self.btn_cari = QtWidgets.QPushButton(self.centralwidget)
                self.btn_cari.setGeometry(QtCore.QRect(400, 100, 90, 51))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.btn_cari.setFont(font)
                self.btn_cari.setText("Cari")
                self.btn_cari.setStyleSheet("""
                QPushButton {
                        background-color: #555555;
                        color: white;
                        border-radius: 8px;
                }
                QPushButton:hover { background-color: #666666; }
                """)

                self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
                self.btn_refresh.setGeometry(QtCore.QRect(500, 100, 100, 51))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.btn_refresh.setFont(font)
                self.btn_refresh.setText("Refresh")
                self.btn_refresh.setStyleSheet("""
                QPushButton {
                        background-color: #6CCF6C;
                        color: white;
                        font-weight: bold;
                        border-radius: 8px;
                }
                QPushButton:hover { background-color: #5BBB5B; }
                """)

                self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
                self.tableWidget.setGeometry(QtCore.QRect(40, 180, 711, 271))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.tableWidget.setFont(font)
                self.tableWidget.setStyleSheet("""
                QTableWidget {
                        background: white;
                        border: 1px solid #aaa;
                        font-size: 14px;
                }
                QHeaderView::section {
                        background-color: #eaeaea;
                        font-weight: bold;
                        padding: 6px;
                        border: 1px solid #aaa;
                }
                """)
                self.tableWidget.horizontalHeader().setStretchLastSection(True)
                self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

                self.btn_back = QtWidgets.QPushButton(self.centralwidget)
                self.btn_back.setGeometry(QtCore.QRect(260, 480, 231, 61))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.btn_back.setFont(font)
                self.btn_back.setText("Back")
                self.btn_back.setStyleSheet("""
                QPushButton {
                        background-color: #555555;
                        color: white;
                        border-radius: 8px;
                }
                QPushButton:hover { background-color: #666666; }
                """)

                MainWindow.setCentralWidget(self.centralwidget)

                # ⬇⬇⬇ FIX PENTING
                self.user_model = Admin()    # <-- BUKAN User()
                # ⬆⬆⬆

                # Load Data Awal
                self.load_data()

                # aksi
                self.btn_cari.clicked.connect(self.search_data)
                self.btn_refresh.clicked.connect(self.refresh_data)
                self.btn_back.clicked.connect(self.back)


        def load_data(self):
                data = self.user_model.select_all()
                self.set_table(data)
                self.label_total.setText(f"Total User: {len(data)}")

        def search_data(self):
                keyword = self.lineEdit.text()
                data = self.user_model.search(keyword)
                self.set_table(data)
                self.label_total.setText(f"Total User: {len(data)}")
                self.lineEdit.clear()

        def refresh_data(self):
                self.lineEdit.clear()
                self.load_data()

        def set_table(self, data):
                self.tableWidget.clearContents()
                self.tableWidget.setColumnCount(4)
                self.tableWidget.setHorizontalHeaderLabels(["Name", "Username", "Password", "Level"])
                self.tableWidget.setRowCount(len(data))

                for i, row in enumerate(data):
                        for j, item in enumerate(row):
                                cell = QtWidgets.QTableWidgetItem(str(item))
                                cell.setTextAlignment(QtCore.Qt.AlignCenter)
                                self.tableWidget.setItem(i, j, cell)
                                
        def back(self):
                from dashboard.dashboard_admin import Ui_MainWindow
                self.dashboard_window = QtWidgets.QMainWindow()
                self.dashboard = Ui_MainWindow()
                self.dashboard.setupUi(self.dashboard_window)
                self.dashboard_window.show()
                self.main_window.close()


# Run Manual
if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(window)
        window.show()
        sys.exit(app.exec_())
