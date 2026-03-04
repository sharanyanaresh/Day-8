import random
import string

def analyze_password(password):

    score = 0
    missing = []

    # Length rules
    if len(password) >= 16:
        score += 3
    elif len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        missing.append("too short")

    # Character checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in "!@#$%^&*":
            has_special = True

    if has_upper:
        score += 1
    else:
        missing.append("uppercase")

    if has_lower:
        score += 1
    else:
        missing.append("lowercase")

    if has_digit:
        score += 1
    else:
        missing.append("digit")

    if has_special:
        score += 1
    else:
        missing.append("special char")

    # Check repeated characters
    repeat = False
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            repeat = True

    if not repeat:
        score += 1

    return score, missing


def rating(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score <= 6:
        return "Strong"
    else:
        return "Very Strong"


# Keep asking until strong password
while True:

    password = input("Enter password: ")

    score, missing = analyze_password(password)

    print(f"Strength: {score}/7 ({rating(score)})")

    if missing:
        print("Missing:", ", ".join(missing))

    if score >= 5:
        print("Password accepted!")
        break
    else:
        print("Try again...\n")


# Password generator
length = int(input("\nEnter length for generated password: "))

characters = string.ascii_letters + string.digits + string.punctuation

generated = ""

for i in range(length):
    generated += random.choice(characters)

print("\nGenerated password:", generated)

score, missing = analyze_password(generated)

print(f"Strength: {score}/7 ({rating(score)})")