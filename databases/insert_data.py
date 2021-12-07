import sqlite3

conn=sqlite3.connect('test.db')
print("database connected")

conn.execute("insert into employee (id,first_name,last_name,salary) VALUES (1,'Qasim','Khan',35000)")
conn.execute("insert into employee (id,first_name,last_name,salary) VALUES (2,'Ali','Khan',40000)")
conn.execute("insert into manager (id,first_name,last_name,salary) VALUES (1,'Hassan','ch',45000)")
conn.execute("insert into manager (id,first_name,last_name,salary) VALUES (2,'Awais','Qarni',50000)")
conn.commit()
print("Records updated Successfully")
conn.close()