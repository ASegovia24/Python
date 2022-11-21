from PySide6.QtWidgets import QApplication, QLabel, QSlider, QLineEdit, QMainWindow, QPushButton
class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de prueba")
        
        self.slider = QSlider(self)
        
        #self.slider.valueChanged.connect(print(self.dial.value()))
        self.slider.setFixedSize(100,150)

        self.lbl = QLabel(self)
        self.lbl.setFixedSize(50,30)
        self.lbl.move(70,0)
        
        

        self.slider.valueChanged.connect(self.setvalue)

    def setvalue(self):
        getvalue = self.slider.value()
        self.lbl.setText(str(getvalue))



if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()