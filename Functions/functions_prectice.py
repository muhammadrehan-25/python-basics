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

def largest_number(*args):
    largest=args[0]
    for i in args:
        if i > largest:
            largest = i
    return largest
result=largest_number(1,3,5,0,19,56,78,98,78,89)
print(result)