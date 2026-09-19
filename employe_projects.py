import json
from random import randint

while True:
    print("\t        MAIN MENU")
    print("=" * 42)
    print("\tEMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 42)
    print("1. ADD EMPLOYEE")
    print("2. LIST EMPLOYEES")
    print("3. SEARCH EMPLOYEE")
    print("4. DELETE EMPLOYEE")
    print("5. UPDATE EMPLOYEE")
    print("6. EXIT")

    choice = input("ENTER YOUR CHOICE: ")

    # FOR EXIT
    if choice == "6":
        print("BYE!")
        break

    # ADD EMPLOYEE
    if choice == "1":
        print("=" * 42)
        print("\tADD EMPLOYEE SECTION")
        print("=" * 42)

        employee_id = randint(500, 1000)
        name = input("ENTER EMPLOYEE NAME: ")
        department = input("ENTER EMPLOYEE DEPARTMENT: ")

        new_employee = {
            "ID": employee_id,
            "name": name,
            "department": department
        }

        with open("employee.json", "r") as f:
            list_of_employee = json.load(f)

        list_of_employee.append(new_employee)

        with open("employee.json", "w") as f:
            json.dump(list_of_employee, f, indent=4)

        print(f"EMPLOYEE ADDED SUCCESSFULLY! \nEmploye ID Generated : {employee_id}\n")
        back_control = input("YOU WANT TO GO MAIN MENU y/n?\n")
        if back_control == "y":
            continue
        else:
            break

    # LIST EMPLOYEES
    elif choice == "2":
        with open("employee.json", "r") as f:
            list_of_employee = json.load(f)

        print("="*38)
        print("     THE LIST OF EMPLOYE")
        print("="*38)

        for employee in list_of_employee:
            print(json.dumps(employee, indent=4))

        print(" ")

        back_control = input("YOU WANT TO GO MAIN MENU y/n?\n")
        if back_control == "y":
            continue
        else:
            break
        
    # SEARCH EMPLOYEE
    elif choice == "3":
        try:
            search_id = int(input("ENTER EMPLOYEE ID TO SEARCH:\n> "))
        except ValueError:
            print("Please enter valid number!")
            continue
            


        with open("employee.json", "r") as f:
            list_of_employee = json.load(f)

        for employee in list_of_employee:
            if employee["ID"] == search_id:
                print(json.dumps(employee, indent=4))
                break
        else:
            print("EMPLOYEE NOT FOUND")
        back_control = input("YOU WANT TO GO MAIN MENU y/n?\n")
        if back_control == "y":
            continue
        else:
            break


    # DELETE EMPLOYEE
    elif choice == "4":
        print("=" * 42)
        print("\tDELETE EMPLOYEE SECTION")
        print("=" * 42)

        delete_employee = int(input("ENTER EMPLOYEE ID TO DELETE: "))

        with open("employee.json", "r") as f:
            list_of_employee = json.load(f)

        for employee in list_of_employee:
            if employee["ID"] == delete_employee:
                confirmation = input(
                    f"IF YOU WANT TO DELETE THIS EMPLOYEE TYPE 'y/n'!\n"
                    f"{json.dumps(employee, indent=4)}\n"
                ).lower()

                if confirmation == "n":
                    print("OK, EMPLOYEE NOT DELETED")
                    break
                elif confirmation == "y":
                    list_of_employee = [
                        emp for emp in list_of_employee
                        if emp["ID"] != delete_employee
                    ]

                    with open("employee.json", "w") as f:
                        json.dump(list_of_employee, f, indent=4)

                    print("EMPLOYEE DELETED SUCCESSFULLY!")
                    back_control = input("YOU WANT TO GO MAIN MENU y/n?\n")
                    if back_control == "y":
                        continue
                    else:
                        break
                else:
                    print("PLEASE ENTER ONLY y OR n")
                break
        else:
            print("EMPLOYEE NOT FOUND")

    # UPDATE EMPLOYEE
    elif choice == "5":  

        print("UPDATE EMPLOYEE - NEXT STEP")
        with open("employee.json", "r") as f:
            list_of_employee = json.load(f)
        
        enter_id = int(input("Enter ID of Employe: \n>"))

        found = False

        for employee in list_of_employee:
            if employee["ID"] == enter_id:
                found = True
                print(f"Employe Founded!\n{json.dumps(employee, indent=4)} ")
                print(" ")
                print("1. Update Name")
                print("2. Update Department")
                update_choice = input("What do you want to update?\n>")
            
            if update_choice == "1":
                new_name = input("*Enter Name: ")
                employee["name"] = new_name
                print(f"Employe Name Updated!")

            elif update_choice == "2":
                new_departement = input("Enter new department:\n>").upper()
                employee["department"] = new_departement
                print(f"Employe department Updated!")
            
            with open("employee.json", "w") as f:
                json.dump(list_of_employee, f, indent=4)
            
            break

    if not found:
        print("Employee ID not found.")

