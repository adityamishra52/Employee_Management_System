import mysql.connector
import createConnection as cs

def updateemployee(eid,ename,department,sallery):
    try:
        cur=cs.cur
        cur.execute("update employee SET ename=%s,department=%s,sallery=%s WHERE eid=%s",(ename,department,sallery,eid))
        cs.con.commit()
        
        if cur.rowcount>0 :
            print("suceesfull updated..")
        else:
            print("something went wrong,Please Check Your Employee id")

    except mysql.connector.DatabaseError as e:
        print("Problem in your update databse: ",e)



def getinputforupdateemployee():
    

    condition=True
    while condition:
        try:
            print("-"*100)
            print("\tYou are in Update page")
            print("-"*100)
            eid=int(input("Enter Employee id Which you want to update: "))
            ename=input("What would you like to set Name: ")
            department=input("What would you like to set Department: ")
            sallery=input("What would you like to set Sallery: ")
            print("-"*100)
            updateemployee(eid,ename,department,sallery)
            print("-"*100)
            condition1=input("would you like to Update More Employee (Yes/No): ")
            condition1.lower()
            if condition1=="no":
                condition = False
    
        except:
            print("problem in your getting data for updation")

# getinputforupdateemployee()

