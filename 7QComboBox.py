from PySide6.QtWidgets import QApplication, QLabel, QComboBox, QLineEdit, QMainWindow, QPushButton
class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de prueba")
        
        self.box = QComboBox(self)
        
        self.box.addItems(["enero","febrero","marzo"])
        
        self.lbl =  QLabel(self)
        self.lbl.setFixedSize(50,30)
        self.lbl.move(110,0)

        self.lbl2 = QLabel(self)
        self.lbl2.setFixedSize(50,30)
        self.lbl2.move(160,0)

        self.box.currentTextChanged.connect(self.lbl.setText)
        self.box.currentTextChanged.connect(self.setvalue)
    def setvalue(self):
        getvalue = self.box.currentIndex()
        self.lbl2.setText(str(getvalue))


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()