
#Question 1 — Login System

"""user_name = input("Enter username: ")
password = input("Enter password: ")

if user_name == "admin":
    if password == "python123":
        print("Login Successfully")
    else:
        print("Wrong password")
else:
    print("Invalid username")"""


#Question 2 — ATM Withdrawal

"""balance = float(input("Enter your balance: "))
withdraw =float(input("Enter amount to withdraw: "))

if balance>0:
    if withdraw<=balance:
        print("Transection Successfully")
    else:
        print("Insufficient balance")
else:
    print("Account blocked")"""


#Question 3 — AI API Access

"""api_key = input("Enter API key: ")
subscription = input("Have subscriiption (yes/no): ").strip().lower()
if not api_key =="" and len(api_key) >=10:
    if subscription == "yes":
        print("unlimited AI requests")
    else:
        print("Limited AI requests")
else:
    print("Invalid Api key")"""
    
    
#CHallenge Question

name = input("Enter your name: ").strip().lower()
percentage = int(input("Enter you %: "))
interview_passed=input("Interview Passes (yes/no): ").strip().lower()

if percentage>=80:
    if interview_passed == "yes":
        print("Name = ",name)
        print("Admession Granted")
    else:
        print("Name = ",name)
        print("Interview Failed")
else:
    print("Name = ",name)
    print("Not Elligible")