# Student Marks Program

name = input("Enter student name: ")

m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))
m4 = int(input("Enter marks in Subject 4: "))
m5 = int(input("Enter marks in Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")