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
# for i in range(0, 50, 2):
#     print("Hi", end=" ")
#####################################################################

word = "pizza"
print(word[0:5])
print(word[-4:-1])
print(word[-5:5])
# start = None
# while start != "":
#     start = (input("\nStart: "))
#     if start:
#         start = int(start)
#         finish = int(input("Finish: "))
#         print("word[", start, ":", finish, "] is", end=" ")
#         print(word[start:finish])
# input("\n\nPress the enter key to exit.")

#counting game

# start = int(input("Enter the starting value: "))
# end  = int(input("Enter the end value: "))
# count = int(input("Enter the count: "))

# for i in range(start, end, count):
#     print(i,end=" ")
#####################################################################

#print in reverse
message = input("enter a message: ")

backwards_message = message[::-1]
print("Your message backwards:", backwards_message)