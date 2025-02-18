##############################################################
# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player has a limited number of guesses.
# the player know if the guess is too high, too low and how many guesses or right on the money
# If the player fails to guess in time, the program should display an appropriately chastising message.

import random

num = random.randint(1, 100)

count = 0
max_guess = 4
trial = 0

while trial != max_guess:
    trial = int(input("Take a guess: "))
    count += 1

    if trial < num:
        print("lower")
    elif trial > num:
        print("higher")
    else:
        print("good job!!!")

    if count == max_guess:
        print("your limit is exceeded")
        break

print("the number is: ", num)
print("the number of trial is: ", count)
    


