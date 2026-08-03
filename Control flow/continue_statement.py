


#Print numbers 1–10 but skip 5.
"""for i in range(1,10):
    if i == 5:
        continue
    print(i)"""
    
#Print numbers 1–10 but skip 5.
"""for i in range(1,20):
    if i % 2 == 0:
        continue
    print(i)"""

#Print characters of "Python" but skip 't'.
"""language = "Python"
for i in language:
    if i == "t":
        continue
    print(i)"""


#Print numbers 1–30 but skip numbers divisible by 4.

"""for i in range(1,30):
    if i % 4 == 0:
        continue
    print(i) """
    
#Ask the user for 5 numbers. Skip any negative number and print the positive ones.

"""for i in range (1,6):
    num = int(input("Enter five Numbers:"))
    if num < 0:
        continue
    print(num)"""
     
#Challenge 1 – Backend Log Filter
#Print every log except "DEBUG".
     
"""logs = ["INFO", "ERROR", "DEBUG", "ERROR", "INFO"]
for i in logs:
    if i == "DEBUG":
        continue
    print(i)"""
    
    
#Challenge 2 – AI Dataset Cleaner
#Skip all negative values and print the remaining numbers.

data = [12, -1, 45, -8, 23, 0, 67]
for i in data:
    if i <0:
        continue
    print(i)