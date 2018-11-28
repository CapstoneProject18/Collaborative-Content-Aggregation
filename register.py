import sqlite3
import datetime
conn = sqlite3.connect("C:\Users\Tanmay Jain\Desktop\cap/AmazingDatabase.db")
cur = conn.cursor()


def register():
    username = input("Enter user name")
    password = input("Enter password")
    sql = "INSERT INTO logininfo values('{}','{}')".format(username,password)
    #print(sql)
    cur.execute(sql)

