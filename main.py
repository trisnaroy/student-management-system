students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added successfully")

def show_students():
    print("\nStudent List:")
    if len(students) == 0:
        print("No students found")
    else:
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student}")

def update_student():
    show_students()
    try:
        index = int(input("Enter student number to update: ")) - 1
        if 0 <= index < len(students):
            new_name = input("Enter new name: ")
            students[index] = new_name
            print("Student updated successfully")
        else:
            print("Invalid student number")
    except:
        print("Invalid input")

def delete_student():
    show_students()
    try:
        index = int(input("Enter student number to delete: ")) - 1
        if 0 <= index < len(students):
            students.pop(index)
            print("Student deleted successfully")
        else:
            print("Invalid student number")
    except:
        print("Invalid input")

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice") 