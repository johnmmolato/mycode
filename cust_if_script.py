#!/usr/bin/env python3
"""JMolato
   Conditional statement challenge"""

def main():
    grade = "Your letter grade is: "
    lettergrade = int(input("What numeric score did you receive? e.i (100, 80, 60)\n"))
    if lettergrade >= 90:
        grade = grade + "A"
    elif lettergrade >= 80:
        grade = grade + "B"
    elif lettergrade >= 70:
        grade = grade + "C"
    elif lettergrade >= 60:
        grade = grade + "D"
    else:
        grade = grade + "F"
    print(grade)

if __name__ == "__main__":
    main()
