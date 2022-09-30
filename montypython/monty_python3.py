#!/usr/bin/python3
"""JMolato
  Conditionals - Life of Brian guessing game without a while True loop."""

def main():

    turn = 0
    answer = " "

    while turn < 3 and answer != "Brian":
        turn += 1     # increase the round counter by 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
        answer = answer.capitalize()

        if answer == "Brian": # logic to check if user gave correct answer
            print("Correct!")
        elif answer == "Shrubbery":
            print("You gave the super secret answer!")
        elif turn == 3:    # logic to ensure round has not yet reached 3
            print("Sorry, the answer was Brian.")
        else:                 # if answer was wrong
            print("Sorry. Try again!")

if __name__ == "__main__":
    main()
