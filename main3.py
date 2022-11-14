from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton
class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de prueba")
        
        self.ledt = QLineEdit(self)
        self.ledt.setFixedSize(50,30)
        self.ledt.setMaxLength(5)

        self.lbl = QLabel(self)
        self.lbl.setFixedSize(50,30)
        self.lbl.move(0,50)
        
        self.ledt.textChanged.connect(self.lbl.setText)


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()