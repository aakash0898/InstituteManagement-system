import pickle
import os

data = []

ID=42100

def initialize_data_file():
    if os.path.exists("INSTITUTE.dat"):
        with open("INSTITUTE.dat", "rb") as file:
            global data
            data = pickle.load(file)

def signup():
    global ID
    name = input("Enter your name: ")
    designation = input("Enter your designation (Admin/Student/Teacher): ")
    password = input("Enter a password: ")
    pc = input("Enter pincode: ")

    if designation == 'Admin':
        ID += 3
    elif designation == 'Student':
        ID += 7
    elif designation == 'Teacher':
        ID += 9
    else:
        print("Invalid designation, please choose 'Admin', 'Student', or 'Teacher'")
        return
    
    data.append([ID, name, designation, password, pc])
    save_data()

    print("Signup successful. Your user ID is:", ID)


def login():
    initialize_data_file()
    user_id = int(input("Enter your user ID: "))
    for user in data:
        if user[0] == user_id:
            password = input("Enter your password: ")
            if user[3] == password:
                print("Welcome,", user[1])
                user_designation = user[2]
                if user_designation == "Admin":
                    admin(user_id)
                elif user_designation == "Student":
                    student(user_id)
                elif user_designation == "Teacher":
                    teacher(user_id)
                return
            else:
                print("Incorrect password. Login failed.")
                return
    print("User not found. Please signup first.")
    return

def save_data():
    with open("INSTITUTE.dat", "wb") as file:
        pickle.dump(data, file)

def admin(user_id):
    while True:
        print("Admin Options:")
        print("1. Manage Teacher Data")
        print("2. Manage Student Data")
        print("3. Update My Information")
        print("4. Display Admin Information")
        print("5. Logout")
        choice = input("Enter your choice: ")
        #for managing teacher data
        if choice == "1":
            i=input("1. Display data\n"
                    "2. Update Data: ")
            if i== "1":
                for user in data:
                    if user[2] == "Teacher":
                        print("****Teacher Information****")
                        print("User ID:", user[0])
                        print("Name:", user[1])
                        print("Designation:", user[2])
                        print("Pincode:", user[4])
                        print("\n")
            elif i == "2":
                st_id=int(input("Enter Teacher ID for updation: "))
                for user in data:
                    if user[0]==st_id:
                        update_admin(st_id)
        # for managing student data
        elif choice == "2":
            i=input("1. Display data\n"
                    "2. Update Data: ")
            if i== "1":
                for user in data:
                    if user[2] == "Student":
                        print("****Student Information****")
                        print("User ID:", user[0])
                        print("Name:", user[1])
                        print("Designation:", user[2])
                        print("Pincode:", user[4])
                        print("\n")
            elif i == "2":
                st_id=int(input("Enter student ID for updation: "))
                for user in data:
                    if user[0]==st_id:
                        update_admin(st_id)
        elif choice == "3":
            update_admin(user_id)
        elif choice == "4":
            for user in data:
                if user[2]=="Admin":
                    print("****Admin Information****")
                    print("****Student Information****")
                    print("User ID:", user[0])
                    print("Name:", user[1])
                    print("Designation:", user[2])
                    print("Pincode:", user[4])
                    print("\n")
        elif choice == "5":
            save_data()
            print("Logged out as admin.")
            break
        else:
            print("Invalid choice. Please try again.")

def update_admin(user_id):
    print("Update Information:")
    for user in data:
        if user[0] == user_id:
            print(user)
    i = int(input("Press 1 to update Name\n"
                  "Press 2 to update Password\n"
                  "Press 3 to update PinCode\n"
                  "Press 4 to update Designation\n"
                  "Enter your choice: "))
    if i == 1:
        name = input("Enter your new name: ")
        for user in data:
            if user[0] == user_id:
                user[1] = name
                print("****Admin Name updated successfully****")
                print("User ID:", user[0])
                print("Name:", user[1])
                print("Designation:", user[2])
                print("Password:", user[3])
                print("Pincode:", user[4])
                print("\n")
                save_data()
                break
    elif i==2:
        password=input("Enter new password: ")
        for user in data:
            if user[0]==user_id:
                user[3]=password
                print("****Password updated successfully****")
                print("User ID:", user[0])
                print("Name:", user[1])
                print("Designation:", user[2])
                print("Password:", user[3])
                print("Pincode:", user[4])
                print("\n")
                save_data()
                break
    elif i==3:
        pc=input("Enter new PinCode: ")
        for user in data:
            if user[0]==user_id:
                user[3]=pc
                print("****PinCode updated successfully****")
                print("User ID:", user[0])
                print("Name:", user[1])
                print("Designation:", user[2])
                print("Password:", user[3])
                print("Pincode:", user[4])
                print("\n")
                save_data()
                break
    elif i==4:
        des=input("Enter updated Designation: ")
        for user in data:
            if user[0]==user_id:
                user[2]=des
                print("****Designation updated successfully****")
                print("User ID:", user[0])
                print("Name:", user[1])
                print("Designation:", user[2])
                print("Password:", user[3])
                print("Pincode:", user[4])
                print("\n")
                save_data()
                break
    else:
        print("***INVALID CHOICE***")

#**********Student Information************
def student(user_id):
    while True:
        print("Student Options:")
        print("1. Display Information")
        print("2. Update Information")
        print("3. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            i=input("1. Display all student information\n"
                    "2. Display your information: ")
            if i=="1":
                for user in data:
                    if user[2] == "Student":
                        print("User ID:", user[0])
                        print("Name:", user[1])
                        print("Designation:", user[2])
                        print("Pincode:", user[4])
                        print("\n")
            elif i=="2":
                for user in data:
                    if user[0]==user_id:
                        print("****Your Information****")
                        print("User ID:", user[0])
                        print("Name:", user[1])
                        print("Designation:", user[2])
                        print("Pincode:", user[4])
                        print("\n")
            else:
                print("!!!!INVALID CHOICE TRY AGAIN!!!!")
                break
        elif choice == "2":
            update_student(user_id)
        elif choice == "3":
            save_data()
            print("Logged out as student.")
            break
        else:
            print("Invalid choice. Please try again.")



#********Teacher functions***********
def teacher(user_id):
    while True:
        print("Teacher Options:")
        print("1. Manage Your Information")
        print("2. Manage Student Data")
        print("3. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            i=input("1. Display All admin data\n"
                    "2. Disaplay your data\n"
                    "3. Update Data: ")
            if i== "1":
                for user in data:
                    if user[2] == "Teacher":
                        print("****Teacher Information****")
                        print("User ID:", user[0])
                        print("Name:", user[1])
                        print("Designation:", user[2])
                        print("Pincode:", user[4])
                        print("\n")
            elif i == "2":
                for user in data:
                    if user[0]==user_id:
                        print("****Your Information****")
                        print("User ID:", user[0])
                        print("Name:", user[1])
                        print("Designation:", user[2])
                        print("Pincode:", user[4])
                        print("\n")
            elif i == "3":
                st_id=int(input("Enter Teacher ID for updation: "))
                for user in data:
                    if user[0]==st_id:
                        update_admin(st_id)
            else:
                print("!!!!INVALID CHOICE TRY AGAIN!!!!")
                break
        #for managing student information
        elif choice == "2":
            i=input("1. Display data\n"
                    "2. Update Data: ")
            if i== "1":
                for user in data:
                    if user[2] == "Student":
                        print("****Student Information****")
                        print("User ID:", user[0])
                        print("Name:", user[1])
                        print("Designation:", user[2])
                        print("Pincode:", user[4])
                        print("\n")
            elif i == "2":
                st_id=int(input("Enter student ID for updation: "))
                for user in data:
                    if user[0]==st_id:
                        update_admin(st_id)
            else:
                print("!!!!INVALID CHOICE TRY AGAIN!!!!")
                break
        elif choice == "3":
            save_data()
            print("Logged out as teacher.")
            break
        else:
            print("Invalid choice. Please try again.")



#***********Main function**************
while True:
    print("Welcome to the Paradise Institute of technology")
    print("Press 1 to Signup")
    print("Press 2 to Login")
    print("Press 3 to Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        signup()
    
    elif choice == "2":
        login()
    
    elif choice == "3":
        save_data()
        print("Thanks for visiting Paradise institute of technology. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
