from PySide6.QtWidgets import *
import os
from PySide6.QtGui import *

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        #abrimos la ventana
        self.setWindowTitle ("untitled.png - Paint")
        #le metemos una barra de menu
        barra_menus = self.menuBar()
        

        #anadimos los menus que va a tener la barra de menus
        file = barra_menus.addMenu("&File")
        edit = barra_menus.addMenu("&Edit")
        view = barra_menus.addMenu("&View")
        image = barra_menus.addMenu("&Image")
        colors = barra_menus.addMenu("&Colors")
        help = barra_menus.addMenu("&Help")

        herramientas = QToolBar("Drawing Tools")
        color = QToolBar("Select Color")

        #anado las acciones de File
        new = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\icons","1.png")),"New",self)
        new.setShortcut(QKeySequence("Ctrl+n"))
        new.triggered.connect(self.new)

        open = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\icons","2.png")),"Open...",self)
        open.setShortcut(QKeySequence("Ctrl+o"))
        open.triggered.connect(self.open)

        #menu de abrir los dibujos recientemente abiertos
        openrecent = QMenu("&Open Recent",self)

        a = QAction("&dibujo1.png",self)
        b = QAction("&asdfg.png",self)
        c = QAction("&FotoDeGato.png",self)

        openrecent.addAction(a)
        openrecent.addAction(b)
        openrecent.addAction(c)
        #

        save = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\icons","3.png")),"Save",self)
        save.setShortcut(QKeySequence("Ctrl+s"))
        save.triggered.connect(self.save)

        saveas = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\icons","4.png")),"Save As...",self)
        saveas.setShortcut(QKeySequence("Ctrl+Shift+s"))
        saveas.triggered.connect(self.save)

        print = QAction("&Print...",self)
        print.setShortcut(QKeySequence("Ctrl+p"))
        print.triggered.connect(self.save)

        exit = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\icons","8.png")),"Exit",self)
        exit.setShortcut(QKeySequence("Alt+f4"))
        exit.triggered.connect(self.exit)

        #acciones de edit
        undo = QAction("&Undo",self)
        undo.setShortcut(QKeySequence("Ctrl+z"))
        
        redo = QAction("&Redo",self)
        redo.setShortcut(QKeySequence("Ctrl+y"))

        copy = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\icons","5.png")),"Copy",self)
        copy.setShortcut(QKeySequence("Ctrl+c"))

        cut = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\icons","6.png")),"Cut",self)
        cut.setShortcut(QKeySequence("Ctrl+x"))

        paste = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\icons","7.png")),"Paste",self)
        paste.setShortcut(QKeySequence("Ctrl+v"))

        select = QAction("&Select All",self)
        select.setShortcut(QKeySequence("Ctrl+a"))

        #acciones de la barra de herramientas
        fselect = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","1.png")),"Free Selection",self)

        rselect = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","2.png")),"Rectangle Selection",self)

        erase = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","3.png")),"Erase",self)

        fill = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","4.png")),"Filling Bucket",self)

        picker = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","5.png")),"Color Picker",self)

        zoom = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","6.png")),"Magnifying Glass",self)

        pen = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","7.png")),"Pen",self)
        
        pbrush = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","8.png")),"Paintbrush",self)

        abrush = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","9.png")),"Airbrush",self)

        text = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","10.png")),"Insert Text",self)

        line = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","11.png")),"Straight Line",self)

        curve = QAction(QIcon(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","12.png")),"Curve Line",self)

        #acciones de color,
        label = QLabel(self)
        pixmap = QPixmap(os.path.join(r"C:\Users\admin\Desktop\python\T2\painticons","color.png"))
        label.setPixmap(pixmap)
        color.addWidget(label)

        #luego se anade cada accion a su respectivo menu
        file.addAction(new)
        file.addAction(open)
        file.addMenu(openrecent)
        file.addAction(save)
        file.addAction(saveas)
        file.addSeparator()
        file.addAction(print)
        file.addSeparator()
        file.addAction(exit)

        edit.addAction(undo)
        edit.addAction(redo)
        edit.addSeparator()
        edit.addAction(copy)
        edit.addAction(cut)
        edit.addAction(paste)
        edit.addSeparator()
        edit.addAction(select)
        
        herramientas.addAction(fselect)
        herramientas.addAction(rselect)
        herramientas.addAction(erase)
        herramientas.addAction(fill)
        herramientas.addAction(picker)
        herramientas.addAction(zoom)
        herramientas.addAction(pen)
        herramientas.addAction(pbrush)
        herramientas.addAction(abrush)
        herramientas.addAction(text)
        herramientas.addAction(line)
        herramientas.addAction(curve)

        herramientas.setMovable(False)
        
        color.setMovable(False)




        #se anaden las barras a la ventana principal
        self.addToolBar(Qt.LeftToolBarArea,herramientas)
        self.addToolBar(Qt.BottomToolBarArea,color)

    #se crean los metodos, uno por boton que hemos metido
    def new(self):
        print("New file created")
    def save(self):
        print("File saved")
    def open(self):
        print("File opened")
    def exit(self):
        quit()

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.setMinimumHeight(500)
    ventana.setMinimumWidth(800)
    ventana.show()
    
    app.exec()  
    