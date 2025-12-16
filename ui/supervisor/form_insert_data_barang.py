from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 0, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(18); font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 160, 251, 101))
        self.pushButton.setFont(QtGui.QFont("", 11, QtGui.QFont.Bold))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 160, 251, 101))
        self.pushButton_2.setFont(QtGui.QFont("", 11, QtGui.QFont.Bold))
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect Buttons
        self.pushButton.clicked.connect(self.openFormMakanan)
        self.pushButton_2.clicked.connect(self.openFormAksesoris)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Insert Data Barang"))
        self.label.setText(_translate("MainWindow", "PILIH KATEGORI"))
        self.pushButton.setText(_translate("MainWindow", "Makanan Hewan"))
        self.pushButton_2.setText(_translate("MainWindow", "Aksesoris Hewan"))

    def openFormMakanan(self):
        from ui.supervisor.insert_makanan_hewan import Ui_MainWindow as UiMakanan
        self.window = QtWidgets.QMainWindow()
        self.ui = UiMakanan()
        self.ui.setupUi(self.window)
        self.window.show()
        self.centralwidget.window().hide()
        # Tombol Back di form insert kembali ke dashboard
        self.ui.pushButton_2.clicked.connect(self.backToDashboard)

    def openFormAksesoris(self):
        from ui.supervisor.insert_aksesoris_hewan import Ui_MainWindow as UiAksesoris
        self.window = QtWidgets.QMainWindow()
        self.ui = UiAksesoris()
        self.ui.setupUi(self.window)
        self.window.show()
        self.centralwidget.window().hide()
        self.ui.pushButton_2.clicked.connect(self.backToDashboard)

    def backToDashboard(self):
        from dashboard import dashboard_supervisor as ds
        self.dashboard = QtWidgets.QMainWindow()
        self.ui_dashboard = ds.Ui_MainWindow()
        self.ui_dashboard.setupUi(self.dashboard)
        self.dashboard.show()
        self.window.close()
        
if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())