from PySide6.QtWidgets import QApplication, QWidget, QDial, QLabel, QSlider, QComboBox, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QStackedLayout, QFormLayout, QLineEdit
class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle ("Register")

        layoutP = QHBoxLayout()
        principal = QWidget()
        principal.setLayout(layoutP)
        self.setCentralWidget(principal)


        #REGISTER
        layoutFormR = QFormLayout()
        register = QWidget()
        register.setLayout(layoutFormR)
        #self.setCentralWidget(register)
        usuario = QLabel("Usuario R: ", self)
        clave = QLabel("Contraseña R: ",self)
        self.usuarioQLr = QLineEdit()
        layoutFormR.addRow(usuario, self.usuarioQLr)
        self.passwordr = QLineEdit()
        self.passwordr.setEchoMode(QLineEdit.Password)
        layoutFormR.addRow(clave, self.passwordr)

        self.botonR = QPushButton("Registar")
        layoutFormR.addRow(self.botonR)
        self.botonR.clicked.connect(self.registrar)

        #LOGIN
        layoutForm = QFormLayout()
        login = QWidget()
        login.setLayout(layoutForm)
        #self.setCentralWidget(login)
        usuario = QLabel("Usuario: ", self)
        clave = QLabel("Contraseña: ",self)
        self.usuarioQL = QLineEdit()
        layoutForm.addRow(usuario, self.usuarioQL)
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        layoutForm.addRow(clave, self.password)

        comprobar = 0
        self.botonL = QPushButton("Login")
        layoutForm.addRow(self.botonL)
        self.botonL.clicked.connect(self.comprobar)
        print(comprobar)
    

        self.correcto = QLabel("Usuario Correcto")
        layoutForm.addRow(self.correcto)
        self.correcto.setStyleSheet("Color: Green")
        self.correcto.hide()

        self.incorrecto = QLabel("Usuario Incorrecto")
        layoutForm.addRow(self.incorrecto)
        self.incorrecto.setStyleSheet("Color:Red")
        self.incorrecto.hide()
            

        
        self.capa = QStackedLayout()
        self.capa.addWidget(register)
        self.capa.addWidget(login)
        
        layoutP.addLayout(self.capa)



    def comprobar(self):
        user = "admin"
        password = "admin"

        if self.usuarioQL.text() == self.usuarioQLr.text() and self.password.text() == self.passwordr.text(): 
            
            self.incorrecto.hide()
            self.correcto.show()
            comprobar = 1
            
            
            
        else:
            self.incorrecto.show()
            self.correcto.hide()
            comprobar = 2

    def registrar(self):
        self.capa.setCurrentIndex(1)



  
        
if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()  