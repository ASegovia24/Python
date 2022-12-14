from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout , QHBoxLayout, QPushButton
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout dentro de otro layout")

        #Creamos los layouts necesarios
        layout_verticalP = QVBoxLayout()
        layout_horizontal01 = QHBoxLayout()
        layout_horizontal02 = QHBoxLayout()
        layout_vertical1 = QVBoxLayout()

        #Creamos un componente principal para la ventana
        componente_principal = QWidget()

        #Le assignamos el layout vertical como disposición
        componente_principal.setLayout(layout_verticalP)
        self.setCentralWidget(componente_principal)

        #
        self.ledt1 = QLineEdit(self)
        self.ledt2 = QLineEdit(self)
        self.btn1 = QPushButton("Login", self)
        self.lbl = QLabel(self)

        #Anadimos los 2 layout dentro del layout principal layout_horizontalP
        layout_verticalP.addLayout(layout_horizontal01)
        layout_verticalP.addLayout(layout_horizontal02)
        layout_verticalP.addLayout(layout_vertical1)

        layout_horizontal01.addWidget(QLabel('Usuario: '))
        layout_horizontal01.addWidget(self.ledt1)

        layout_horizontal02.addWidget(QLabel('Contrasena: '))
        layout_horizontal02.addWidget(self.ledt2)
        
        layout_vertical1.addWidget(self.btn1)
        layout_vertical1.addWidget(self.lbl)

        self.btn1.clicked.connect(self.clicDeBoton)
    def clicDeBoton(self):
        if(self.ledt1.text() == 'user' and self.ledt2.text() == 'contr' ):
            self.lbl.setStyleSheet("color: green;font: bold 16px;")
            self.lbl.setText("Usuario aceptado")


        else:
            self.lbl.setText("Usuario denegado")
            self.lbl.setStyleSheet("color: red;font: bold 16px;")


        








app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()