# text_file = open("text.txt", "r")
# value = text_file.read(5)
# print(value)
# text_file.close()
# text_file = open("text.txt", "r")
# value = text_file.readline()
# value1 = text_file.readline()
# value2 = text_file.readline()

# print(value)
# print(value1)
# print(value2)
# text_file.close()

# text_file = open("text.txt", "r")
# for line in text_file:
#     print(line)
# text_file.close()
#########################################################################
print("Reading a text file with the read() method.")
text_file = open("write_it.txt", "r")
for line in text_file:
    print(line)
text_file.close()

#####################################################################################################
# so by default, if a mode is not created, it redas a file
# text_file = open("text.txt")
# value = text_file.read()
# print(value)
# text_file.close()
###################################################################

# Write It
# Demonstrates writing to a text file
print("Creating a text file with the write() method.")
text_file = open("write_it.txt", "w")
lines = ["Line 1\n",
"This is line 2\n",
"That makes this line 3\n"]
text_file.writelines(lines)
text_file.close()

