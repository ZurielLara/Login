
#import myslq.conector

class Registro_datos():

    #def __init__(self):
        #self.conexion = myslq.conector.connect(host='localhost',
        #                                        database='base_datos',
        #                                        user='root',
        #                                        password='admin'
        #                                        )
    
    def busca_users(self, users):
        #cur=self.conexion.cursor()
        #sql = "SELECT * FROM login_datos WHERE Users= {}".format(users)
        #cur.execute(slq)
        #usersx = cur.fetchall()
        #cur.close()
        admin="'Zuriel'"
        if users == admin:
            usersx=1
        else:
            usersx=0 
        return usersx

    def busca_password(self, password):
        #cur=self.conexion.cursor()
        #sql = "SELECT * FROM login_datos WHERE Password= {}".format(password)
        #cur.execute(slq)
        #passwordx = cur.fetchall()
        #cur.close()
        contra="'admin'"
        if password == contra:
            passwordx=1
        else:
            passwordx=0

        return passwordx