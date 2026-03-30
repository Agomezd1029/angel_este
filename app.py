import json

students = []

# ---------------- FUNCTIONS ----------------

def add_student():
    try:
        student_id = input("Enter ID: ")
        
        # Check if ID already exists
        for s in students:
            if s["id"] == student_id:
                print("ID already exists.")
                return
        
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        status = input("Enter status (active/inactive): ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "status": status
        }

        students.append(student)
        print("Student added successfully.")

    except ValueError:
        print("Invalid input.")

def view_students():
    if not students:
        print("No students found.")
        return

    for s in students:
        print(s)

def search_student():
    search = input("Enter ID or name: ")
    found = False

    for s in students:
        if s["id"] == search or s["name"].lower() == search.lower():
            print(s)
            found = True

    if not found:
        print("Student not found.")

def update_student():
    student_id = input("Enter ID to update: ")

    for s in students:
        if s["id"] == student_id:
            s["name"] = input("New name: ")
            s["age"] = int(input("New age: "))
            s["course"] = input("New course: ")
            s["status"] = input("New status: ")
            print("Student updated.")
            return

    print("Student not found.")

def delete_student():
    student_id = input("Enter ID to delete: ")

    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            print("Student deleted.")
            return

    print("Student not found.")

# ---------------- PERSISTENCE ----------------

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)
    print("Data saved.")

def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
        print("Data loaded.")
    except FileNotFoundError:
        print("No previous data found.")

# ---------------- MENU ----------------

def menu():
    load_data()

    while True:
        print("\n--- STUDENT SYSTEM ---")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Save data")
        print("7. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_student()
        elif option == "2":
            view_students()
        elif option == "3":
            search_student()
        elif option == "4":
            update_student()
        elif option == "5":
            delete_student()
        elif option == "6":
            save_data()
        elif option == "7":
            save_data()
            print("Goodbye.")
            break
        else:
            print("Invalid option.")

# ---------------- RUN ----------------

menu()