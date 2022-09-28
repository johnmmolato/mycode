#!/usr/bin/env python3
"""Amazon | JMMolato
   print() - display data to std out"""

# below is a function constaining our code
def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 address:")

    # display the input back to the user.
    print("You told me the IPv4 address is: " + user_input)

# this calls main
main()
