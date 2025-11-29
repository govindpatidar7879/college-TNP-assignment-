import os
import random
from datetime import datetime

students = {}
current_user = ""
logged_in = False

def load_data():
    if not os.path.exists("students.txt"):
        return
    with open("students.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")
            if len(data) == 10:
                u, p, n, r, b, y, e, ph, a, d = data
                students[u] = {
                    "password": p, "name": n, "roll_no": r, "branch": b, "year": y,
                    "email": e, "phone": ph, "address": a, "dob": d
                }

def save_data():
    with open("students.txt", "w") as f:
        for u, info in students.items():
            f.write(f"{u}|{info['password']}|{info['name']}|{info['roll_no']}|{info['branch']}|{info['year']}|{info['email']}|{info['phone']}|{info['address']}|{info['dob']}\n")

def register():
    print("\n--- Registration ---")
    user = input("Username: ").strip()
    if user in students:
        print("Already registered, try another username.")
        return
    pwd = input("Password: ").strip()
    name = input("Full name: ")
    roll = input("Roll no: ")
    branch = input("Branch: ")
    year = input("Year: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")
    dob = input("Date of birth: ")

    students[user] = {
        "password": pwd, "name": name, "roll_no": roll, "branch": branch,
        "year": year, "email": email, "phone": phone, "address": address, "dob": dob
    }
    save_data()
    print("Registration done successfully!")

def login():
    global logged_in, current_user
    if logged_in:
        print("Already logged in.")
        return
    print("\n--- Login ---")
    user = input("Username: ").strip()
    pwd = input("Password: ").strip()

    if user == "admin" and pwd == "admin123":
        logged_in = True
        current_user = "admin"
        print("Admin logged in successfully!")
        return

    if user in students and students[user]["password"] == pwd:
        logged_in = True
        current_user = user
        print("Login Successful. Welcome", students[user]["name"])
    else:
        print("Invalid credentials.")

def show_profile():
    if not logged_in or current_user == "admin":
        print("Login first (only for student).")
        return
    data = students[current_user]
    print("\n--- Profile ---")
    for k, v in data.items():
        if k != "password":
            print(k, ":", v)

def update_profile():
    if not logged_in or current_user == "admin":
        print("Login first (only for student).")
        return
    print("\n--- Update Profile ---")
    info = students[current_user]
    for k in info:
        if k == "password":
            continue
        new_val = input(f"{k} ({info[k]}): ").strip()
        if new_val:
            info[k] = new_val
    save_data()
    print("Profile updated!")

def logout():
    global logged_in, current_user
    if not logged_in:
        print("No user logged in.")
        return
    print(current_user, "logged out.")
    logged_in = False
    current_user = ""

# ---------------- QUIZ PART ---------------- #

def load_questions(cat):
    fname = cat.lower() + ".txt"
    if not os.path.exists(fname):
        print("File not found:", fname)
        return []
    qlist = []
    with open(fname, "r") as f:
        for line in f:
            part = line.strip().split("|")
            if len(part) == 6:
                q, a, b, c, d, ans = part
                qlist.append({"q": q, "opt": [a, b, c, d], "ans": ans})
    return qlist

def quiz():
    if not logged_in or current_user == "admin":
        print("Only students can attempt quiz.")
        return

    print("\n--- Quiz Categories ---")
    print("1. DSA\n2. DBMS\n3. PYTHON")
    ch = input("Choose category: ").strip()

    cat = ""
    if ch == "1":
        cat = "DSA"
    elif ch == "2":
        cat = "DBMS"
    elif ch == "3":
        cat = "PYTHON"
    else:
        print("Invalid choice.")
        return

    questions = load_questions(cat)
    if not questions:
        return
    random.shuffle(questions)
    questions = questions[:5]

    score = 0
    for i, q in enumerate(questions, 1):
        print("\nQ", i, ":", q["q"])
        for j, opt in enumerate(q["opt"], 1):
            print(f"{j}. {opt}")
        ans = input("Your answer (1-4): ").strip()
        if ans.isdigit() and 1 <= int(ans) <= 4:
            if q["opt"][int(ans) - 1].lower() == q["ans"].lower():
                score += 1
    print("\nQuiz completed! Your Score:", score, "/", len(questions))

    with open("scores.txt", "a") as f:
        f.write(f"{current_user}|{cat}|{score}/{len(questions)}|{datetime.now()}\n")

def view_scores():
    if not os.path.exists("scores.txt"):
        print("No scores yet.")
        return
    print("\n--- Scores ---")
    with open("scores.txt", "r") as f:
        for line in f:
            u, c, s, d = line.strip().split("|")
            print(u, "|", c, "|", s, "|", d)

# ---------------- MAIN ---------------- #

def main():
    load_data()
    while True:
        print("\n===== STUDENT QUIZ SYSTEM =====")
        print("1.Register")
        print("2.Login")
        print("3.Show Profile")
        print("4.Update Profile")
        print("5.Attempt Quiz")
        print("6.View Scores")
        print("7.Logout")
        print("8.Exit")
        ch = input("Enter choice: ").strip()

        if ch == "1":
            register()
        elif ch == "2":
            login()
        elif ch == "3":
            show_profile()
        elif ch == "4":
            update_profile()
        elif ch == "5":
            quiz()
        elif ch == "6":
            view_scores()
        elif ch == "7":
            logout()
        elif ch == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
