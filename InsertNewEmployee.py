import mysql.connector
import createConnection as cs
def Insertion(eid,ename,email,department,sallery):

    try:
        cur=cs.cur
        cur.execute("insert into employee values(%s,%s,%s,%s,%s)",(eid,ename,email,department,sallery))
        cs.con.commit()
        print("Employee added successfully! 👍")

        
        

    except mysql.connector.DatabaseError as e:
        print("Problem in your Insertion : ",e)

def getInputForInsertion():
    Condition=True
    while Condition:
        
        try:
            print("="*100)
            print(" \b Enter Employee Details")
            eid=int(input("Enter Employee ID: "))
            ename=input("Enter Employee Name: ")
            email=input("Enter Employee Email: ")
            department=input("Enter Employee Department: ")
            sallery=input("Enter Employee Sallery: ")

            Insertion(eid,ename,email,department,sallery)
            print("="*100)

            print("Would you like to add another Employee : ")
            Condition1=input("YES or NO : \n")
            if Condition1.lower() == "no":
                Condition=False
            print("="*100)

        
        except :
            print("problem in your getting input")

# getInputForInsertion()

