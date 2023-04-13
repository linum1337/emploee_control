import mysql.connector


def checkIfExists():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="45.146.40.1",
        user="scanner",
        password="uNmyc1337_!",
    )
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)

def tableCreation():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="45.146.40.1",
        user="scanner",
        password="uNmyc1337_!",
        database="visitors_test"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)
tableCreation()