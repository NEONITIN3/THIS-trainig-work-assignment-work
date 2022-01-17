import sqlite3
conn=sqlite3.connect('EMPDB.db') #creating DB
cur = conn.cursor()
#creating table in DB
# cur.execute("""Create table emp12(first text,last text,pay integer)""")
# conn.commit()
#insert value in Table
cur.execute('insert into emp12 values("Ram","chandra",20090870)')
cur.execute('insert into emp12 values("Ram","chandra",20090870)')
cur.execute('insert into emp12 values("Ram","chandra",20090870)')
cur.execute('insert into emp12 values("Ram","chandra",20090870)')
cur.execute('insert into emp12 values("Ram","chandra",20090870)')
conn.commit()
cur.execute('select *from emp12')
print(cur.fetchall())
conn.commit()
conn.close()