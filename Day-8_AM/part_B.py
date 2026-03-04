# Tax Calculator — Indian Income Tax (New Regime FY 2024-25)

income = float(input("Enter annual income: "))

# standard deduction
taxable_income = income - 75000
if taxable_income < 0:
    taxable_income = 0

print("\nTaxable Income:", taxable_income)

tax = 0

# 0–3L
slab_income = min(taxable_income, 300000)
slab_tax = slab_income * 0
tax += slab_tax
print("0–3L Tax:", slab_tax)

# 3–7L
if taxable_income > 300000:
    slab_income = min(taxable_income, 700000) - 300000
    slab_tax = slab_income * 0.05
    tax += slab_tax
    print("3–7L Tax:", slab_tax)

# 7–10L
if taxable_income > 700000:
    slab_income = min(taxable_income, 1000000) - 700000
    slab_tax = slab_income * 0.10
    tax += slab_tax
    print("7–10L Tax:", slab_tax)

# 10–12L
if taxable_income > 1000000:
    slab_income = min(taxable_income, 1200000) - 1000000
    slab_tax = slab_income * 0.15
    tax += slab_tax
    print("10–12L Tax:", slab_tax)

# 12–15L
if taxable_income > 1200000:
    slab_income = min(taxable_income, 1500000) - 1200000
    slab_tax = slab_income * 0.20
    tax += slab_tax
    print("12–15L Tax:", slab_tax)

# above 15L
if taxable_income > 1500000:
    slab_income = taxable_income - 1500000
    slab_tax = slab_income * 0.30
    tax += slab_tax
    print("Above 15L Tax:", slab_tax)

print("\nTotal Tax:", tax)

effective_tax_rate = (tax / income) * 100 if income > 0 else 0
print("Effective Tax Rate:", round(effective_tax_rate, 2), "%")