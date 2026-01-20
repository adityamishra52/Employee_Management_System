import mysql.connector
import createConnection as cs

try:
    cur=cs.cur
    cur.execute("create table employee(eid int primary key,ename varchar(50) not null,email varchar(25) not null unique,department varchar(25) not null,sallery varchar(10) not null)")
    print(cur)

except mysql.connector.DatabaseError as e:
    print("Problem in your attributes Creation: ",e)