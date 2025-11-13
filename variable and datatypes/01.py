
# String(str)

# s = "python programming"
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.strip())
# print(s.replace("o", "m"))
# print(s.split())
# print(s.find("o"))
# print(s.count("o"))


# List(list)

# nums = [10, 10, 20, 30, 40, 50]
# nums.append(60) add one item
# nums.extend([70, 80]) add multiple item
# nums.insert(2, 70) add item at index
# nums.remove(10) remove item
# nums.pop(4) # remove by index
# nums.sort() sort ascending
# nums.reverse() reverse order
# nums.count(10) count occurrences
# nums.index(30) return index
# print(nums)


# Tuple(tuple)

# t = (1, 2, 3, 4)
# print(t.count(3))
# print(t.index(3))


# Set(set)

# s = {1, 2, 3, 3, 4}
# s2 = {2, 5, 6, 7}
# s.add(5) add element
# s.update([6, 7]) add multiple element
# s.remove(2) remove 
# s.discard(2) remove safely
# s.pop() remove random element
# s.clear()
# union_set = s.union(s2)
# print(f"Union using union() method: {union_set}")
# inter_section = s.intersection(s2)
# print(f"inter_section {inter_section}")
# diff = s.difference(s2)
# print(f"Difference is: {diff}")

# Frozen Set(frozenset)

# fs = frozenset([1, 2, 3])
# print(fs)

# Dictionary(dict)

# student = {"name": "Harsh", "age": 21, "city": "Ahmedabad"}
# print(student.keys()) return all keys
# print(student.values()) return all values
# print(student.items()) return pairs
# print(student.get("name")) return value safely
# print(student.update({"age":22})) update values
# print(student.pop("city"))
# print(student.pop)
# student["domain"] = "Python"
# print(student)

# Slicing

# Slicing means extracting specific part from sequence

# sequence[start: end: step]

# num = [10, 20, 30, 40, 50]
# print(num[1:4])

# 1. String 
# s = "Python"
# print(s[0:4])
# print(s[:3])
# print(s[2:])
# print(s[-3:])
# print(s[::-1])

# 2. List slicing

# L = [10, 20, 30, 40, 50, 60]
# print(L[1:4])
# print(L[:3])
# print(L[::2])
# print(L[::-1])

# 3. Tuple Slicing

# t = (1, 2, 3, 4, 5, 6)
# print(t[1:4])

# 4. Set Slicing

# s = {10, 20, 30, 40, 50}
# L = list(s)
# print(L[1:4])

# 5. Dictionary Slicing

# d = {"a":1, "b":2, "c":3, "d":4}
# keys = list(d.keys())
# values = list(d.values())

# print(keys[1:3])      
# print(values[::-1])  


# 1.for Loop

# for i in range(5):
#     print(i)

# fruits = ["apple", "banana", "cherry"]
# for item in fruits:
#     print(item)

# for i in range(1, 10, 2):
#     print(i)


# 2. while Loop

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# count = 5
# while count > 0:
#     print(count)
#     count -= 1
# print("Blast off!")

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# 3. Nested Loop

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i * j, end=" ")
#     print()

# Example with enumerate():

# Cars = ["BMW", "LC300","M5CS"]
# for index, Cars in enumerate(Cars):
#     print(index, Cars)

# Example with zip():

# lang = ["Python", "JavaScript"]
# scores = [90, 89]
# for l, s in zip(lang, scores):
#     print(l, "=", s)

# Star pattern

# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()

# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     for space in range(n - i):
#         print(" ", end="")
#     for star in range(2 * i - 1):
#         print("*", end="")
#     print()

# Phase 2:- Functions

# def greet():
#     print("Welcome to Python!")
# greet()

# Function with parameters

# def user(name):
#     print("Hello", name)
# user("Python")

# Function with return value

# def add(a, b):
#     return a + b
# result = add(5, 6)
# print(result)

# Function without parameters but with return

# def pi():
#     return 3.14
# print(pi())

# Function Flow

# def lang(name):
#     return "Hello " + name
# msg = lang("Python")
# print(msg)

# Function to find a square:
# def square(num):
#     return num * num
# n = int(input("Enter a number: "))
# print("Square:", square(n))

# Function to print multiplication table
# def table(n):
#     print(f"Multiplication table of {n}")
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n*i}")
# num = int(input("Enter a number: "))
# table(num)

# Part 2 - Function Arguments in python

# positive arguments
# def student(name, age):
#     print("Name", name)
#     print("Age", age)
# student("Harsh", 21)


# Keyword Arguments
# def student(name, age):
#     print("Name", name)
#     print("Age", age)
# student(age=21, name="Harsh")

# Default Arguments
# def greet(name = "Guest"):
#     print("Hello", name)
# greet("Harsh")
# greet()

# Arbitrary Arguments

# *args --> Multiple Positional Arguments
# def add_numbers(*nums):
#     total = 0
#     for n in nums:
#         total += n
#     print("Sum =", total)
# add_numbers(2, 4, 6)
# add_numbers(5, 10, 5)

# **kwargs --> Multiple Keyword Arguments
# def show_details(**info):
#     for key, value in info.items():
#         print(f"{key} -> {value}")
# show_details(name="Harsh", age=20, city="Ahmedabad" )

# Practice Task 

# Default Argument
# def details(name, age=18):
#     print("Name:", name)
#     print("Age:", age)
# details("Harsh", 20)
# details("Raj")

# Using *args(Sum of all numbers)
# def sum_all(*numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total
# print("Sum =", sum_all(2, 4, 6))
# print("Sum =", sum_all(10, 20, 30, 40))

# Using **kwargs(profile info)
# def profile(**data):
#     for key, value in data.items():
#         print(f"{key} -> {value}")
# profile(name="Harsh", age=20, skill="Python")

# Mix of positional, Default, and *args
# def user_profile(name, age=18, *hobbies):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     if hobbies:
#         print("Hobbies:")
#         for hobby in hobbies:
#             print("-", hobby)
#     else:
#         print("No hobbies added.")
# user_profile("Harsh", 21, "Coding", "Music", "Cricket")
# user_profile("Raj")

# Mixed Arguments Example
# def all_types(name, *skills, age=18, **info):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print("Skill:", skills)
#     print("Other info:", info)
# all_types("Harsh", "Python", "HTML", age=21, city="Ahmedabad", goal="Web Developer")

# Lambda (Anonymous) Functions
# add = lambda a, b: a + b
# print(add(5, 3))

# Square of a Number
# Square = lambda x: x * x
# print(Square(6))

# Even or Odd Checker
# check = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(check(10))
# print(check(7))

# Multiple Arguments
# multiply = lambda a, b, c: a * b * c
# print(multiply(2, 3, 4))

# Lambda inside map()
# nums = [1, 2, 3, 4, 5]
# square = list(map(lambda x: x**2, nums))
# print(square)

# Lambda inside filter()
# nums = [10, 25, 30, 45, 50, 65]
# even = list(filter(lambda x: x % 2 == 0, nums))
# print(even)

# Lambda inside reduce()
# from functools import reduce

# nums = [2, 4, 6, 8, 10]
# result = reduce(lambda n, i: n + i, nums)
# print("Sum =", result)

# Lambda inside sorted
# students = [("Harsh", 22), ("Raj", 19), ("Amit", 25)]
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)

# Sort Dictionary by Value
# scores = {'Harsh': 80, 'Raj': 95, 'Amit': 70}
# sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
# print(sorted_scores)

# List Comprehension
# square = [i * i for i in range(5)]
# print(square)

# create list of squares
# nums = [1, 2, 3, 4, 5]
# square = [x**2 for x in nums]
# print(square)

# Get Even Numbers only
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# even = [x for x in nums if x % 2 == 0]
# print(even)

# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Convert Strings to Uppercase
# names = ["harsh", "raj", "amit"]
# upper_names = [name.upper() for name in names]
# print(upper_names)

# Flatten a Nested List (2D → 1D)
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [num for row in matrix for num in row]
# print(flattened)

# Nested List Comprehension (Matrix Creation)
# matrix = [[j for j in range(1, 4)] for i in range(2)]
# print(matrix)

# Cub of Numbers
# cubs = [x**3 for x in range(1, 11)]
# print("Cubes from 1 to 10:", cubs)

# Convert Celsius to Fahrenheit
# cel = [0, 10, 20, 30, 40]
# far = [(c * 9/5) + 3 for c in cel]
# print("Fahrenheit value:", far)

# Generate a 3X3 Matrix
# matrix = [[j for j in range(1, 4)] for i in range(3)]
# for row in matrix:
#     print(row)

# Set Operations(Math Style)

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A|B)  Union 
# print(A & B) Intersection
# print(A - B) Difference
# print(A ^ B) Symmetric Difference

# Looping Through a Set
# fruits = {"apple", "banana", "cherry"}
# for item in fruits:
#     print(item)

# Set Comprehension
# squares = {x**2 for x in range(1, 6)}
# print(squares)

# Remove Duplication from a List set
# numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]
# unique_numbers = set(numbers)
# print("Unique numbers:", unique_numbers)

# Add and Remove Element
# fruits = {"apple", "banana"}
# print("Original:", fruits)
# fruits.add("mango")
# print("After add:", fruits)
# fruits.discard("banana")
# print("After discard:", fruits)
# fruits.clear()
# print("After clear:", fruits)

# Set Comprehension
# even = {x for x in range(1, 21) if x % 2 == 0}
# print("Even numbers:", even)

# Subset and Superset Check
# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5 ,6}
# print("A is subset of B:", A.issubset(B))
# print("B is superset of A:", B.issuperset(A))

# 🔹 What is a Dictionary?

# A dictionary stores data in key-value pairs.
# It’s like a real dictionary — you look up a key (word) and get its value (meaning).

# info = {"name:" "Harsh", "language:" "Python"}
# print(info["name"])
# print(info.get("language"))

# Dictionary Comprehension
# square = {x: x**2 for x in range(1, 6)}
# print(square)

# Copying Dictionaries
# d1 = {"a":1, "b": 2}
# d2 = d1.copy()
# d2["a"] = 99
# print("Original:", d1)
# print("Copy:", d2)

# Practice 

# Create and Access a dictionary
# person = {"name": "Harsh", "age": 21, "city": "Ahmedabad"}
# print("Name:", person["name"])
# print("Age:", person.get("age"))

# Add, Update, and Delete Items
# student = {"name": "Raj", "course": "Python"}
# student["age"] = 22
# student["course"] = "JavaScript"
# student.pop("age")
# print(student)

# Loop through Dictionary
# fruits = {"apple": 100, "banana": 50, "mango": 120}
# for fruits, price in fruits.items():
#     print(f"The price of {fruits} is Rs.{price}")

# Nested Dictionary
# student = {
#     "s1": {"name": "Harsh", "marks": 99},
#     "s2": {"name": "Raj", "marks": 91},
#     "s3": {"name": "Dhruv", "marks": 76}
# }
# print(student["s2"]["name"])
# print(student["s3"]["marks"])

# Strings

# Basic Operations
# name = "Harsh"
# print(len(name))          Length
# print(name[0])            Access character by index
# print(name[-1])           Last character
# print(name[1:4])          Slicing
# print(name + " Chavda")   Concatenation
# print(name * 3)           Repetition
