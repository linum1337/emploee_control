import datetime

import model
SHOP_ID = '1'
def scan(text):
    try:
        inp_data = text.split('/')
        #model.rec_visit(inp_data[0], inp_data[1])
        print(inp_data)
        return inp_data

    except:
        return False
#scan('17/03/2023/10/11/bill0000139\r')

from PyQt6.QtWidgets import (
    QLineEdit
)
import sys
from PyQt6.QtGui import QPalette, QColor, QMovie
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
QCheckBox,
QPushButton,
QMainWindow
)



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 250)
        self.setWindowTitle(f"ShopID {SHOP_ID}")
        layout = QVBoxLayout()
        self.stacklayout = QStackedLayout()
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addLayout(self.stacklayout)
        self.input = QLineEdit()
        self.gif = QLabel()
        self.check_c = QPushButton()
        self.check_c.setText("Закрыть смену")
        self.check_o = QPushButton()
        self.check_o.setText("Открыть смену")
        self.label = QLabel

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        font = self.input.font()
        font.setPointSize(1)
        #self.input.setFont(font)
        #self.input.setFixedWidth(150)
        self.input.setVisible(True)
        layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.gif)
        layout.addWidget(self.check_c)
        layout.addWidget(self.check_o)
        self.check_c.clicked.connect(self.closeEmp)
        self.check_o.clicked.connect(self.openEmp)

        self.status = 0

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)


    def closeEmp(self):
        self.status = 0
        print(0)
        text = self.input.text()
        inp = scan(text)
        model.check_time(inp[0], inp[1])
        self.gif.setText("Смена закрыта!")
    def openEmp(self):
        self.status = 1
        text = self.input.text()
        inp = scan(text)
        print(inp)
        model.rec_visit(inp[0], SHOP_ID)
        self.gif.setText("Смена открыта!")




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
