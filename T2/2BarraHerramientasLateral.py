from PySide6.QtWidgets import *
import os
from PySide6.QtGui import *

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        #abrimos la ventana
        self.setWindowTitle ("Menu")
        #le metemos una barra de menu
        barra_menus = self.menuBar()

        #anadimos los menus que va a tener la barra de menus
        menu = barra_menus.addMenu("&Menu")
        archivo = barra_menus.addMenu("&Archivo")

        #anadimos varias acciones para los menus, una para Menu y 2 para Archivo
        accion = QAction("&Imprimir por consola",self)
        #tras definir la accion se le puede dar un atajo de teclado
        accion.setShortcut(QKeySequence("Ctrl+p"))
        #y despues se le puede dar una accion al clicar sobre el
        accion.triggered.connect(self.imprimir_por_consola)

        #para la accion de guardar vamos a meterle un icono. 
        # para eso guardamos la ruta en una variable
        rutaIconoGuardar = os.path.join(r"C:\Users\admin\Desktop","floppy.png")
        #y al definir la accion guardar le tenemos que dar el icono que queremos
        guardar = QAction(QIcon(rutaIconoGuardar),"Guardar",self)
        guardar.setShortcut(QKeySequence("Ctrl+s"))
        guardar.triggered.connect(self.guardar)

        abrir = QAction("&Abrir",self)
        abrir.setShortcut(QKeySequence("Ctrl+o"))
        abrir.triggered.connect(self.abrir)

        #luego se anade cada accion a su respectivo menu
        menu.addAction(accion)
        archivo.addAction(guardar)
        archivo.addAction(abrir)

#//////////////////////////////////////////////////////////////////////////////////
        #BARRA DE HERRAMIENTAS
        #creamos la barra de herramientas
        barra_herramientas = QToolBar("Barra de herramientas")
        #la barra de herramientas permite anadir acciones igual que los menus
        barra_herramientas.addAction(guardar)
        #y despues se anade a la ventana principal
        self.addToolBar(barra_herramientas)
#/////////////////////////////////////////////////////////////////////////////////
        barra_herramientas2 = QToolBar("Barra de herramientas")
        barra_herramientas2.addAction(guardar)
        barra_herramientas2.addAction(abrir)
        self.addToolBar(barra_herramientas2)


    #se crean 3 metodos, uno por boton que hemos metido
    def imprimir_por_consola(self):
        print("accion 1 menu")
    def guardar(self):
        print("archivo guardado")
    def abrir(self):
        print("archivo abierto")

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()  
    