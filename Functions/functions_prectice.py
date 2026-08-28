"""def average(a,b,c):
    return (a+b+c)/3
result = average(10,20,30)
print(result)"""


"""def calculator(a,b):
    add = a+b
    multi = a*b
    return add,multi
add,multi = calculator(5,4)
print(add)
print(multi)
"""

"""def info(name,age,city):
    print(f"My name is {name}.")
    print(f"I m {age} years old.")
    print(f"I m living in {city}")
    return
info("Rehan",21,"Karachi");"""

"""def intro(name,city="Khairpur"):
    print("my name is",name)
    print("I m living in",city)
    return
intro("Rehan","karachi")"""

"""def employe(name,salary = 50000,department="IT"):
    print("Name       :",name)
    print("Salary     :",salary)
    print("Department :",department)
    print()
    return
employe("Rehan")
employe("Rehan",670000)
employe(name="ALi",salary=990000,department="Buisness administration")"""

"""def add(*args):
    total=0
    for i in args:
        total+=i
    return total

result=add(5,10,15,20,25)
print(result)"""

"""def number(*args):
    for i in args:
        print(i)
    return
number(10,23,34,53,53,56,32)"""

"""def even_numbers(*args):
    for i in args:
        if i % 2 == 0:
            print(i)
    return
even_numbers(2,3,4,5,6,8,10,11,12,14,17,20,18)"""

"""def largest_number(*args):
    largest=args[0]
    for i in args:
        if i > largest:
            largest = i
    return largest
result=largest_number(1,3,5,0,19,56,78,98,78,89)
print(result)"""

"""def info(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
    return
info(name="Rehan",age=21,department="Software")"""

"""def student(name,*subjects,**details):
    print("Name :",name)
    print()
    print("Skills:")
    for i in subjects:
        print(i)
    print()
    print("Info:")
    for key,value in details.items():
        print(key,":",value)
    return
student("Rehan",
        "Python","Java","C++","DSA",
        age=21,city="karachi",department="SE"
        )"""
        
"""def calculator(a,b):
    def add():
         return a+b    
    return add()
    def multiply():
        return a*b
    return multiply

result=calculator(5,4)
print(result)"""

"""students=[
    ("Rehan",89),
    ("Ali",78),
    ("Ahmed",98)
]

students.sort(key=lambda students:students[1], reverse=True)
print(students)"""

"""def add(a,b):
    return a+b
def multiply_by_two_numbers(number):
    result=add(number,number)
    return result
print(multiply_by_two_numbers(10))


def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
def calculate(a,b):
    multiplication=multiply(a,b)
    subtration=subtract(a,b)
    return multiplication,subtration
multiply_result,subtrat_result=calculate(15,7)
print(multiply_result)
print(subtrat_result)"""
    
"""    
def add(a,b):
    return a+b
def square(number):
    return number*number
def final_result(a,b):
    result=add(a,b)
    result=square(result)
    return result
result=final_result(2,3)
print(result)"""

"""def process_username(username):
    username= username.strip()
    username=username.lower()
    return username
result=process_username("    REHAN123     ")
print(result)"""

"""def validate_username(username):
    username=username.strip()
    username=username.lower()
    if len(username)>=5:
        return True
    else:
        return False
    return 
result=validate_username("    REHan123   ")
print(result)
    
def count_even(numbers):
    count=0
    for i in numbers:
        if i % 2 == 0 :
            count+=1
    return count
    
result=count_even([12,34,54,43,55,56,59,87,80,35])
print(result)"""
         
"""def add(a,b=4):
    Ali is a hardworker boy and  do work fo his family 
    return a+b
result=add(5)
print(result)"""



   
