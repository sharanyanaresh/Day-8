# PROMPT USED

"""
Write a Python program that validates an Indian PAN card number format using if-else conditions.
PAN format: 5 uppercase letters, 4 digits, 1 uppercase letter (e.g., ABCDE1234F).
The 4th character indicates the type of taxpayer.
"""

# AI GENERATED CODE

pan = input("Enter PAN number: ")

if len(pan) == 10:
    
    if pan[:5].isalpha() and pan[:5].isupper():
        if pan[5:9].isdigit():
            if pan[9].isalpha() and pan[9].isupper():
                print("Valid PAN")
            else:
                print("Invalid PAN")
        else:
            print("Invalid PAN")
    else:
        print("Invalid PAN")

else:
    print("Invalid PAN length")


# CRITICAL EVALUATION

# 1. Position validation
# First 5 characters -> letters ✔
# Next 4 characters -> digits ✔
# Last character -> letter ✔

# 2. Edge cases
# Does not check taxpayer type at position 4
# Does not handle lowercase input
# No detailed error messages

# 3. Approach
# Character slicing approach used
# Regex could make this shorter but assignment required if-else

# 4. Pythonic?
# Logic is correct but nested if blocks reduce readability

# IMPROVED VERSION

pan = input("Enter PAN number: ")

if len(pan) != 10:
    print("Invalid PAN length")

elif not pan[:5].isalpha() or not pan[:5].isupper():
    print("First 5 characters must be uppercase letters")

elif not pan[5:9].isdigit():
    print("Characters 6-9 must be digits")

elif not pan[9].isalpha() or not pan[9].isupper():
    print("Last character must be uppercase letter")

else:
    taxpayer_type = pan[3]
    print("Valid PAN")
    print("Taxpayer type character:", taxpayer_type)