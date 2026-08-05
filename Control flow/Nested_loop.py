# ==========================================
# Nested Loops - Personal Notes
# ==========================================

"""
Nested Loop:
A loop inside another loop.

Golden Rules:
1. Outer loop decides the number of rows.
2. Inner loop decides what to print in each row.
3. For every one iteration of the outer loop,
   the inner loop starts from the beginning
   and runs completely.
"""

# Example 1
for i in range(3):
    for j in range(2):
        print(i, j)

print()

# Example 2
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()
    
print()
for i in range(1,6,):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

print()    
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print()
for i in range(6) :
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print() 
  
for i in range(1,6):
    for j in range(5, 5-i, -1):
        print(j, end=" ")
    print()
    
for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()