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

department=input("Enter your department: ")

for index,char in enumerate(department,start=1):
    print(f"{char} :{index}")