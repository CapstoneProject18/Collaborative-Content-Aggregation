import sqlite3
import datetime
conn = sqlite3.connect("C:\Users\Tanmay Jain\Desktop\cap/AmazingDatabase.db")
cur = conn.cursor()

def login():
    username = input("Enter user name")
    password = input("Enter password")
    try:
        sql = "select * from logininfo where username = '{}' and password = '{}'".format(username,password)
        cur.execute(sql)
        return True
    except:
        return False

