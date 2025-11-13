# # Basic usage
# print("Hello, Python!")

# # Printing multiple items:
# name = "Python"
# age = 20
# print("Name:", name, "Age:", age)

# # Using f-string(formatted string)
# print(f"The language is {name} and {age} ")

# # Using .formate() method
# print("My name is {} and I am {} years old.".format(name, age))

# # Special characters \n, \t
# print("Hello\nWorld")
# print("Name:\tPython")

# # Taking input from User(input())
# name1 = input("Enter your name: ")
# print(f"Hello, {name1}!")


# # input as Numbers
# age = int(input("Enter your age: "))
# height = float(input("Enter your height in meters: "))
# print(f"You are {age} years old and {height} meters tall.")


# Multiple input 
# x, y = input("Enter two numbers separated by space: ").split()
# x = int(x)
# y = int(y)
# print(f"Sum: {x + y}")

# Output Formatting Techniques
# name = "Harsh"
# age = 20
# print("Name:", name, "Age:", age)

# # Using + Operator(concatenation)
# print(f"Name: {name}, Age: {age}")

# # Using f-string
# print(f"Name: {name}, Age: {age}")

# # Using .formate() method
# print("Name: {}, Age: {}".format(name, age))

# Advanced Input Tricks
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(f"Sum = {num1 + num2}")

# # Taking list input in one line:
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# print(numbers)

# Practical Example
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print(f"Hello {name}!")
print(f"Age next year: {age + 1}")
print(f"Height in cm: {height * 100}")
