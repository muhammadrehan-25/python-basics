history =[]
balance  = 5000
amount = 0
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
        print("Thanku for using ATM.")
        print("-" * 35)
        break
    if choice == 1:
        if not balance:
            print("Inffucient Balance,")
        else:
            print(f"Yor balance is: {balance}")
    elif choice == 2:
        amount = int (input("Enter amount to deposit."))
        balance+=amount
        history.append(f"Deposit amount: {amount}")
        print("Deposit successfully.")

    elif choice == 3:
        amount=int (input("Enter amount to withdraw"))
        if amount>balance:
            print("Insufficient balance.")
            
        else:
            balance-=amount
            history.append(f"Withdraw amount: {amount}")
            print("Withdraw Successfully.")
    elif choice == 4:
        if not history:
            print("No Historie Found.")
        else:
            for index,transaction in enumerate(history,start=1):
                 print(f"{index}.{transaction}")
    else:
        print("Invalid choice.")  
        
        
        
        
    