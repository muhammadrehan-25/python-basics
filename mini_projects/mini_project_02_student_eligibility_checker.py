#============== Student Eligibility Checker ================

print("============= Student Eligibility Checker ==============")
name = input("Enter Your Name: ")
age = int (input("Enter Your Age: "))
attendance = float(input("Enter Your Attendance %: "))
department = input("Enter Your Department: ")

print("========================================================")
print("Name                    : ",name)
print("Eligible for Admession  : ",age>=18)
print("Attendance abpve 75%    : ",attendance>=75.0)
print("Department is Software  : ",department == 'Software')
print("'Re' in Rehan           : ",'Re' in name)



