
##############################################################
# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low and how many guesses
# or right on the money

def guess_number(num):
    """Ask for a number within a range."""
    guess_comp = 1
    trial = int(input("take a guess: \n"))

    while trial != num:

        if trial < num:
            print("Your guess is lower\n")
        elif trial > num:
            print("Your guess is higher\n")
        else:
            print("Good job!!!\n")

        trial = int(input("guess the number: \n"))
        guess_comp+=1

    print("Yeah!!!!!!! you guessed right, the number is ", num ,end="")
    print("\n")
    print("your trial is: ", guess_comp)

    return trial

#main
import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")
num = random.randint(1, 100)

response = guess_number(num)
print("\n")

