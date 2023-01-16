from PySide6.QtWidgets import *
class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle ("Cuanto sabes")

        layoutP = QHBoxLayout()
        principal = QWidget()
        principal.setLayout(layoutP)
        self.setCentralWidget(principal)
       

        layoutFormR = QFormLayout()
        register = QWidget()
        register.setLayout(layoutFormR)
        lblusuario = QLabel("Usuario o correo ", self)
        self.usuario = QLineEdit()
        layoutFormR.addRow(lblusuario, self.usuario)
        lblfecha = QLabel("Fecha de nacimiento",self)
        self.date = QDateEdit()
        layoutFormR.addRow(lblfecha, self.date)

        self.botonR = QPushButton("Registar y jugar!!")
        layoutFormR.addRow(self.botonR)
        self.botonR.clicked.connect(self.siguiente1)

#######

        layoutPreg = QGridLayout()
        preg = QWidget()
        preg.setLayout(layoutPreg)
        
        layoutPreg.addWidget(QLabel('Pregunta1: Cual es la capital de Italia?'), 0, 1, 1, 4)
        layoutPreg.addWidget(roma, 1, 1,1,2)
        layoutPreg.addWidget(sevilla, 1, 3,1,2)
        layoutPreg.addWidget(francia, 3, 1,1,2)
        layoutPreg.addWidget(paris, 3, 3,1,2)

        roma = QPushButton("Roma")
        sevilla = QPushButton("Sevilla")
        francia = QPushButton("Francia")
        paris = QPushButton("Paris")

        roma.clicked.connect(self.siguiente2)
    
        layoutPreg2 = QGridLayout()
        preg2 = QWidget()
        preg2.setLayout(layoutPreg2)
        
        layoutPreg2.addWidget(QLabel('Has acertado'), 0, 1, 1, 4)

        self.capa = QStackedLayout()
        self.capa.addWidget(register)
        self.capa.addWidget(preg)
        self.capa.addWidget(preg2)
        
        layoutP.addLayout(self.capa)

    def siguiente1(self):
        self.capa.setCurrentIndex(1)
    def siguiente2(self):
        self.capa.setCurrentIndex(2)

app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()
  
