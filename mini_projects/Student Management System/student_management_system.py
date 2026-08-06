Students=[]
while True:
    print("===================================")
    print("    Student Management Systemm     ")
    print("===================================")
    
    print("1.Add Student.")
    print("2.Show All Student.")
    print("3.Remove Student.")
    print("4.Search student by name.")
    print("5.Exit")
    print("===================================")
    choice = int(input("Enter choice: "))
    if choice == 5:   
        print("Program Exiting.")
        print("-" * 35)
        break
    
    if choice == 1:
        name=input("Enter Student name: ").strip().lower()
        roll_nomber=input("Enter Roll Nomber: ").strip()
        age = int(input("Enter age: "))
        department = input("Enter Department: ").strip().lower()
        Student = [name,roll_nomber,age,department]
        Students.append(Student)
        print("Student added succesfully.")
        
    elif choice == 2:
        if not Students:
            print("No Student found.")
            
        else:
            for index,Student in enumerate(Students,start=1):
                print(f"\nStudents    : {index}")
                print(f"Name          : {Student[0].title()}")
                print(f"Roll Number   : {Student[1]}")
                print(f"Age           : {Student[2]}")
                print(f"Department    : {Student[3].title()}")
                print("-" * 35)
                  
    elif choice == 3:
        found=False
        if not Students:
            print("No Students Available.")
        name = input("Enter name to remove: ").strip().lower()
        for Student in Students:
            if Student[0]==name:
                found=True
                Students.remove(Student)
                print("Student Remove Successfully.")
                break
        if not found:
            print("Student not found.")
    elif choice == 4:
        name = input("Enter Name to Search: ").strip().lower()
        found=False
        if not Students:
            print("No Students Available.")
        for Student in Students:
            if Student[0] == name:
                found=True
                
                print(f"Name          : {Student[0].title()}")
                print(f"Roll Number   : {Student[1]}")
                print(f"Age           : {Student[2]}")
                print(f"Department    : {Student[3].title()}")
                print("-" * 35)
                break
        if not found:
                print("Student not found.")
           
    else:
        print("Enter Correct Choice.")
    