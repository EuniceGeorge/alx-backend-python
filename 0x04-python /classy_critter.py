# Classy Critter
# Demonstrates class attributes and static methods

class Critter(object):
    """A virtual pet"""
    total = 0

    @staticmethod # It is invoked through a class
    def status():
        print("\nThe total number of critters is", Critter.total)
    def __init__(self, name, mood):
        print("A critter has been born!")
        self.name = name
        self.__mood = mood
        Critter.total += 1 #every time a new object is instantiated, the value of the attribute is incremented by 1
    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")
#main

print("Accessing the class attribute Critter.total:", end=" ")
print(Critter.total)
print("\nCreating critters.")
# crit1 = Critter("critter 1")
# crit2 = Critter("critter 2")
# crit3 = Critter("critter 3")
# crit3 = Critter("critter 4")
# crit3 = Critter("critter 5")

crit = Critter("ade", "happy")
crit.talk()
print(crit.__mood)

# Critter.status()
# print("\nAccessing the class attribute through an object:", end= " ")
# print(crit.total) #This line prints the value of the class attribute total (and not an attribute of the object itself).
# input("\n\nPress the enter key to exit.")