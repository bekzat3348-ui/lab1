
score = float(input("Enter score (0-100): "))


if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100!")
else:
    
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
    print(f"Your grade is: {grade}")
