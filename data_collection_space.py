from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QFrame
from PyQt6.QtGui import QFont, QTextBlock, QTextLayout
#from PyQt6.QtDesigner
num = 0
num_lookup = 0

class lookup_menu():
    def __init__(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        font = QFont("Nunito", 50) 
        super().__init__()
        self.setWindowTitle("Space data collection")

        titel_start = QTextLayout()
        titel_start.text()
        titel_start.setText("Hello, Welcome to SDC!")


        button_start = QPushButton("start lookup") 
        button_start.pressed.connect(self.close)

        button_close = QPushButton("close")
        button_close.pressed.connect(self.close)

        
        self.setFont(font)
        self.setMenuWidget(button_start)
        self.setMenuWidget(button_close)
        self.show()
        
app = QApplication([])
window = MainWindow()
size = QFrame()
window.setBaseSize(1200, 900) 
window.resize(1200, 900)
app.exec()






    



