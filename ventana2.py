# Form implementation generated from reading ui file 'ventanados.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VentanaDos(object):
    def setupUi(self, VentanaDos):
        VentanaDos.setObjectName("VentanaDos")
        VentanaDos.resize(782, 600)
        self.centralwidget = QtWidgets.QWidget(VentanaDos)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-30, 0, 811, 591))
        self.frame.setAutoFillBackground(True)
        self.frame.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0852273 rgba(75, 228, 222, 255), stop:1 rgba(108, 61, 194, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 130, 671, 291))
        font = QtGui.QFont()
        font.setFamily("SWRomnt")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(0, 0, 0, 0%);\n"
";\n"
"font: 72pt \"SWRomnt\";")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        VentanaDos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaDos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
        self.menubar.setObjectName("menubar")
        VentanaDos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaDos)
        self.statusbar.setObjectName("statusbar")
        VentanaDos.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaDos)
        QtCore.QMetaObject.connectSlotsByName(VentanaDos)

    def retranslateUi(self, VentanaDos):
        _translate = QtCore.QCoreApplication.translate
        VentanaDos.setWindowTitle(_translate("VentanaDos", "MainWindow"))
        self.label.setText(_translate("VentanaDos", "Bienvenido"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaDos = QtWidgets.QMainWindow()
    ui = Ui_VentanaDos()
    ui.setupUi(VentanaDos)
    VentanaDos.show()
    sys.exit(app.exec())