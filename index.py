import createConnection as cs
import InsertNewEmployee as insert
import removeEmployee as remove
import ViewEmployee as view
import UpdateNewEmployee as update
# import Createcolumn as coulmn


print("#"*150)

print("-"*100)
print(" \t\tEmoployee Information System")
print("-"*100)

condition=True
while condition:

    print("\t 1. New Employee")
    print("\t 2. View Employee")
    print("\t 3. View All Employee")
    print("\t 4. Remove Employee")
    print("\t 5. Update Employee Information")
    print("\t 6. Exit")

    print("-"*100)


    choose=input(" \tWhat you want to do: ")
    choose.lower()
    print("-"*100)


    
    match choose:
        case "1" | "new employee":
            insert.getInputForInsertion()
            

        case "2" | "view employee":
            view.getInputforviewrecord()

        case "3" | "view all employee":
            view.viewAllEmployee()

        case "4" | "remove employee":
            remove.getInputforremoveEmployee()

        case "5" | "update employee information":
            update.getinputforupdateemployee()

        case "6" | "exit":
            print("\t\tThankyou for choose Our Application ")
            break
        case _:
            print("\t\t You type something wrong please try again")

    print("#"*150)

    print("Again You Want to use this application")
    condition1=input("Yes or No: ")
    condition1.islower
    if condition1=="no":
        print("\t\tThankyou for choosing Our Application ")
        condition=False
    print("#"*150)





print("#"*150)

