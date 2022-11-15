from datetime import datetime

from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QLabel, QLineEdit,
                               QMainWindow, QPushButton)


class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de prueba")
        
        self.ledt = QDateTimeEdit(self,calendarPopup=True)
        self.ledt.setFixedSize(110,30)
        #self.ledt.setMaxLength(5)

        self.lbl = QLabel(self)
        self.lbl.setFixedSize(110,30)
        self.lbl.move(115,0)

        self.ledt.dateTimeChanged.connect(self.time)
    def time(self):
        time = self.ledt.dateTime()
        self.lbl.setText(time.toString("dd-MM-yyyy HH:mm"))




if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()