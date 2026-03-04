# transaction_analyzer.py

transactions = []

total_credit = 0
total_debit = 0

# while loop for input
while True:

    entry = input("Enter transaction amount (or 'done'): ")

    if entry.lower() == "done":
        break

    amount = float(entry)
    t_type = input("Type (credit/debit): ").lower()

    transactions.append(amount)

    # track totals
    if t_type == "credit":
        total_credit += amount
    else:
        total_debit += amount

    # high value flag
    if amount > 10000:
        print("⚠ High value transaction detected")

# summary calculations
count = len(transactions)

highest = max(transactions) if transactions else 0

average = sum(transactions) / count if count > 0 else 0

net_balance = total_credit - total_debit

# bar chart of last 10 transactions
print("\nTransaction Bar Chart")

last_transactions = transactions[-10:]

for amt in last_transactions:

    stars = int(amt / 1000)

    print("*" * stars, f"({amt})")

# summary
print("\nSummary")
print("Total transactions:", count)
print("Total credits:", total_credit)
print("Total debits:", total_debit)
print("Net balance:", net_balance)
print("Highest transaction:", highest)
print("Average amount:", round(average, 2))