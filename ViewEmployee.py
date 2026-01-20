import mysql.connector
import createConnection as cs

def viewAllEmployee():
    try:
        cur=cs.cur
        cur.execute("SELECT * FROM employee")
        target=cur.fetchall()
        if target:
            # getting cols name
            print("-"*100)
            for col in cur.description:
                print(col[0],end="\t\t")
            print()
            print("-"*100)
            # getting values/records
            for record in target:
                for val in record:
                    print(val,end="\t\t")
                print("\n")
            print("-"*100)
        

    except mysql.connector.DatabaseError as e:
        print("Problem in Your All showing db: ",e)

def viewEmployee(eid):
    try:
        cur=cs.cur
        cur.execute("SELECT * FROM employee WHERE eid=%s",(eid,))
        target=cur.fetchone()
        if target:
            print("-"*40)
            for col in cur.description:
                print("{}".format(col[0]),end="\t \t")
            print()
            print("-"*40)
            # getting the records
        
            for record in target:
                
                print("{}".format(record),end="\t \t")
            print()
            print("-"*40)
        else:
            print("User not found....")

    except mysql.connector.DatabaseError as e:
        print("Problem in your View Database: ",e)

def getInputforviewrecord():
    Condition=True
    while Condition:
    
        print("You are on View page")
        try:
            print("="*100)
            print(" \b Enter Employee Details")
            eid=input("Enter Employee ID you want to View: ")
            

            viewEmployee(eid)
            print("="*100)

            print("Would you like to view another Employee : ")
            Condition1=input("YES or NO : \n")
            if Condition1.lower() == "no":
                Condition=False

        
        except :
            print("problem in your getting input")

# getInput()
# viewAllEmployee()