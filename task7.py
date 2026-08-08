# ==============================
# Task 7 - Strings & Collections
# ==============================

print("===== Task 7 : Strings & Collections =====")

# -----------------------------
# STRING OPERATIONS
# -----------------------------

text = input("Enter a sentence: ")

print("\n--- String Operations ---")

print("Original String :", text)

print("Uppercase :", text.upper())

print("Lowercase :", text.lower())

print("Replace Python with Data Analytics :")
print(text.replace("Python", "Data Analytics"))

word = input("Enter a word to find: ")

position = text.find(word)

print("Position of the word :", position)


# -----------------------------
# LIST OPERATIONS
# -----------------------------

print("\n--- List Operations ---")

numbers = []

for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    numbers.append(num)

print("Original List :", numbers)

remove_number = int(input("Enter a number to remove: "))

if remove_number in numbers:
    numbers.remove(remove_number)
    print("After Remove :", numbers)
else:
    print("Number not found in the list.")

numbers.sort()

print("Sorted List :", numbers)


# -----------------------------
# TUPLE
# -----------------------------

print("\n--- Tuple ---")

student = ("Adithyan", 21, "BCA")

print("Tuple :", student)

print("First Element :", student[0])

print("Second Element :", student[1])

print("Third Element :", student[2])


# -----------------------------
# DICTIONARY
# -----------------------------

print("\n--- Dictionary ---")

student_info = {
    "Name": "Adithyan",
    "Age": 21,
    "Branch": "BCA",
    "College": "University of Calicut"
}

print(student_info)

print("Student Name :", student_info["Name"])

print("Branch :", student_info["Branch"])


# -----------------------------
# SET
# -----------------------------

print("\n--- Set ---")

colors = {"Red", "Blue", "Green"}

print("Original Set :", colors)

colors.add("Yellow")

print("After Add :", colors)

colors.remove("Blue")

print("After Remove :", colors)
