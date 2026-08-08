# ==============================
# Task 9 - Student Record Management System
# ==============================

students = []

while True:

    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # -----------------------
    # Add Student
    # -----------------------

    if choice == "1":

        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        branch = input("Enter Branch: ")

        student = {
            "Name": name,
            "Age": age,
            "Branch": branch
        }

        students.append(student)

        print("Student Added Successfully!")

    # -----------------------
    # Display Students
    # -----------------------

    elif choice == "2":

        if len(students) == 0:
            print("No Student Records Found.")

        else:

            print("\nStudent Records")

            for student in students:
                print(student)

    # -----------------------
    # Search Student
    # -----------------------

    elif choice == "3":

        search = input("Enter Student Name: ")

        found = False

        for student in students:

            if student["Name"].lower() == search.lower():

                print("\nStudent Found")
                print(student)

                found = True

        if found == False:

            print("Student Not Found.")

    # -----------------------
    # Delete Student
    # -----------------------

    elif choice == "4":

        delete_name = input("Enter Student Name to Delete: ")

        found = False

        for student in students:

            if student["Name"].lower() == delete_name.lower():

                students.remove(student)

                print("Student Deleted Successfully!")

                found = True

                break

        if found == False:

            print("Student Not Found.")

    # -----------------------
    # Exit
    # -----------------------

    elif choice == "5":

        print("Thank You!")

        break

    else:

        print("Invalid Choice")