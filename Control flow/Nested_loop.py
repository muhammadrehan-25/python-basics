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
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()