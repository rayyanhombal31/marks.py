score = float(input("Enter marks: "))
passing_score = 40

if score >= passing_score:
    print("Pass")
else:
<<<<<<< Updated upstream
    print("Fail")
=======
    print("Result: FAIL")
    
    # Check Pass / Fail and assign Grade
if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    print("Result: PASS")
    
    if average >= 85:
        grade = "Distinction (A+)"
    elif average >= 75:
        grade = "First Class (A)"
    elif average >= 60:
        grade = "Second Class (B)"
    elif average >= 50:
        grade = "Pass Class (C)"
    else:
        grade = "Pass (D)"
        
    print("Grade:", grade)
else:
    print("Result: FAIL")
    print("Grade: No Grade (F)")
>>>>>>> Stashed changes
