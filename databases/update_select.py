import sqlite3

conn=sqlite3.connect('test.db')

conn.execute("Update employee SET salary=50000 where id=1")
conn.execute("Update manager SET first_name='Ahmed', last_name='Hassan' where id=1")

conn.commit()

print("Data Updated Succefully")
print("Total Rows updated", conn.total_changes)

data=conn.execute("select * from employee")
for i in data:
    print(i)

conn.close()