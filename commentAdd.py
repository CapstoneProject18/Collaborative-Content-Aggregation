import sqlite3
import datetime
conn = sqlite3.connect("C:\Users\Tanmay Jain\Desktop\cap/AmazingDatabase.db")
cur = conn.cursor()




def CommentAdd(tablename,username):
    comment = input("Enter comment")
    sql = "insert into {} (username,comments,time) values('{}','{}','{}')".format(tablename,username,comment,datetime.datetime.now())
    print(sql)
    cur.execute(sql)

