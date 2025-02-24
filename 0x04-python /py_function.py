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
