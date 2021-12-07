import sqlite3

conn=sqlite3.connect('test.db')

data_employee=conn.execute("select * from employee order by first_name")
data_manager=conn.execute("select * from manager order by  salary DESC")
for i in data_employee:
    print(i)

for i in data_manager:
    print(i)

data_limit=conn.execute("select * from employee limit 2 offset 1")   #### it will show data from offset i.e 1 here to limit i.e 2 here
print("Data will resitrict upto limit")
for i in data_limit:
    print(i)

conn.commit()
conn.close()

