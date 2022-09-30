#!/usr/bin/env python3
"""JMolato
   While loop with conditional"""

def main():
    # integer turn initiated to 0
    turn = 0
    # sets up an infinite loop condition
    while True:
        # increase the turn counter
        turn = turn + 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        # string answer collected from the user
        answer = input("Your guess--> ")
        # check if user gave the correct answer
        if answer == "Brian":
            print("Correct")
            break
        elif turn == 3:
            print("Sorry, the answer was Brian.")
            break
        else:
            print("Sorry! Try again!")

if __name__ == "__main__":
    main()
