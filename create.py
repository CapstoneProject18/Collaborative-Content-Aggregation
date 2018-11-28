import sqlite3
import datetime
conn = sqlite3.connect("C:\Users\Tanmay Jain\Desktop\cap/AmazingDatabase.db")
cur = conn.cursor()


# In[15]:


def create():
    tablename = input()
    try:
        cur.execute("""CREATE TABLE {} (Cid integer PRIMARY KEY,username TEXT,userid INT,time datetime,comments TEXT)""".format(tablename))
    except:
        pass

