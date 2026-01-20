import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",user="root",password="1234",db="aditya")
    cur=con.cursor()
    # print(con)

except mysql.connector.DatabaseError as e:
    print("Problem in your Connection : ",e)