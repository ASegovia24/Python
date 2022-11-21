from PySide6.QtWidgets import QApplication, QLabel, QDial, QLineEdit, QMainWindow, QPushButton
class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de prueba")
        
        self.dial = QDial(self)
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(print(self.dial.value()))
        self.dial.setFixedSize(100,150)

        self.lbl = QLabel(self)
        self.lbl.setFixedSize(50,30)
        self.lbl.move(70,0)
        
        

        self.dial.valueChanged.connect(self.setvalue)

    def setvalue(self):
        getvalue = self.dial.value()
        self.lbl.setText(str(getvalue))



if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()