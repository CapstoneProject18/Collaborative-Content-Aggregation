
#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
import datetime
conn = sqlite3.connect("C:\Users\Tanmay Jain\Desktop\cap/AmazingDatabase.db")
cur = conn.cursor()


def exploreTopics():
    username = input("Enter user name")
    
    try:
        sql = "select * from topiclist where username != '{}'".format(username,password)
        cur.execute(sql)
        return True
    except:
        return False
