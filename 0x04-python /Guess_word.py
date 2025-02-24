
#  Create a game where the computer picks a random word and the player has to guess that word. 
# The computer tells the player how many letters are in the word. 
# Then the player gets five chances to ask if a letter is in the word. 
# The computer can only respond with “yes” or “no”. 
# Then, the player must guess the word.

# A simple algorithm to solve the problem

#FUNCTION start_game:
#     // Initialize game
#     word_list = [...list of possible words...]
#     secret_word = randomly select a word from word_list
#     chances_remaining = 5
#     letters_guessed = empty list

#     // Tell player the word length
#     Display "The word has " + length of secret_word + " letters."

#     // Letter guessing phase
#     WHILE chances_remaining > 0:
#         Display "You have " + chances_remaining + " chances remaining."
#         Ask player "What letter would you like to check?"
#         letter = get player's input
        
#         IF letter is in letters_guessed:
#             Display "You already guessed that letter! Try another one."
#             CONTINUE
            
#         Add letter to letters_guessed
#         chances_remaining = chances_remaining - 1
        
#         IF letter is in secret_word:
#             Display "Yes"
#         ELSE:
#             Display "No"

#     Final guess phase
#     Display "Now make your guess! What's the word?"
#     player_guess = get player's input
    
#     IF player_guess equals secret_word:
#         Display "Congratulations! You won!"
#     ELSE:
#         Display "Sorry, the word was: " + secret_word


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

