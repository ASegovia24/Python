import os

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        #abrimos la ventana
        self.setWindowTitle("Editor de texto")
        #le metemos una barra de menu
        barra_menus = self.menuBar()
        #anadimos los menus que va a tener la barra de menus
        menu = barra_menus.addMenu("&Archivo")

        #anado las acciones de Abrir
        ruta_a_icono_abrir = os.path.join(r"C:\Users\admin\Desktop\Python\T2", "open.png")
        accion_abrir = QAction(QIcon(ruta_a_icono_abrir), "&Abrir", self)
        accion_abrir.setShortcut(QKeySequence("Ctrl+o"))
        accion_abrir.triggered.connect(self.abrir)
        menu.addAction(accion_abrir)

        #anado las acciones de Guardar
        ruta_a_icono_guardar = os.path.join(r"C:\Users\admin\Desktop\Python\T2", "save.png")
        accion_guardar = QAction(QIcon(ruta_a_icono_guardar), "&Guardar", self)
        accion_guardar.setShortcut(QKeySequence("Ctrl+s"))
        accion_guardar.triggered.connect(self.guardar)
        menu.addAction(accion_guardar)

        #anado las acciones de Salir
        ruta_a_icono_salir = os.path.join(r"C:\Users\admin\Desktop\Python\T2", "close.png")
        accion_salir = QAction(QIcon(ruta_a_icono_salir), "&Salir", self)
        accion_salir.setShortcut(QKeySequence("Ctrl+q"))
        accion_salir.triggered.connect(self.salir)
        menu.addAction(accion_salir)

        #Meto las acciones en la toolbar
        barra_herramientas = QToolBar("Barra de herramientas")
        barra_herramientas.addAction(accion_abrir)
        barra_herramientas.addAction(accion_guardar)
        barra_herramientas.addAction(accion_salir)
        self.addToolBar(barra_herramientas)
        barra_herramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        #Creo el cuadro editor de texto
        self.dock1 = QDockWidget()
        self.dock1.setWindowTitle("Editar archivo")
        self.dock1.setWidget(QTextEdit(""))
        self.addDockWidget(Qt.TopDockWidgetArea,self.dock1)



    #
    def abrir(self):

        ventana_dialogo = QFileDialog.getOpenFileName(
            self, caption="Abrir archivo para editar...", dir=".",
            filter="Documentos de texto (*.txt);;Documentos PDF (*.pdf)",
            selectedFilter="Documentos de texto (*.txt)")
        file = ventana_dialogo[0]
        print(file)
        text=open(file, 'r').read()        
        self.dock1.widget().setPlainText(text)

    #
    def guardar(self):
        ventana_dialogo=QFileDialog.getSaveFileName(

        self, caption="Guardar archivo...", dir=".",
            filter="Documentos de texto (*.txt);;Documentos PDF (*.pdf)",
            selectedFilter="Documentos de texto (*.txt)")
        
        file = ventana_dialogo[0]
        print(file)
        text = self.dock1.widget().toPlainText()
        open(file, "w").write(text)

    #
    def salir(self):
        QApplication.quit()



if __name__ == "__main__":
    app = QApplication([])
    #app.setAttribute(Qt.AA_DontShowIconsInMenus)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
    