from PySide6.QtWidgets import QApplication, QLabel, QComboBox, QLineEdit, QMainWindow, QPushButton
class Ventana (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de prueba")
        
        self.box = QComboBox(self)
        
        self.box.addItems(["-elige un mes-","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
        
        self.lbl =  QLabel(self)
        self.lbl.setFixedSize(70,30)
        self.lbl.move(110,0)

        self.lbl2 = QLabel(self)
        self.lbl2.setFixedSize(50,30)
        self.lbl2.move(180,0)

        self.box.currentTextChanged.connect(self.lbl.setText)
        self.box.currentTextChanged.connect(self.setvalue)
        

        self.box.currentTextChanged.connect(self.printvalue)

        
    def setvalue(self):
        getvalue = self.box.currentIndex()
        if(getvalue != 0):
            self.lbl2.setText(str(getvalue))
        else:
            self.lbl.setText("")
            self.lbl2.setText("")

    
    def printvalue(self):
        getvalue = str(self.box.currentIndex())
        gettext = str(self.box.currentText())
        if(gettext != "-elige un mes-"):
            print(gettext, "es el mes numero",getvalue)
#by Adrian Segovia

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()