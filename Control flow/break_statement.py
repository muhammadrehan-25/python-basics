# ==========================================
#          Break Statement Practice
# ==========================================

# ------------------------------------------
# Question 1 (Easy)
# Print numbers from 1 to 10.
# Stop when the number becomes 6.
# ------------------------------------------

"""
for i in range(1, 11):
    if i == 6:
        break
    print(i)
"""

# ------------------------------------------
# Question 2 (Easy)
# Print each letter of the word.
# Stop when the letter is 'e'.
# ------------------------------------------

"""
word = "Backend"

for letter in word:
    if letter == "e":
        break
    print(letter)
"""

# ------------------------------------------
# Question 3 (Easy)
# Print every fruit until Mango is found.
# ------------------------------------------

"""
fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

for fruit in fruits:
    if fruit == "Mango":
        break
    print(fruit)
"""

# ------------------------------------------
# Question 4 (Easy-Medium)
# Ask the user to enter numbers continuously.
# Stop when user enters 0.
# ------------------------------------------

"""
while True:
    number = int(input("Enter Number: "))

    if number == 0:
        break

print("Program Ended")
"""

# ------------------------------------------
# Question 5 (Easy-Medium)
# Print numbers from 20 down to 1.
# Stop when number becomes 13.
# ------------------------------------------

"""
for i in range(20, 0, -1):
    if i == 13:
        break
    print(i)
"""

# ------------------------------------------
# Question 6 (Medium)
# Search for Python.
# ------------------------------------------

"""
languages = ["Java", "C++", "Python", "Go", "Rust"]

for language in languages:
    if language == "Python":
        print("Language Found")
        break
"""

# ------------------------------------------
# Question 7 (Medium)
# Login System
# Keep asking until correct password.
# ------------------------------------------

"""
while True:
    password = input("Enter Password: ")

    if password == "python123":
        print("Login Successful")
        break
"""

# ------------------------------------------
# Question 8 (Medium)
# Find first number divisible by 5.
# ------------------------------------------

"""
numbers = [15, 18, 22, 45, 60, 75]

for number in numbers:
    if number % 5 == 0:
        print("Found:", number)
        break
"""

# ------------------------------------------
# Question 9 (Hard)
# Search for Sara.
# ------------------------------------------

"""
students = [
    "Ali",
    "Ahmed",
    "Rehan",
    "Sara",
    "Bilal"
]

for student in students:
    if student == "Sara":
        print("Student Found")
        break
"""

# ------------------------------------------
# Question 10 (Hard)
# Print numbers from 1 to 100.
# Stop at the first number divisible by both
# 7 and 9.
# ------------------------------------------

"""
for i in range(1, 101):
    if i % 7 == 0 and i % 9 == 0:
        print("Found:", i)
        break
"""

# ==========================================
#               CHALLENGES
# ==========================================

# ------------------------------------------
# Challenge 1
# AI Login Gateway
# ------------------------------------------

"""
while True:
    api_key = input("Enter API Key: ")

    if api_key == "AI2026":
        print("Access Granted")
        break
"""

# ------------------------------------------
# Challenge 2
# Backend Request Queue
# ------------------------------------------

"""
requests = [
    "Login",
    "Upload",
    "Delete",
    "Shutdown",
    "Logout"
]

for request in requests:
    print("Processing:", request)

    if request == "Shutdown":
        print("Server Stopped")
        break
"""

# ------------------------------------------
# Challenge 3
# User Search
# ------------------------------------------

"""
users = [
    "Ali",
    "Ahmed",
    "Rehan",
    "Sara",
    "Hamza"
]

username = input("Enter Username: ")

found = False

for user in users:
    if user == username:
        found = True
        break

if found:
    print("User Exists")
else:
    print("User Not Found")
"""

# ------------------------------------------
# Challenge 4
# AI Token Monitor
# ------------------------------------------

"""
tokens = [120, 98, 76, 45, -5, 200]

for token in tokens:
    print("Token:", token)

    if token < 0:
        print("Invalid Token Detected")
        break
"""

# ------------------------------------------
# Challenge 5
# Security Scanner
# ------------------------------------------

"""
files = [
    "photo.jpg",
    "resume.pdf",
    "virus.exe",
    "notes.txt"
]

for file in files:
    print("Scanning:", file)

    if file == "virus.exe":
        print("Threat Detected")
        break
"""