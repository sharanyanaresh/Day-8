# PART C

# Q1: Difference between elif and multiple if
# Multiple if statements evaluate each condition independently,
# so more than one block can execute.
# elif creates a single decision chain, so once one condition is true,
# the remaining conditions are skipped.

# Example:
# score = 85
# Using multiple if → Output: D, C, B
# Using elif → Output: B
# Reason: multiple if checks every condition, elif stops at the first true condition.


# Q2: Triangle classification function
def classify_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        print("Invalid triangle")

    elif a + b <= c or a + c <= b or b + c <= a:
        print("Not a triangle")

    elif a == b == c:
        print("Equilateral triangle")

    elif a == b or b == c or a == c:
        print("Isosceles triangle")

    else:
        print("Scalene triangle")


# Q3: Debug question
# Bug: Using multiple if statements causes grade to be overwritten
# because multiple conditions become true.
# Fix: Use elif so only one condition executes.