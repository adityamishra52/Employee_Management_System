import mysql.connector
import createConnection as cs

def removeEmployee(eid):
        try:
            cur=cs.cur
            cur.execute("SELECT * FROM employee WHERE eid=%s",(eid,))
            if cur.fetchone():        
                cur.execute("delete from employee where eid=%s",(eid,))
                cs.con.commit()
                print("Employee Deleted......")
            else:
                print("Employee not present in Database....")
            
            

        except mysql.connector.DatabaseError as e:
            print("Problem in your Deletion Time: ",e)



def getInputforremoveEmployee():
    Condition=True
    while Condition:
        print("You are on deletion page")
        try:
            print("="*100)
            print(" \b Enter Employee Details")
            eid=input("Enter Employee ID you want to delete: ")
            

            removeEmployee(eid)
            print("="*100)

            print("Would you like to remove another Employee : ")
            Condition1=input("YES or NO : \t")
            if Condition1.lower() == "no":
                Condition=False

        
        except :
            print("problem in your getting input")


