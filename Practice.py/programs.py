# Check even or odd
# n = int(input("Enter a number: "))    
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Largest of three numbers
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# if a > b and a > c:
#     print("Larger", a)
# elif b > a and b > c:
#     print("Larger", b)
# else:
#     print("Larger", c)

# Swap two variable(without third)
# a , b = 5, 10
# b, a = a, b
# print(a, b)

# Print number 1 to 10
# for i in range(1, 11):
#     print(i)

#Even numbers between 1 to 50
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# Factorial using loop
# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print("factorial:", fact)


# Multiplication table
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{i} x {n} = {n*i}")

# Reverse digits using while loop
# n = int(input("Enter a number: "))
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10
# print("Reversed:", rev)

# Method 2
# num = int(input("Enter a number: "))
# reverse_number = int(str(num)[::-1])
# print("Reversed number:", reverse_number)

# Count vowels in a string
# s = input("Enter string: ").lower()
# count = 0
# for ch in s:
#     if ch in 'aeiou':
#         count += 1
# print("Vowels:", count)


# Check Palindrome string
# s = input("Enter string: ")
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# reversed string
# s = input("Enter a string: ")
# rev_string = s[::-1]
# print(rev_string)

# Count words in sentence
# s = input("Enter a sentence: ")
# word = s.split()
# print("Number of word:", len(word))

# Reverse string without slicing
# s = input("Enter string: ")
# rev = ' '
# for ch in s:
#     rev = ch + rev
# print("Reversed:", rev)

# Remove space from string
# s = "Hello, welcome!"
# no_space = s.replace(" ", "")
# print(no_space)

# Largest and smallest in list
# num = [4, 5, 6, 2, 45]
# print("Largest:", max(num))
# print("Smallest:", min(num))

# Sum of list element
# num = [1, 3, 4, 76, 5, 34]
# print("Sum", sum(num))

# Remove duplicates
# num = [1, 2, 3, 3, 4, 1]
# dupli = list(set(num))
# print(dupli)

# Find even numbers from list
# num = [1, 2, 3, 4, 5, 6, 7]
# even = [x for x in num if x % 2 == 0]
# print(even)

# Sort list without sort()
# num = [4, 1, 3, 2]
# for i in range(len(num)):
#     for j in range(i + 1, len(num)):
#         if num[i] > num[j]:
#             num[i], num[j] = num[j], num[i]
# print(num)

# Function for factorial
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact
# print(factorial(5))

# Function to check prime
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(7))

# Function to reverse string
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("Hello"))

# Fibonacci series
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
# fibonacci(10)

# Sum of even number in list
# def sum_even(lst):
#     total = 0
#     for x in lst:
#         if x % 2 == 0:
#             total += x
#     return total
# print(sum_even([1, 2, 3, 4, 5, 6]))

# Class Car
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def display(self):
#         print(f"Brand: {self.brand}, model: {self.model}")
# c1 = Car("Toyota", "Fortuner")
# c1.display()

# Class Student
# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
#     def show(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll)
# s1 = Student("Jay", 101)
# s1.show()

# Inheritance Example
# class Parent:
#     def display_parent(self):
#         print("This is Parent class")
# class Child(Parent):
#     def display_child(self):
#         print("This is Child class")
# c = Child()
# c.display_parent()
# c.display_child()

# Method Overriding
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# d = Dog()
# d.sound()

# Constructor Example
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def show(self):
#         print(f"Employee: {self.name}, Salary: {self.salary}")
# e1 = Employee("Harsh", 25000)
# e1.show()

# While loop

# Print number 1 to 10
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Print even numbers from 1 to 20
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# Print reverse order(10 to 1)
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# Sum of first 10 natural numbers
# i = 1
# total = 0
# while i <= 10:
#     total += i
#     i += 1
# print("Sum:", total)

# Find factorial of a number
# n = int(input("Enter a number: "))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("Factorial:", fact)

# OOPs 

# Create a class and object
# class Car:
#     def start(self):
#         print("Car Started...")
# p1 = Car()
# p1.start()

# Constructor example
# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
#     def show(self):
#         print(f"Name: {self.name}, Roll no: {self.roll}")
# s1 = Student("Harsh", 101)
# s1.show()

# Encapsulation(Private Variable)