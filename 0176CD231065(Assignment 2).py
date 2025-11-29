students = {}     
logged_user = ''  
logged = False    

def register():
    global students
    print(" Student Registration ")

    username = input("Enter Username-").strip()
    if username in students:
        print(" Username already exists, Try another name.")
        return

    password = input("Enter Password- ").strip()
    name = input("Enter Full Name-")
    roll_no = input("Enter Roll Number- ")
    branch = input("Enter Branch- ")
    year = input("Enter Year of Study- ")
    email = input("Enter Email ID-")
    phone = input("Enter Contact Number- ")
    address = input("Enter Address- ")
    dob = input("Enter Date of Birth (DD-MM-YYYY)- ")
    gender = input("Enter Gender- ")

    
    students[username] = {
        "password": password,
        "name": name,
        "roll_no": roll_no,
        "branch": branch,
        "year": year,
        "email": email,
        "phone": phone,
        "address": address,
        "dob": dob,
        "gender": gender
    }

    print("Registration Successful! You can now login.")


def login():
    global logged, logged_user
    print("Student Login")

    if logged:
        print("You are already logged in as", logged_user)
        return

    username = input("Enter Username- ").strip()
    password = input("Enter Password- ").strip()

    if username in students and students[username]["password"] == password:
        logged = True
        logged_user = username
        print(f"\n Login Successful Welcome, {students[username]['name']}.")
    else:
        print("Invalid Username or Password")


def show_profile():
    global logged, logged_user
    print(" Student Profile ")

    if not logged:
        print("Please login first to view profile.")
        return

    profile = students[logged_user]
    for key, value in profile.items():
        if key != "password":
            print(f"{key.capitalize()}: {value}")


def update_profile():
    global logged, logged_user
    print("Update Profile")

    if not logged:
        print("Please login first to update profile.")
        return

    profile = students[logged_user]
    print("Leave a field blank if you don't want to update it.\n")

    for key in profile:
        if key == "password":
            continue
        new_value = input(f"Update {key.capitalize()} (current: {profile[key]}): ").strip()
        if new_value:
            profile[key] = new_value

    print(" Profile Updated Successfully")


def logout():
    global logged, logged_user
    if not logged:
        print(" No user is currently logged in.")
        return

    print(f"{students[logged_user]['name']} has been logged out successfully.")
    logged = False
    logged_user = ''


def terminate():
    print(" Exiting the LNCT Student System.")
    exit()

def main():
    while True:
        
        print("   Welcome to LNCT Student System")
        
        print("""
        1. Registration
        2. Login
        3. Show Profile
        4. Update Profile
        5. Logout
        6. Main Menu
        7. Exit
        """)

        choice = input("Select option (1/2/3/4/5/6/7):").strip()

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            show_profile()
        elif choice == '4':
            update_profile()
        elif choice == '5':
            logout()
        elif choice == '6':
            print("Returning to Main Menu.")
            continue
        elif choice == '7':
            terminate()
        else:
            print(" Invalid choice! Please select from 1 to 7.")

main()

