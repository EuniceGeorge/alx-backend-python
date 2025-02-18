# print("my name is Eunice")
# print("same",
#       "message",
#       "As before")
# print("here", end=" ")
# print("it is....")

# Write a Tipper program where the user enters a restaurant
# bill total. The program should then display two amounts: a
# 15 percent tip and a 20 percent tip.
# import random

#val = random.randint(1, 10)
# val2 = random.randrange(10)
# print (val2)
# print("Your total bill is 400000")
# first = int((400000 * 15) // 100)
# second = int ((400000 * 20 )// 100)

# print("for a 15% discount, you will pay", first)

# print("for a 20% discount, you will pay ", second)

# print("why are you so tall?\n")
# response = ""
# while response != "Because":
#     response = input("Why?\n")
# print("oh,great")

# counter = 0
# while counter != 10:
#     counter +=1
#     print(counter)
    
#working with while conditional loop

#print("Exclusive users only")

#make sure that the user enters something for the username and password
# username=""
# while not username:
#     username = input("username: ")

# password=""
# while not password:
#     password = input("password: ")

# if username == "peace" and password == "001":
#     print("welcome buddy")
# else:
#     print("You are not allowed")
# input("press any key to exit:\n ")
##############################################################
# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low and how many guesses
# or right on the money

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
    


