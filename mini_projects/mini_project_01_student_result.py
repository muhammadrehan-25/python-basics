# Mini Project 1: Student Grade Calculator

name=input("Enter Student Name: ")
roll_number=input("Enter Roll Number: ")
py_marks=int(input("Enter python marks: "))
java_marks=int(input("Enter java marks: "))
DSA_marks=int(input("Enter DSA marks: "))

total_marks=300
Total=py_marks+java_marks+DSA_marks
Average=Total/3
Percentage=(Total/total_marks)*100

print()
print("========= Student Result =========")
print(end="\n\n")

print("Name              :",name)
print("Roll Number       :",roll_number)
print(end="\n\n")

print("Python marks      :",py_marks)
print("Java marks        :",java_marks)
print("DSA marks         :",DSA_marks)
print(end="\n\n")

print("Total             :",Total) 
print(f"Average           :{Average:.2f}")
print(f"Percentage        :{Percentage:.2f}%")
print(end="\n\n")

print("====================================")