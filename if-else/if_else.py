# ==========================================
# Topic: Conditional Statements (Practice Solutions)
# ==========================================

# --- Question 1: Positive, Negative or Zero ---
number = int(input("Enter a number: "))
if number > 0:
    print("Number is positive")
elif number == 0:
    print("Number is zero")
else:
    print("Number is negative")


# --- Question 2: Temperature Checker ---
temperature = int(input("Enter temperature in 'Celsius': "))
if temperature > 30:
    print("Hot Weather")
elif 15 <= temperature <= 30:  # Pythonic Range Chaining
    print("Pleasant")
else:
    print("Cold Weather")


# --- Question 3: Grading System ---
marks = int(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid Input! Please enter marks between 0-100.")
elif marks >= 90:
    print("Grade = A+")
elif marks >= 80:
    print("Grade = A")
elif marks >= 70:
    print("Grade = B")
elif marks >= 60:
    print("Grade = C")
else:
    print("Grade = Fail")


# --- Question 4: Leap Year Checker ---
year = int(input("Enter year to check if it's a leap year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a Leap Year")
else:
    print("This is a normal year")


# --- Question 5: Authentication Router (True Guard Clause Pattern) ---
role = input("Enter your role (admin/developer/guest): ").strip().lower()
valid_roles = ['admin', 'developer', 'guest']

# Guard Clause 1: Invalid Role Check
if role not in valid_roles:
    print("Access Denied: Invalid role entered.")
else:
    is_active = input("Are you active? (yes/no): ").strip().lower() == "yes"
    
    # Guard Clause 2: Inactive User Check
    if not is_active:
        print("Access Denied: Account is disabled/inactive.")
    # Business Logic (Flat & Clean)
    elif role == 'admin':
        print("Full Access")
    elif role == 'developer':
        print("Code Access")
    elif role == 'guest':
        print("Only View Access")