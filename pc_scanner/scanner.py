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
        self.check = QCheckBox()
        self.check.setText("Закрыть смену")
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
        layout.addWidget(self.check)
        self.check.stateChanged.connect(self.stateChange)
        self.status = 0
        self.input.returnPressed.connect(self.get)

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)


    def stateChange(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            self.status = 0
        elif state == Qt.CheckState.Unchecked:
            self.status = 1
    def get(self):
            text = self.input.text()
            inp = scan(text)
            if self.status == 1:
                print(inp)
                model.rec_visit(inp[0], SHOP_ID)
                self.gif.setText("Смена открыта!")
            else:
                print(0)
                model.check_time(inp[0], inp[1])
                self.gif.setText("Смена закрыта!")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
