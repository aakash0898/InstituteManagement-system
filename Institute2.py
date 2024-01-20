import pickle
import os

data = []

admin_ID = (42100, 43000)
student_ID = (43100, 44000)
employee_ID = (44100, 45000)

def initialize_data_file():
    if os.path.exists("INSTITUTE.dat"):
        with open("INSTITUTE.dat", "rb") as file:
            data.extend(pickle.load(file))

def signup():
    name = input("Enter your name: ")
    designation = input("Enter your designation (admin/student/employee): ")
    password = input("Enter a password: ")
    pc = input("Enter pincode: ")

    if designation == 'admin':
        id_range = admin_ID
    elif designation == 'student':
        id_range = student_ID
    elif designation == 'employee':
        id_range = employee_ID
    else:
        print("Invalid designation, please choose 'admin', 'student', or 'employee'")
        return

    user_id = max(user[0] for user in data if id_range[0] <= user[0] <= id_range[1]) + 1 if data else id_range[0]

    data.append([user_id, name, designation, password, pc])
    save_data()

    print("Signup successful. Your user ID is:", user_id)

def login():
    initialize_data_file()
    user_id = int(input("Enter your user ID: "))
    if user_id < len(data):
        user = data[user_id]
        password = input("Enter your password: ")
        if user[0] == user_id and user[3] == password:
            print("Welcome,", user[1])
            return user_id
        else:
            print("Incorrect password. Login failed.")
    else:
        print("User not found. Please signup first.")
    return None


def save_data():
    with open("INSTITUTE.dat", "wb") as file:
        pickle.dump(data, file)



def admin(user_id):
    if data[user_id][2] == "admin":
        while True:
            print("Admin Options:")
            print("1. Manage Employee Data")
            print("2. Manage Student Data")
            print("3. Update My Information")
            print("4. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                update_admin(user_id)
            elif choice == "4":
                save_data()
                print("Logged out as admin.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("You do not have admin privileges.")

def update_admin(user_id):
    print("Update Admin Information:")

    i = int(input("Press 1 to update Name\n"
                  "Press 2 to update Password\n"
                  "Press 3 to update PinCode\n"
                  "Enter your choice: "))
    if i == 1:
        name = input("Enter your new name: ")
        data[user_id][1] = name
        print("Admin information updated successfully.")



def student(user_id):
    if data[user_id]['designation'] == "student":
        while True:
            print("Student Options:")
            print("1. Display Information")
            print("2. Update Information")
            print("3. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                save_data()
                print("Logged out as student.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("You do not have student privileges.")

def employee(user_id):
    if data[user_id]['designation'] == "employee":
        while True:
            print("Employee Options:")
            print("1. Display Information")
            print("2. Read Student Data")
            print("3. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                save_data()
                print("Logged out as employee.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("You do not have employee privileges.")



while True:
    print("Welcome to the Institute Management System")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        signup()
    
    elif choice == "2":
        user_id = login()
        if user_id is not None:
            user_designation = data[user_id][2]
            if user_designation == "admin":
                admin(user_id)
            elif user_designation == "student":
                student(user_id)
            elif user_designation == "employee":
                employee(user_id)
    
    elif choice == "3":
        save_data()
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
