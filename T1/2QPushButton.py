from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QWidget, QMainWindow 
class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de prueba")
        self.btn1 = QPushButton("Haz clic aqui", self)
        self.setCentralWidget(self.btn1)
        self.btn1.clicked.connect(self.clicDeBoton)
    def clicDeBoton(self):
        print("Senal de clic recibida")
if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()
