import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from Login import *
from ventana2 import*
import conexion
import time

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.bt_ingresar.clicked.connect(self.iniciar_sesion)
        #base de datos
        self.datos = conexion.Registro_datos()

    def iniciar_sesion(self):
        self.ui.contrasena_incorrecta.setText('')
        self.ui.usuario_incorrecto.setText('')
        users_entry = self.ui.users.text()
        password_entry = self.ui.password.text()

        users_entry= str("'" + users_entry + "'")
        password_entry= str("'" + password_entry + "'")

        dato1 = self.datos.busca_users(users_entry)
        dato2 = self.datos.busca_password(password_entry)

        if dato1 == 0 and dato2 == 0:
            self.ui.contrasena_incorrecta.setText('Contraseña incorrecta')
            self.ui.usuario_incorrecto.setText('Usuario incorrecto')
        else:

            if dato1 == 0:
                self.ui.usuario_incorrecto.setText('Usuario incorrecto')
            else:
                dato1=1

            if dato2 == 0:
                self.ui.contrasena_incorrecta.setText('Contraseña incorrecta')
            else:
                dato2=1


            if dato1 == 1 and dato2 == 1:
                #for i in range(0,10):
                time.sleep(0.02)

                self.hide()
                self.ventana = Ventana_dos()
                self.ventana.show()

class Ventana_dos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana= Ui_VentanaDos()
        self.ventana.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_cafe= MiApp()
    mi_cafe.show()
    sys.exit(app.exec())
