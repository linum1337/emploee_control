import datetime
import sqlite3
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

def search_emploee(name):
    v_list = []
    mydb = mysql.connector.connect(
        host="45.146.40.1",
        user="scanner",
        password="uNmyc1337_!",
        database="visitors_test"
    )
    mycursor = mydb.cursor()
    sqlite_insertion = """SELECT id FROM emploeers WHERE name= %s"""
    insertion_data = ((str(name),))
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
