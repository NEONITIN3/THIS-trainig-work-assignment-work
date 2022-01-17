'''only once it created no need to run again otherwise its give error'''
# import sqlite3
# conn=sqlite3.connect('employeeDB.db')
# cur = conn.cursor()
# #creating table in DB
# cur.execute("""Create table sample(first text,last text,pay integer)""")
# conn.commit()

import sqlite3
conn=sqlite3.connect(':memory:') #its create DB in memory
#conn=sqlite3.connect('employeeBD2.db')
'''if u working on memory u dont need to give name of databases its just store'''
cur = conn.cursor()
cur.execute("""Create table sample2(first text,last text,pay integer)""")
conn.commit()

