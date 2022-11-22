from PySide6.QtWidgets import QApplication, QLabel, QComboBox, QLineEdit, QMainWindow, QPushButton
class Ventana (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de prueba")
        
        self.box = QComboBox(self)
        
        #se le anaden los elementos al combobox
        self.box.addItems(["-elige un mes-","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
        
        self.lbl =  QLabel(self)
        self.lbl.setFixedSize(70,30)
        self.lbl.move(110,0)

        self.lbl2 = QLabel(self)
        self.lbl2.setFixedSize(50,30)
        self.lbl2.move(180,0)
        
        #esta parte se usa para actualizar el texto que 
        # aparece en pantalla al lado del widget
        self.box.currentTextChanged.connect(self.lbl.setText)
        self.box.currentTextChanged.connect(self.setvalue)
        
        #esta parte imprime el mes y el numero en la consola
        self.box.currentTextChanged.connect(self.printvalue)

    #este metodo sirve para sacar el numero del mes
    # y en caso de ser 0, le dice al label del nombre
    # que tambien quede vacio
    def setvalue(self):
        getvalue = self.box.currentIndex()
        if(getvalue != 0):
            self.lbl2.setText(str(getvalue))
        else:
            self.lbl.setText("")
            self.lbl2.setText("")

    #este metodo sirve para extraer del combobox
    # el texto y el indice, y concatenarlos en el print
    # solo en caso de que se haya elegido un mes y no
    # la opcion de -elige un mes-, en cuyo caso no 
    # imprime nada
    def printvalue(self):
        getvalue = str(self.box.currentIndex())
        gettext = str(self.box.currentText())
        if(gettext != "-elige un mes-"):
            print(gettext, "es el mes numero",getvalue)

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()