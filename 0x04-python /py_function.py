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

# 1. Write a Python function to find the maximum of three numbers.
# Click me to see the sample solution

# def max_num(*num):
#     return max(*num)

# num = []
# for i in range(3):
#     number = input("enter number: ")
#     num.append(number)

# maxi= max_num(num)
# print(maxi)



# 2. Write a Python function to sum all the numbers in a list.
# Sample List (8, 2, 3, 0, 7)
# Expected Output : 20
# Click me to see the sample solution

def num_sum(*num):
     return sum(*num)

num = []
maxi=int(input("enter maximum number: "))
for i in range(maxi):
    number =int(input("enter number: "))
    num.append(number)

values = num_sum(num)
print(values)


# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
# Click me to see the sample solution



# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
# Click me to see the sample solution

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
# Click me to see the sample solution

# 6. Write a Python function to check whether a number falls within a given range.
# Click me to see the sample solution

# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
# Click me to see the sample solution

# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
# Click me to see the sample solution

# 9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
# Click me to see the sample solution

# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

# 16. Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
# Click me to see the sample solution