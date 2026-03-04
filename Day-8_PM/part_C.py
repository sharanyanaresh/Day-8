# PROMPT USED

"""
Write a Python program that prints a diamond pattern of asterisks.
The user inputs the number of rows for the upper half.
Include proper spacing and use nested loops only (no string multiplication tricks).
"""

# AI GENERATED CODE

n = int(input("Enter rows: "))

# upper half
for i in range(1, n+1):

    for j in range(n-i):
        print(" ", end="")

    for j in range(2*i-1):
        print("*", end="")

    print()

# lower half
for i in range(n-1, 0, -1):

    for j in range(n-i):
        print(" ", end="")

    for j in range(2*i-1):
        print("*", end="")

    print()


# CRITICAL EVALUATION

# Spacing correctness
# Pattern prints correctly centered diamond.

# Readability
# Code is readable but could benefit from comments.

# Edge cases
# n = 0 → prints nothing (should show message)
# n = 1 → prints a single star (works)

# Nested loops
# Correctly uses nested loops, no string multiplication.

# Time complexity
# O(n^2) since nested loops print roughly n^2 characters.


# IMPROVED VERSION

n = int(input("Enter rows: "))

if n <= 0:
    print("Invalid number of rows")

else:

    # upper half
    for i in range(1, n+1):

        for s in range(n-i):
            print(" ", end="")

        for star in range(2*i-1):
            print("*", end="")

        print()

    # lower half
    for i in range(n-1, 0, -1):

        for s in range(n-i):
            print(" ", end="")

        for star in range(2*i-1):
            print("*", end="")

        print()