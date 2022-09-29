#!/usr/bin/env python3
"""JMolato
   Lab challenge creating lists"""

def main():
    import random
    wordbank= ["indentation", "spaces"]
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris",
            "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey",
            "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]
    wordbank.append(4)
    num = input("Pick a number between 0 and 18\n")
    num = int(num)
    student_name = tlgstudents[num:num+1]
    rand_student = random.choice(tlgstudents)
    print("{} always uses {} {} to indent.".format(("".join(student_name)), wordbank[2], wordbank[1]))
    print("{} always uses {} {} to indent.".format(("".join(rand_student)), wordbank[2], wordbank[1]))

main()
