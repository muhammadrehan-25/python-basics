

#Challenge 1 — Login System

#Keep asking the user for a password until they enter:
#python123
#Then print:
#Login Successful

"""password = ""

while password != "python123":
    password = input("Enter password: ")

print("Login Successful")"""

#🔥 Challenge 2 — ATM PIN
#atm pin verifier
"""pin=""
count=1
while count<=3:
    pin=int(input("Enter your pin: "))
    count+=1
    if pin==4321:
        print("Access granted")
        break
    else:   
        print("Card bloocked") """
       
       
#       Challenge 3 — AI API Tokens
"""
Start with:
tokens = 100
Ask the user:
How many tokens to use?
Subtract the tokens.
Repeat until tokens become 0 or less.
Finally print:

No Tokens Remaining """


"""tokens=100
while tokens>0:
    use_tokens=int(input("How many tokens to use: "))
    tokens-=use_tokens
    
    print("Remainuing tokens are: ",tokens)"""


#Challenge 4 — Backend Request Queue
"""request = 1
while request<=5:
    print("Processing request: ",request)
    request+=1"""

request=" "
while request!="no":
    request=input("Upload another file (yes/no): ").strip().lower()
print("Finished")