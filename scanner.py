import datetime

import mysql.connector

bd_location = '/Users/vladislavcehov/PycharmProjects/qr_time/visitors.db'

def user_add(id, cookie, login):
    mydb = mysql.connector.connect(
        host="45.146.40.1",
        user="scanner",
        password="uNmyc1337_!",
        database="visitors_test"
    )
    mycursor = mydb.cursor()
    sqlite_insertion = """INSERT INTO emploeers (name, role, phone) VALUES (%s, %s, %s)"""
    insertion_data = (str(id), str(cookie), str(login))
    mycursor.execute(sqlite_insertion, insertion_data)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
def point_add(address):
    mydb = mysql.connector.connect(
        host="45.146.40.1",
        user="scanner",
        password="uNmyc1337_!",
        database="visitors_test"
    )
    mycursor = mydb.cursor()
    sqlite_insertion = """INSERT INTO points (adress) VALUES (%s)"""
    insertion_data = (str(address),)
    mycursor.execute(sqlite_insertion, insertion_data)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def visit_search(id):
    v_list = []
    mydb = mysql.connector.connect(
        host="45.146.40.1",
        user="scanner",
        password="uNmyc1337_!",
        database="visitors_test"
    )
    mycursor = mydb.cursor()
    sqlite_insertion = """SELECT id, vtime, pointID FROM visits WHERE id= %s"""
    insertion_data = ((str(id),))
    mycursor.execute(sqlite_insertion, insertion_data)
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
        v_list.append(i)
    return v_list


def rec_visit(id, point_id):
    mydb = mysql.connector.connect(
        host="45.146.40.1",
        user="scanner",
        password="uNmyc1337_!",
        database="visitors_test"
    )
    mycursor = mydb.cursor()
    print(id, point_id)
    sqlite_insertion = """INSERT INTO visits (id, vtime, pointID) VALUES (%s, %s, %s)"""
    curtime = datetime.datetime.now()
    insertion_data = (str(id), str(curtime), point_id)
    mycursor.execute(sqlite_insertion, insertion_data)
    mydb.commit()
def check_time(id, name):
    cur_visit = visit_search(id)[-1]
    print(cur_visit)
    pointID = cur_visit[2]
    vistime = datetime.datetime.strptime(cur_visit[1], "%Y-%m-%d %H:%M:%S.%f")
    cur_time = datetime.datetime.now()
    delta = cur_time - vistime
    spmins = int(delta.total_seconds()//60)
    mydb = mysql.connector.connect(
        host="45.146.40.1",
        user="scanner",
        password="uNmyc1337_!",
        database="visitors_test"
    )
    mycursor = mydb.cursor()
    sqlite_insertion = """INSERT INTO all_visitings (empID, pointID, minutes) VALUES (%s, %s, %s)"""
    curtime = datetime.datetime.now()
    insertion_data = ((str(id), str(pointID), str(spmins)))
    mycursor.execute(sqlite_insertion, insertion_data)
    mydb.commit()


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
        check_time(inp[0], inp[1])
        self.gif.setText("Смена закрыта!")
    def openEmp(self):
        self.status = 1
        text = self.input.text()
        inp = scan(text)
        print(inp)
        rec_visit(inp[0], SHOP_ID)
        self.gif.setText("Смена открыта!")




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
