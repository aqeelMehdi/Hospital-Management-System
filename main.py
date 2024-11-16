from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


class HospitalSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("dash_Board.ui", self)
        
app = QApplication(sys.argv)
window = HospitalSystem()
window.show()
sys.exit(app.exec())
