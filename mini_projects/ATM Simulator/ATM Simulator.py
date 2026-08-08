history =[]
balance  = 5000
pin =1234
login = False
for i in range(3):
    user_pin=int(input("Enter pin to login: "))
    if user_pin == pin:
        print("-"*35)
        print("Login Successfully")
        print("-"*35)
        login = True 
        break

    else:
        print("Invalid Pin.")
if login:    
    while True:
        
            print("===================================")
            print("           ATM SIMULATOR           ")
            print("===================================")
            
            print("1.Check Balance.")
            print("2.Deposit Money.")
            print("3.Withdraw Money.")
            print("4.Transaction History .")
            print("5.Exit")
            print("===================================")
            choice = int(input("Enter choice: "))
            if choice == 5:   
                print("Thankyou for using ATM.")
                print("-" * 35)
                break
            if choice == 1:
                print("Your Balance is: ",balance)
                print("-"*35)
            elif choice == 2:
                amount = int (input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    history.append(f"Deposit amount: {amount}")
                    print("Deposit successfully.")
                else:
                    print("Amount must be greater then 0.")
                

            elif choice == 3:
                amount=int (input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be greater than 0")
                elif amount > balance:
                    print("Insufficient balance.")
                    print()
                    
                else:
                    balance-=amount
                    history.append(f"Withdraw amount: {amount}")
                    print("Withdraw Successfully.")
                    print()
            elif choice == 4:
                if not history:
                    print("No History Found.")
                    print()
                else:
                    for index,transaction in enumerate(history,start=1):
                        print(f"{index}.{transaction}")
                        print()
            else:
                print("Invalid choice.")  
                print()
                
                
                
            