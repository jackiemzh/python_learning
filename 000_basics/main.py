# Example Python script
# freeCodeCamp
# https://www.youtube.com/watch?v=rfscVS0vtbw&t=6013s

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# TABLE OF CONTENTS -----
# 01 PRINT
# 02 STRING
# 03 NUMBERS
# 04 USER INPUT
# 05 Calculater
# 06 mad libs
# 07 lists
# 08 lists function
# 09 tuples
# 10 functions





# 01 PRINT -----

character_name = "JOHN"
character_age = "40"
IS_MALE = True

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")


# 02 STRING -----

# seperate lines
print("LINE 1 \nLINE 2")

# print quation mark
phase = "LINE 1\"LINE 2"
print(phase)

# upper/lower case
phase = "line 1 \nline 2"
print(phase.upper())

# isupper()
phase = "line 1 \nline 2"
print(phase.isupper())
print(phase.upper().isupper())

# length
phase = "ABCDE XYZ"
print(len(phase))

# index
phase = "ABCDE XYZ"
print(phase[0])

print(phase.index("A"))
print(phase.index("AB"))

# replace
print(phase.replace("AB","NM"))


# 03 NUMBERS -----

# remainder
my_num = 5
print(my_num % 3)

# convert to string
print(str(my_num ) + " is my lucky number.")

# abs
print(abs(-10.5))

# power
print(pow(3,2))

# max, min, round

#
from math import *

# floor
print(floor(9.6))

# ceil
print(ceil(9.6))

# sqrt
print(sqrt(81))

# 04 USER INPUT -----

name = input("Enter you name: ")
age = input("Enter you age: ")
print("Hello " + name + "! You are " + age + ".")

# 05 Calculater -----

number1 = input("Enter your first number:")
number2 = input("Enter your second number:")
results = int(number1) + float(number2)
print("The sum is: "+ str(results))


# 06 mad libs -----

colour = input("Enter your colour:")
plural_noun = input("Enter your noun:")

print("Roses are " + colour )
print(plural_noun +" are blue")


# 07 lists -----

friends = ["Steve", "Jenny", "Tom"]
print(friends[:-1])

# 08 lists function -----

friends = ["Steve", "Jenny", "Tom"]
number = [8, 10, 52]

friends.extend(number)
print(friends)

# add at the end of the list
friends.append("Cidy")
print(friends)

# insert
friends.insert(1, "Apple")
print(friends)

# remove
friends.remove( "Apple")
print(friends)

# remove the last element
friends.pop()
print(friends)

# check index
print(friends.index("Steve"))

# check counts
print(friends.count("Steve"))

# sort order
friends = ["Steve", "Jenny", "Tom"]
friends.sort()
print(friends)

# reverse order (from the largest to smallest)
number.reverse()
print(number)


# copy
friends2 =  friends.copy()
print(friends2)


# clear all
friends.clear()
print(friends)


# 09 Tuples -----
# container which stores different values
# can't change its element

coordinates = (7,3)
coordinates[0] = 10
print(coordinates[0])

coordinates = [(7,3),(10,3),(9,8)]
coordinates[0] = 10
print(coordinates[0])


# 10 functions -----


