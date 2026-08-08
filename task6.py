# Task 6 - Functions

# Function to calculate square
def square(number):
    return number * number


# Function to calculate average
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3


print("===== Functions Program =====")

# Input for square
number = int(input("Enter a number: "))

# Call square function
result = square(number)

print("Square =", result)

print()

# Input for average
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Call average function
avg = average(a, b, c)

print("Average =", avg)