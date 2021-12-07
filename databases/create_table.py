import sqlite3

conn=sqlite3.connect('test.db')

conn.execute('''create table employee(    
             id         integer PRIMARY KEY NOT NULL,
             first_name text NOT NULL,
             last_name text NOT NULL,
             salary integer NOT NULL);''')

conn.execute('''create table manager
        (    id         integer PRIMARY KEY NOT NULL,
             first_name text NOT NULL,
              last_name text NOT NULL,
              salary integer NOT NULL);''')
print("Tables Created Successfully")
conn.commit()
conn.close()

