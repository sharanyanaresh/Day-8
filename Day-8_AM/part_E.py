# Smart Transaction Validator

amount = float(input("Transaction amount (Rs): "))
category = input("Category (food/travel/electronics/other): ").lower()
hour = int(input("Hour of transaction (0-23): "))
daily_spent = float(input("Amount already spent today (Rs): "))

# BLOCK rules
if amount > 50000:
    print("BLOCKED: exceeds single transaction limit")

elif daily_spent + amount > 100000:
    print("BLOCKED: exceeds daily spending limit")

# FLAG rule
elif hour < 6 or hour > 23:
    print("FLAGGED: unusual transaction hour")

# Category limits
elif category == "food" and amount >= 5000:
    print("FLAGGED: food category limit exceeded")

elif category == "electronics" and amount >= 30000:
    print("FLAGGED: electronics category limit exceeded")

else:
    print("APPROVED")

vip = input("VIP customer? (yes/no): ").lower() == "yes"

single_limit = 100000 if vip else 50000
daily_limit = 200000 if vip else 100000

food_limit = 10000 if vip else 5000
electronics_limit = 60000 if vip else 30000

if amount > single_limit:
    print("BLOCKED: exceeds single transaction limit")

elif daily_spent + amount > daily_limit:
    print("BLOCKED: exceeds daily spending limit")

elif hour < 6 or hour > 23:
    print("FLAGGED: unusual transaction hour")

elif category == "food" and amount >= food_limit:
    print("FLAGGED: food category limit exceeded")

elif category == "electronics" and amount >= electronics_limit:
    print("FLAGGED: electronics category limit exceeded")

else:
    print("APPROVED")