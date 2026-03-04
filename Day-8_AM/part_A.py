# admission screening tool

entrance_score = float(input("Enter a score from 0 to 100: "))
gpa = float(input("Enter a GPA from 0 to 10: "))
has_recommendation = input("Does this person have a recommendation? (yes/no): ")
category = input("Category (general/obc/sc_st): ")
extracurricular_score = float(input("Enter a score from 0 to 10: "))

# scholarship rule
if entrance_score >= 95:
    print("ADMITTED (Scholarship)")
    exit()

# category cutoff
if category == "general":
    cutoff = 75
elif category == "obc":
    cutoff = 65
else:
    cutoff = 55

# bonus points
bonus_points = 0

if has_recommendation == "yes":
    bonus_points += 5

if extracurricular_score > 8:
    bonus_points += 3

effective_score = entrance_score + bonus_points

print("Effective Score:", effective_score)

# final decision
if gpa < 7.0:
    print("REJECTED: GPA below requirement")

elif effective_score >= cutoff:
    print("ADMITTED (Regular)")

elif effective_score >= cutoff - 5:
    print("WAITLISTED")

else:
    print("REJECTED: Score below cutoff")