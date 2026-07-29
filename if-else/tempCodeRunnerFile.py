marks=int(input("Enter marks '0-100':"))

if marks<0 or marks >100:
    print("Enter marks between 0-100")
elif marks>=90 and marks<=100:
    print("Grade = A+")
elif marks>=80 and marks<90:
    print("Grade = A")
elif marks >=70 and marks<80:
    print("Grade = B")
elif marks >=60 and marks<70:
    print("Grade = C")
elif marks<60:
    print("Fail")
else:
    print("Enter valid marks.")
    