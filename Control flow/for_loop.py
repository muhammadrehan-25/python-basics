#============================================
#          Writing Real for Loops
#===========================================

#            Prectice Questions


#1.Question
"""for i in range(1,6):
    print(i,"Hello")"""

#Question 2

#Print numbers from 1 to 10.
"""for i in range(2,10,2):
    print(i)"""

#Question 3

#Print all even numbers from 2 to 20.

"""for i in range(2,21,2):
    print(i)"""
    
    
#Question 4

#Print all odd numbers from 1 to 19.

"""for i in range(1,20,2):
    print(i)"""
    
    
#Challenge 1

#Print the multiplication table of 7.
"""table=7
for i in range(1,11):
    print(f"{table} x {i} = {table*i}")"""
  
  
#Challenge 2

#Print the countdown:  
"""for i in range(10,0,-1):
    print(i)"""
    
"""table = int (input("Enter table number: "))
for i in range (1,11):
    print(tablle,"x",i,"=",table*i)
    """
"""sum=0
for i in range (2,51,2):
    print(i)
    sum+=i
print("sum: ",sum) """
"""
department=input("Enter your department: ")

for index,char in enumerate(department,start=1):
    print(f"{char} :{index}")"""
    
#Question 1 (Easy)

#Print each character of the following string on a new line.

#ame = "Rehan"
    
"""name ="Rehan"
for letter in name:
    print(letter)"""

#Question 2 (Easy)
#Print each programming language.
#languages = ["Python", "Java", "C++", "Go"]    

"""languages = ['Python','Java','C++','Go']
for language in languages:
    print(language)"""
    
#Question 3 (Easy)
#Print each fruit with its position using enumerate().
#fruits = ["Apple", "Banana", "Mango"]

"""fruits = ["Apple","Banana","Mango"]
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)"""


#Question 4 (Easy-Medium)
#Print only vowels from the string.

"""word = "Artificial Inteligence"
for char in word:
    if char.lower() in "aeiou":
        print(char)"""
        
#Question 5 (Easy-Medium)

#Count how many characters are in the string without using len().

"""text = "Backend"
count =0
for i in text:
    count+=1
print("Total Characters =",count)"""


#Question 6 (Easy-Medium)

#Print only those numbers that are greater than 50.

"""numbers = [10, 55, 70, 25, 90, 40]
for number in numbers:
    if number>50:
        print(number)"""
        
#Question 7 (Medium)

#Print each student's name with its roll number.
"""
students = ["Ali", "Ahmed", "Rehan", "Bilal"]
for index,student in enumerate(students,start=1):
    print(f"Roll Number {index} : {student}")"""
    
#Question 8 (Medium)

#Find how many times the letter 'a' appears.

"""sentence = "Pakistan Zindabad"
count = 0
for i in sentence:
   if i.lower() in "a":
        count+=1
print("Total a =",count) """ 
        
        
#Question 9 (Medium-Hard)

#Print only the names that start with the letter A.

"""names = ["Ali","Ahmed","Rehan","Ayisha","Nida","Bilal","Arshad"]
for name in names:
    if name[0]=="A":
        print(name)"""
        
#Question 10 (Medium-Hard)

"""Given:

tasks = [
    "Login",
    "Upload File",
    "Generate AI Response",
    "Logout"
]

Print:

Task 1 : Login
Task 2 : Upload File
Task 3 : Generate AI Response
Task 4 : Logout"""

"""tasks = [
    "Login",
    "Upload File",
    "Generate AI Response",
    "Logout"
]
for index,task in enumerate(tasks,start=1):
    print(f"Task {index} : {task}")"""
    
    
#Challenge 1 — AI Request Processor
#Print:

"""requests = [
    "Translate Text",
    "Summarize PDF",
    "Generate Email",
    "Analyze CSV"
]

for index,request in enumerate(requests):
    print(f"Processing : {request}")
"""
    
    
#Challenge 2 — User Login Checker
#users = [
 #   "Ali",
  #  "Ahmed",
   # "Rehan",
    #"Sara"
#]

#Ask the user for a username.
#If the username exists, print:
#Login Successful
#Otherwise:
#User Not Found

"""users = ["Ali","Rehan","Ahmed","Sara"]
found = False
username = input("Enter user name: ")
for user in users:
    if user == username:
        found = True
        break
    
if found:
        print("Login successful")
else:
        print("Usernot found")"""
        
#Challenge 4 — Backend Log Viewer
#Count how many "ERROR" logs are present.

"""logs = [
    "INFO",
    "ERROR",
    "INFO",
    "WARNING",
    "ERROR"
]

count = 0
for i in logs:
    if i == "ERROR":
        count+=1
print("Total error fount =",count)"""



#Challenge 5 — AI Token Report

"""tokens = [120, 80, 0, 250, 40]
for i in tokens:
    if i>100:
        print(i)"""