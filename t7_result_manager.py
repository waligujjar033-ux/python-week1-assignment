# Ticket 7 - Student Result Manager

# Starting students (name, marks)
students = [
    ("Ali", 82),
    ("Sara", 67),
    ("Hassan", 39),
    ("Ayesha", 91),
    ("Usman", 55)
]


# Function to calculate grade
def get_grade(marks):

    if marks >= 80:
        return "A"

    elif marks >= 65:
        return "B"

    elif marks >= 50:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "F"


# Function to find student by name
def find_student(name):

    for i in range(len(students)):

        if students[i][0].lower() == name.lower():
            return i

    return -1


# Function to get valid marks
def get_marks():

    while True:

        marks = input("Enter marks (0-100): ")

        if not marks.isdigit():
            print("Error: Enter numbers only.")
            continue

        marks = int(marks)

        if marks >= 0 and marks <= 100:
            return marks

        else:
            print("Error: Marks must be 0 to 100.")


# Function to add student
def add_student():

    name = input("Enter student name: ").strip()

    if name == "":
        print("Error: Name cannot be empty.")
        return

    if find_student(name) != -1:
        print("Error:", name, "already exists.")
        return

    marks = get_marks()

    students.append((name, marks))

    print("Student added successfully!")


# Function to update or delete student
def update_delete():

    name = input("Enter student name: ").strip()

    index = find_student(name)

    if index == -1:
        print("Student not found.")
        return

    print("1. Update Student")
    print("2. Delete Student")

    choice = input("Choose: ")

    if choice == "1":

        marks = get_marks()

        students[index] = (students[index][0], marks)

        print("Student updated successfully!")

    elif choice == "2":

        students.pop(index)

        print("Student deleted successfully!")

    else:
        print("Invalid choice!")


# Function to show all students
def show_students():

    if len(students) == 0:
        print("No students available.")
        return

    # Sort students by marks (highest first)
    sorted_students = sorted(
        students,
        key=lambda student: student[1],
        reverse=True
    )

    print()
    print(f"{'#':<5}{'Name':<15}{'Marks':<10}{'Grade'}")
    print("-" * 40)

    number = 1

    for name, marks in sorted_students:

        grade = get_grade(marks)

        print(f"{number:<5}{name:<15}{marks:<10}{grade}")

        number += 1


# Function to show class statistics
def show_stats():

    if len(students) == 0:
        print("No students available.")
        return

    total = 0
    passed = 0
    failed = 0

    highest = students[0][1]
    lowest = students[0][1]
    topper = students[0][0]

    for name, marks in students:

        total += marks

        if marks > highest:
            highest = marks
            topper = name

        if marks < lowest:
            lowest = marks

        if marks >= 40:
            passed += 1

        else:
            failed += 1

    average = total / len(students)

    print()
    print("Topper:", topper, f"({highest})")
    print(f"Average: {average:.2f}")
    print("Highest:", highest, " Lowest:", lowest)
    print("Passed:", passed, " Failed:", failed)


# Function to search students
def search_student():

    search = input("Enter name to search: ").strip().lower()

    found = False

    for name, marks in students:

        if search in name.lower():

            print(name, "-", marks, "-", get_grade(marks))

            found = True

    if found == False:
        print("No student found.")


# Main menu
while True:

    print()
    print("===== Student Result Manager =====")

    print("1. Add Student")
    print("2. Update/Delete Student")
    print("3. Show All Students")
    print("4. Class Statistics")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_delete()

    elif choice == "3":
        show_students()

    elif choice == "4":
        show_stats()

    elif choice == "5":
        search_student()

    elif choice == "6":

        confirm = input("Are you sure? (y/n): ").lower()

        if confirm == "y":
            print("Goodbye!")
            break

        else:
            print("Exit cancelled.")

    else:
        print("Invalid choice! Try again.")