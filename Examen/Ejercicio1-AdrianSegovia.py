from PySide6.QtWidgets import *
class VentanaPrincipal (QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle ("Calculadora")

        layout_cuadrícula = QGridLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_cuadrícula)
        self.setCentralWidget(componente_principal)
        
        ##
        
        self.label = QLabel("")

        self.uno = QPushButton("1")
        self.dos = QPushButton("2")
        self.tres = QPushButton("3")
        self.cuatro = QPushButton("4")
        self.cinco = QPushButton("5")
        self.seis = QPushButton("6")
        self.siete = QPushButton("7")
        self.ocho = QPushButton("8")
        self.nueve = QPushButton("9")
        self.cero = QPushButton("0")
        self.ce = QPushButton("CE")

        ##
        
        self.uno.clicked.connect(self.clic1)
        self.dos.clicked.connect(self.clic2)
        self.tres.clicked.connect(self.clic3)
        self.cuatro.clicked.connect(self.clic4)
        self.cinco.clicked.connect(self.clic5)
        self.seis.clicked.connect(self.clic6)
        self.siete.clicked.connect(self.clic7)
        self.ocho.clicked.connect(self.clic8)
        self.nueve.clicked.connect(self.clic9)
        self.cero.clicked.connect(self.clic0)
        self.ce.clicked.connect(self.clicce)

        ##

        layout_cuadrícula.addWidget(QPushButton('Historial'), 0, 1, 1, 4)

        layout_cuadrícula.addWidget(self.label, 1, 1, 1, 4)

        layout_cuadrícula.addWidget(self.siete, 2, 1)
        layout_cuadrícula.addWidget(self.ocho, 2, 2)
        layout_cuadrícula.addWidget(self.nueve, 2, 3)
        layout_cuadrícula.addWidget(self.ce, 2, 4)

        layout_cuadrícula.addWidget(self.cuatro, 3, 1)
        layout_cuadrícula.addWidget(self.cinco, 3, 2)
        layout_cuadrícula.addWidget(self.seis, 3, 3)
        layout_cuadrícula.addWidget(QPushButton('/'), 3, 4)

        layout_cuadrícula.addWidget(self.uno, 4, 1)
        layout_cuadrícula.addWidget(self.dos, 4, 2)
        layout_cuadrícula.addWidget(self.tres, 4, 3)
        layout_cuadrícula.addWidget(QPushButton('*'), 4, 4)

        layout_cuadrícula.addWidget(self.cero, 5, 1)
        layout_cuadrícula.addWidget(QPushButton('='), 5, 2)
        layout_cuadrícula.addWidget(QPushButton('-'), 5, 3)
        layout_cuadrícula.addWidget(QPushButton('+'), 5, 4)

        ##

    def clic1(self):
        self.label.setText(self.label.text()+self.uno.text())
    def clic2(self):
        self.label.setText(self.label.text()+self.dos.text())
    def clic3(self):
        self.label.setText(self.label.text()+self.tres.text())
    def clic4(self):
        self.label.setText(self.label.text()+self.cuatro.text())
    def clic5(self):
        self.label.setText(self.label.text()+self.cinco.text())
    def clic6(self):
        self.label.setText(self.label.text()+self.seis.text())
    def clic7(self):
        self.label.setText(self.label.text()+self.siete.text())
    def clic8(self):
        self.label.setText(self.label.text()+self.ocho.text())
    def clic9(self):
        self.label.setText(self.label.text()+self.nueve.text())
    def clic0(self):
        self.label.setText(self.label.text()+self.cero.text())
    def clicce(self):
        self.label.setText("")




app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()
  
