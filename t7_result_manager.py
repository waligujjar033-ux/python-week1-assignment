# T7 - Student Result Manager

# Starting students
students = [
    ("Ali", 82),
    ("Sara", 67),
    ("Hassan", 39),
    ("Ayesha", 91),
    ("Usman", 55)
]


# Main menu
while True:

    print("\n===== Student Result Manager =====")
    print("1. Add Student")
    print("2. Update/Delete Student")
    print("3. Show All Students")
    print("4. Class Statistics")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Choose: ")


    # OPTION 1 - ADD STUDENT
    if choice == "1":

        name = input("Enter student name: ").strip()

        if name == "":
            print("Error: Name cannot be empty.")
            continue

        # Check duplicate name
        exists = False

        for student in students:
            if student[0].lower() == name.lower():
                exists = True
                break

        if exists:
            print("Error:", name, "already exists.")
            continue

        # Check valid marks
        while True:

            marks = input("Enter marks (0-100): ")

            if marks.isdigit():

                marks = int(marks)

                if 0 <= marks <= 100:
                    break

            print("Error: Marks must be 0 to 100.")

        students.append((name, marks))

        print("Student added successfully!")


    # OPTION 2 - UPDATE OR DELETE
    elif choice == "2":

        name = input("Enter student name: ").strip()

        index = -1

        # Find student
        for i in range(len(students)):

            if students[i][0].lower() == name.lower():
                index = i
                break

        if index == -1:
            print("Student not found.")
            continue

        print("1. Update Student")
        print("2. Delete Student")

        action = input("Choose: ")

        if action == "1":

            while True:

                marks = input("Enter new marks (0-100): ")

                if marks.isdigit():

                    marks = int(marks)

                    if 0 <= marks <= 100:
                        break

                print("Error: Marks must be 0 to 100.")

            # Replace old tuple with new tuple
            students[index] = (students[index][0], marks)

            print("Student updated successfully!")

        elif action == "2":

            students.pop(index)

            print("Student deleted successfully!")

        else:
            print("Invalid choice!")


    # OPTION 3 - SHOW ALL STUDENTS
    elif choice == "3":

        if len(students) == 0:
            print("No students available.")
            continue

        # Sort students by highest marks
        # Bubble sort using loops
        sorted_students = students.copy()

        for i in range(len(sorted_students)):

            for j in range(len(sorted_students) - 1):

                if sorted_students[j][1] < sorted_students[j + 1][1]:

                    sorted_students[j], sorted_students[j + 1] = (
                        sorted_students[j + 1],
                        sorted_students[j]
                    )

        print()
        print(f"{'#':<5}{'Name':<15}{'Marks':<10}{'Grade'}")
        print("-" * 40)

        number = 1

        for student in sorted_students:

            name = student[0]
            marks = student[1]

            # Calculate grade
            if marks >= 80:
                grade = "A"

            elif marks >= 65:
                grade = "B"

            elif marks >= 50:
                grade = "C"

            elif marks >= 40:
                grade = "D"

            else:
                grade = "F"

            print(f"{number:<5}{name:<15}{marks:<10}{grade}")

            number += 1


    # OPTION 4 - CLASS STATISTICS
    elif choice == "4":

        if len(students) == 0:
            print("No students available.")
            continue

        total = 0
        passed = 0
        failed = 0

        highest = students[0][1]
        lowest = students[0][1]
        topper = students[0][0]

        for student in students:

            name = student[0]
            marks = student[1]

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


    # OPTION 5 - SEARCH STUDENT
    elif choice == "5":

        search = input("Enter name to search: ").strip().lower()

        found = False

        for student in students:

            name = student[0]
            marks = student[1]

            if search in name.lower():

                # Calculate grade
                if marks >= 80:
                    grade = "A"

                elif marks >= 65:
                    grade = "B"

                elif marks >= 50:
                    grade = "C"

                elif marks >= 40:
                    grade = "D"

                else:
                    grade = "F"

                print(name, "-", marks, "-", grade)

                found = True

        if found == False:
            print("No student found.")


    # OPTION 6 - EXIT
    elif choice == "6":

        confirm = input("Are you sure? (y/n): ").lower()

        if confirm == "y":
            print("Goodbye!")
            break

        else:
            print("Exit cancelled.")


    # INVALID MENU OPTION
    else:
        print("Invalid choice! Try again.")