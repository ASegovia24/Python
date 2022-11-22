from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout , QHBoxLayout, QPushButton
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout dentro de otro layout")

        #Creamos los layouts necesarios
        layout_horizontalP = QHBoxLayout()
        layout_vertical = QVBoxLayout()
        layout_horizontal = QHBoxLayout()

        #Creamos un componente principal para la ventana
        componente_principal = QWidget()

        #Le assignamos el layout vertical como disposición
        componente_principal.setLayout(layout_horizontalP)
        self.setCentralWidget(componente_principal)

        #Anadimos los 2 layout dentro del layout principal layout_horizontalP
        layout_horizontalP.addLayout(layout_vertical)
        layout_horizontalP.addLayout(layout_horizontal)

        #Añadimos cuatro botones al layout vertical
        layout_vertical.addWidget(QPushButton('V1'))
        layout_vertical.addWidget(QPushButton('V2'))
        layout_vertical.addWidget(QPushButton('V3'))
        layout_vertical.addWidget(QPushButton('V4'))

        #Añadimos cuatro botones al layout horizontal
        layout_horizontal.addWidget(QPushButton('H1'))
        layout_horizontal.addWidget(QPushButton('H2'))
        layout_horizontal.addWidget(QPushButton('H3'))
        layout_horizontal.addWidget(QPushButton('H4'))


app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()