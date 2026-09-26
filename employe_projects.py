
# Employee Management System (CRUD)
# A simple command-line tool to Add, List, Search, Update and Delete
# employee records stored in a JSON file.

import json
import os
from random import randint

DATA_FILE = "employee.json"

# FILE HELPERS

def load_employees():
    """Load the employee list from disk. Returns [] if the file is missing/empty/corrupt."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        print("WARNING: employee.json was empty or corrupted. Starting fresh.")
        return []


def save_employees(employees):
    """Write the employee list back to disk."""
    with open(DATA_FILE, "w") as f:
        json.dump(employees, f, indent=4)


def generate_unique_id(employees):
    """Generate a random ID that doesn't collide with an existing employee."""
    existing_ids = {emp["ID"] for emp in employees}
    while True:
        new_id = randint(500, 1000)
        if new_id not in existing_ids:
            return new_id



# SMALL INPUT-HELPERS


def input_nonempty(prompt):
    """Keep asking until the user types something other than blank/whitespace."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field can't be empty. Try again.")


def input_int(prompt):
    """Keep asking until the user types a valid integer. Returns None if they type 'q' to cancel."""
    while True:
        raw = input(prompt).strip()
        if raw.lower() == "q":
            return None
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid number (or 'q' to cancel).")


def input_yes_no(prompt):
    """Keep asking until the user answers y or n. Returns True for y, False for n."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please enter 'y' or 'n'.")


def find_employee_index(employees, emp_id):
    """Return the index of the employee with this ID, or None if not found."""
    for i, emp in enumerate(employees):
        if emp["ID"] == emp_id:
            return i
    return None


# CRUD OPERATIONS


def add_employee():
    print("=" * 42)
    print("\tADD EMPLOYEE SECTION")
    print("=" * 42)

    employees = load_employees()

    name = input_nonempty("ENTER EMPLOYEE NAME: ")
    department = input_nonempty("ENTER EMPLOYEE DEPARTMENT: ").upper()
    employee_id = generate_unique_id(employees)

    employees.append({
        "ID": employee_id,
        "name": name,
        "department": department
    })
    save_employees(employees)

    print(f"EMPLOYEE ADDED SUCCESSFULLY!\nEmployee ID Generated: {employee_id}\n")


def list_employees():
    employees = load_employees()

    print("=" * 38)
    print("     THE LIST OF EMPLOYEES")
    print("=" * 38)

    if not employees:
        print("No employees found.")
    else:
        for employee in employees:
            print(json.dumps(employee, indent=4))
    print()


def search_employee():
    employees = load_employees()

    search_id = input_int("ENTER EMPLOYEE ID TO SEARCH (or 'q' to cancel): ")
    if search_id is None:
        return

    index = find_employee_index(employees, search_id)
    if index is not None:
        print(json.dumps(employees[index], indent=4))
    else:
        print("EMPLOYEE NOT FOUND")


def delete_employee():
    print("=" * 42)
    print("\tDELETE EMPLOYEE SECTION")
    print("=" * 42)

    employees = load_employees()

    delete_id = input_int("ENTER EMPLOYEE ID TO DELETE (or 'q' to cancel): ")
    if delete_id is None:
        return

    index = find_employee_index(employees, delete_id)
    if index is None:
        print("EMPLOYEE NOT FOUND")
        return

    employee = employees[index]
    confirmed = input_yes_no(
        f"IF YOU WANT TO DELETE THIS EMPLOYEE TYPE 'y/n'!\n"
        f"{json.dumps(employee, indent=4)}\n"
    )

    if not confirmed:
        print("OK, EMPLOYEE NOT DELETED")
        return

    del employees[index]
    save_employees(employees)
    print("EMPLOYEE DELETED SUCCESSFULLY!")


def update_employee():
    print("=" * 42)
    print("\tUPDATE EMPLOYEE SECTION")
    print("=" * 42)

    employees = load_employees()

    emp_id = input_int("ENTER EMPLOYEE ID TO UPDATE (or 'q' to cancel): ")
    if emp_id is None:
        return

    index = find_employee_index(employees, emp_id)
    if index is None:
        print("EMPLOYEE NOT FOUND")
        return

    employee = employees[index]
    print(f"EMPLOYEE FOUND!\n{json.dumps(employee, indent=4)}\n")
    print("1. Update Name")
    print("2. Update Department")
    update_choice = input("What do you want to update? ").strip()

    if update_choice == "1":
        employee["name"] = input_nonempty("NEW NAME: ")
        print("Employee name updated!")
    elif update_choice == "2":
        employee["department"] = input_nonempty("NEW DEPARTMENT: ").upper()
        print("Employee department updated!")
    else:
        print("Invalid choice. No changes made.")
        return

    save_employees(employees)

# MENU / MAIN LOOP
MENU_ACTIONS = {
    "1": add_employee,
    "2": list_employees,
    "3": search_employee,
    "4": delete_employee,
    "5": update_employee,
}


def print_menu():
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


def main():
    while True:
        print_menu()
        choice = input("ENTER YOUR CHOICE: ").strip()

        if choice == "6":
            print("BYE!")
            break

        action = MENU_ACTIONS.get(choice)
        if action is None:
            print("Invalid choice. Please enter a number from 1-6.\n")
            continue

        action()
        print()  # spacing before the menu reprints


if __name__ == "__main__":
    main()



























































