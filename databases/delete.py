import sqlite3

conn=sqlite3.connect('test.db')

conn.execute("Delete from employee where id=1")
conn.execute("Delete from manager where id=2")
conn.execute("Delete from employee where id=2")
conn.execute("Delete from manager where id=1")
conn.commit()
print("Records deleted successfully")
conn.close()