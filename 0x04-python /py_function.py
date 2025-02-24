# # positional parameters
# #Using Positional Parameters and Positional Arguments
# def birthday1(name, age):
#     print("Happy birthday,", name, "!", " I hear you're", age, "today.\n")

# # parameters with default values
# #Using Positional Parameters and Keyword Arguments
# def birthday2(name = "katherine", age = 1):
#     print("Happy birthday,", name, "!", " I hear you're", age, "today.\n")

# birthday1("Jackson", 1)
# birthday1(1, "Jackson") #this is wrong
# birthday1(name = "Jackson", age = 1)
# birthday1(age = 1, name = "Jackson")

# print("\n")
# print("""This is 
#       a new 
#       line""")
# print("\n")

# birthday2()
# birthday2(name = "Katherine")
# birthday2(age = 12)
# birthday2(name = "Katherine", age = 12)
# birthday2("Katherine", 12)

# input("\n\nPress the enter key to exit.")

# 2. Modify the Guess My Number chapter project from Chapter 3 by reusing the function ask_number().
# 3. Modify the new version of Guess My Number you created in the last challenge
# so that the program’s code is in a function called main(). Don’t forget to call main() 
# so that you can play the game.

def main(comp_guess):
    chances = 5
    guess = ""

    #Tell player the word length
    comp_guess_len = len(comp_guess)
    print("The word has ", comp_guess_len,  " letters.", end=" \n")

#Letter guessing phase
    while chances > 0:
        print("you have ", chances, " chances left")
        check = input("what letter will you love to check: ")
    
        if check in guess:
            print("Already checked that letter")
            continue

        guess += check
        chances = chances - 1

        if check in comp_guess:
         print("yes")
        else:
            print("no")
    return guess

import random

# Initialize game
word = ("shoe", "bag", "chair", "fan")
comp_guess = random.choice(word)

value = main(comp_guess)
#Final guess phase
print("Now guess, what's the word? ", end=" \n")
player_guess = input("enter you guess: ")

if player_guess == comp_guess:
    print("congratulation!!!")
else:
    print("sorry, the word was", comp_guess)
