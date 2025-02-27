# #we want to create a class and
#  #create an instance of the class

# class Critter(object): #you create a class(blueprint) using an object
#     """ define a method"""
#     def talk(self): #define a method
#         print("Hi, print the word !!!!!!!!!!!!")

# #main
# crit = Critter() #create an instance of a class

# crit.talk() #invoke the method created

######################################################################################

# working with constructors
# A constructor is always automatically invoked after a new object is created

# class Critter(object):
#     """create a constructor"""
#     def __init__(self):
#         print("I'm the new constructor")

#     def talk(self):
#         print("I am the methed created")

# #main
# crit_1 = Critter() # Automatically, the constructor is invoked in the new instance

# print("\n")
# print("Now without the new method\n")
# crit_2 = Critter()
# crit_2.talk()

###########################################################################################

# creating Attributes for the class

class Critter(object):
    """create a constructor"""
    def __init__(self, name, age):
        print("I'm the new constructor")
        self.name = name
        self.age = age

    def __str__(self): # This special function defines the way the object will be printed
        rep = "Critter object name and age are: \n", self.name, self.age, "\n"
        return rep

    def talk(self):
        print("Hi. I'm", self.name, "and i'm ", self.age, "years olds", "\n")

#main
crit_1 = Critter("Tola", 12) # Automatically, the constructor is invoked in the new instance
crit_1.talk()
print(crit_1)

print("\n")
print("Now without the new method\n")
crit_2 = Critter("Bisi", 15)
crit_2.talk()
print(crit_2)