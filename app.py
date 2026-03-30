import json

# Tupla
fields = ("id", "name", "age", "course", "status")

students = []

# -------- FUNCTIONS --------

def add_student():
    try:
        student_id = input("ID: ")

        for s in students:
            if s["id"] == student_id:
                print("ID exists")
                return

        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")
        status = input("Status (active/inactive): ")

        if status != "active" and status != "inactive":
            print("Invalid status")
            return

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "status": status
        }

        students.append(student)
        print("Added")

    except:
        print("Error")

def view_students():
    if len(students) == 0:
        print("No students")
        return

    for s in students:
        print(s)

def search_student():
    x = input("Search ID or name: ")

    for s in students:
        if s["id"] == x or s["name"] == x:
            print(s)
            return

    print("Not found")

def update_student():
    student_id = input("ID to update: ")

    for s in students:
        if s["id"] == student_id:
            try:
                s["name"] = input("New name: ")
                s["age"] = int(input("New age: "))
                s["course"] = input("New course: ")
                s["status"] = input("New status: ")
                print("Updated")
                return
            except:
                print("Error")
                return

    print("Not found")

def delete_student():
    student_id = input("ID to delete: ")

    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            print("Deleted")
            return

    print("Not found")

# -------- FILE --------

def save_data():
    file = open("students.json", "w")
    json.dump(students, file)
    file.close()
    print("Saved")

def load_data():
    global students
    try:
        file = open("students.json", "r")
        students = json.load(file)
        file.close()
        print("Loaded")
    except:
        print("No file")

# -------- MENU --------

def menu():
    load_data()
    running = True

    while running:
        print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Save 7.Exit")
        op = input("Option: ")

        if op == "1":
            add_student()
        elif op == "2":
            view_students()
        elif op == "3":
            search_student()
        elif op == "4":
            update_student()
        elif op == "5":
            delete_student()
        elif op == "6":
            save_data()
        elif op == "7":
            save_data()
            print("Bye")
            running = False
        else:
            print("Invalid")

# -------- RUN --------

menu()