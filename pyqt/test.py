from PyQt5.QtWidgets import *
from PyQt5 import uic

class Stats:
    
    def __init__(self):
        
        self.ui = uic.loadUi('stats.ui')
        self.ui.button1.clicked.connect(self.calc)
        
    def calc(self):
        self.ui.button1.setText('clicked')
        data = self.ui.edit1.toPlainText()
        

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()