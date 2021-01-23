# Example Python script
# freeCodeCamp
# https://www.youtube.com/watch?v=rfscVS0vtbw&t=6013s

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

'''
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
# 11 return
# 12 if statement
# 13 if statement & comparisons
# 14 Building a better calculator
# 15 Dictionary
# 16 While loop
# 17 Building a guessing game
# 18 for
# 19 exponent function
# 20 2D lists & nested loops
# 21 comments
# 22 try except
# 23 reading files
# 24 writing files
# 25 Modules & pip
# 26 Classes & objects
# 27 building a multiple choice quiz
# 28 inheritance
'''



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

 def say_hi(name, age):
     print("Hello! " + name + ". You are " + str(age) +".")


say_hi(name="Yoyo", age=5)


# 11 return -----

def cube(num):
    return num*num*num

result = cube(8)
print(result)


# 12 if statement -----

is_male = True
is_tall = False

# and, or, not

if is_male and is_tall:
    print("tall male found")
elif is_male and not(is_tall):
    print("short male found")
else:
    print("no male found")

# 13 if statement & comparisons -----

def max_num(num1, num2, num3):
    if num1>= num2 and num1>=num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else:
        return num3


print(max_num(1,20,8))


# 14 Building a better calculator -----

num1 = float(input("Enter your first number:"))
op = input("Enter your operator:")
num2 = float(input("Enter your second number:"))

if op== "+":
    print(num1+num2)
elif op=="-":
    print(num1 - num2)
elif op=="/":
    print(num1 / num2)
elif op=="*":
    print(num1 * num2)
else:
    print("invalid operator")

# 15 Dictionary -----
# unique key:value

month_conversion = {"Jan":"January",
                    "Feb":"February",
                    "Mar":"March",
                    4:"April"}

print(month_conversion.get("Mar"))
print(month_conversion.get("Lv","Not a valid key"))


# 16 While loop -----

i=1
while i<10:
    print(i)
    i += 1

# 17 Building a guessing game  -----

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count <= guess_limit:
        guess_count += 1
        guess = input("Enter your guess:")
    else:
        out_of_guesses =True

if  out_of_guesses :
    print("No more chances!")
else:
    print("Correct! You guessed " + str(guess_count)+ " times!")


# 18 for -----

for letter in "ABCDEFG":
    print(letter)

friends2 = ['kim',"pop","rada"]
for f in friends2:
    print(f)

for ii in range(10):
    print(ii)

for ii in range(len(friends2)):
    print(friends2[ii])


# 19 exponent function -----

# 2^3
print(2**3)

#
def raise_to_power(base_number,power_number):

    if power_number == 1:
        result = base_number
    else:
        result= 1
        for index in range(power_number):
            result = result* base_number
    return result

print(raise_to_power(3,4))


# 20 2D lists & nested loops -----

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

# [row index] [column index]
print(number_grid[0][2])


for row in number_grid:
    print(row)
    for col in row:
        print(col)


# 21 build a translator -----

def my_translate(phase):
    translation = ""
    for letter in phase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(my_translate("A1234"))


# 21 comments -----

''' 
long comments
long comments
'''



# 22 try except (catching errors) -----

try:
    value =  10/0
    number0 =  int(input("Enter your number:"))
    print(number0)
except ZeroDivisionError as ERR:
    print(ERR)
except ValueError:
    print("invalid input")


# 23 reading files -----
# r (read), w (write), a (append), r+ (read & write)

employee_file = open("/Users/jackiemzh/Documents/DS/python_learning/000_basics/txt/scratch.txt", "r")

print(employee_file.readable())

# save as arrary
em_arrary = employee_file.readlines()
print(em_arrary)
print(em_arrary[1])

employee_file.close()


# 24 writing files -----


employee_file = open("/Users/jackiemzh/Documents/DS/python_learning/000_basics/txt/scratch.txt", "a")
employee_file.write("Tom - HR")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

employee_file0 = open("/Users/jackiemzh/Documents/DS/python_learning/000_basics/txt/scratch.txt", "r")
print(employee_file0.readlines())

# overwrite
employee_file1 = open("/Users/jackiemzh/Documents/DS/python_learning/000_basics/txt/scratch1.txt", "w")
employee_file1.write("Kelly - Customer Service")
employee_file1.close()


employee_file2 = open("/Users/jackiemzh/Documents/DS/python_learning/000_basics/txt/index.html", "w")
employee_file2.write("<p>This is HTML </p>")
employee_file2.close()



# 25 Modules & pip -----
# https://docs.python.org/3/py-modindex.html
# source script

# current directory
import os
print(os.getcwd())

# change directory
os.chdir("/Users/jackiemzh/Documents/DS/python_learning/000_basics/source_funcs")

#import useful_tools.py
import useful_tools

# roll_dice is a function within useful_tools
print(useful_tool.roll_dice(10))



# use pip (package manager) to install python docx
# Terminial
# pip3 --version
# pip3 install python-docx
# pip3 uninstall python-docx

#import docx
#docx.


# 26 Classes & objects -----

# from student file, import Student class
import sys
#sys.path.insert(1, '/Users/jackiemzh/Documents/data_science/python_learning/python_learning/000_basics/student.py')
sys.path.append( '/Users/jackiemzh/Documents/data_science/python_learning/python_learning/000_basics/')
from student import Student


student1= Student("Jim", "Maths", 4.1 ,False)
student2= Student("Pola", "Art", 3.6 ,True)

print(student1)
print(student1.name)


# 28 inheritance -----
# copy attributes of one class to another

sys.path.append( '/Users/jackiemzh/Documents/data_science/python_learning/python_learning/000_basics/')
from Chef import chef

myChef = chef()
myChef.make_special_dis()

from CC import chinesechef

chinesechef.make_s# Example Python script
# freeCodeCamp
# https://www.youtube.com/watch?v=rfscVS0vtbw&t=6013s

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

'''
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
# 11 return
# 12 if statement
# 13 if statement & comparisons
# 14 Building a better calculator
# 15 Dictionary
# 16 While loop
# 17 Building a guessing game
# 18 for
# 19 exponent function
# 20 2D lists & nested loops
# 21 comments
# 22 try except
# 23 reading files
# 24 writing files
# 25 Modules & pip
# 26 Classes & objects
# 27 building a multiple choice quiz
# 28 inheritance
'''



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

 def say_hi(name, age):
     print("Hello! " + name + ". You are " + str(age) +".")


say_hi(name="Yoyo", age=5)


# 11 return -----

def cube(num):
    return num*num*num

result = cube(8)
print(result)


# 12 if statement -----

is_male = True
is_tall = False

# and, or, not

if is_male and is_tall:
    print("tall male found")
elif is_male and not(is_tall):
    print("short male found")
else:
    print("no male found")

# 13 if statement & comparisons -----

def max_num(num1, num2, num3):
    if num1>= num2 and num1>=num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else:
        return num3


print(max_num(1,20,8))


# 14 Building a better calculator -----

num1 = float(input("Enter your first number:"))
op = input("Enter your operator:")
num2 = float(input("Enter your second number:"))

if op== "+":
    print(num1+num2)
elif op=="-":
    print(num1 - num2)
elif op=="/":
    print(num1 / num2)
elif op=="*":
    print(num1 * num2)
else:
    print("invalid operator")

# 15 Dictionary -----
# unique key:value

month_conversion = {"Jan":"January",
                    "Feb":"February",
                    "Mar":"March",
                    4:"April"}

print(month_conversion.get("Mar"))
print(month_conversion.get("Lv","Not a valid key"))


# 16 While loop -----

i=1
while i<10:
    print(i)
    i += 1

# 17 Building a guessing game  -----

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count <= guess_limit:
        guess_count += 1
        guess = input("Enter your guess:")
    else:
        out_of_guesses =True

if  out_of_guesses :
    print("No more chances!")
else:
    print("Correct! You guessed " + str(guess_count)+ " times!")


# 18 for -----

for letter in "ABCDEFG":
    print(letter)

friends2 = ['kim',"pop","rada"]
for f in friends2:
    print(f)

for ii in range(10):
    print(ii)

for ii in range(len(friends2)):
    print(friends2[ii])


# 19 exponent function -----

# 2^3
print(2**3)

#
def raise_to_power(base_number,power_number):

    if power_number == 1:
        result = base_number
    else:
        result= 1
        for index in range(power_number):
            result = result* base_number
    return result

print(raise_to_power(3,4))


# 20 2D lists & nested loops -----

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

# [row index] [column index]
print(number_grid[0][2])


for row in number_grid:
    print(row)
    for col in row:
        print(col)


# 21 build a translator -----

def my_translate(phase):
    translation = ""
    for letter in phase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(my_translate("A1234"))


# 21 comments -----

''' 
long comments
long comments
'''



# 22 try except (catching errors) -----

try:
    value =  10/0
    number0 =  int(input("Enter your number:"))
    print(number0)
except ZeroDivisionError as ERR:
    print(ERR)
except ValueError:
    print("invalid input")


# 23 reading files -----
# r (read), w (write), a (append), r+ (read & write)

employee_file = open("/Users/jackiemzh/Documents/DS/python_learning/000_basics/txt/scratch.txt", "r")

print(employee_file.readable())

# save as arrary
em_arrary = employee_file.readlines()
print(em_arrary)
print(em_arrary[1])

employee_file.close()


# 24 writing files -----


employee_file = open("/Users/jackiemzh/Documents/DS/python_learning/000_basics/txt/scratch.txt", "a")
employee_file.write("Tom - HR")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

employee_file0 = open("/Users/jackiemzh/Documents/DS/python_learning/000_basics/txt/scratch.txt", "r")
print(employee_file0.readlines())

# overwrite
employee_file1 = open("/Users/jackiemzh/Documents/DS/python_learning/000_basics/txt/scratch1.txt", "w")
employee_file1.write("Kelly - Customer Service")
employee_file1.close()


employee_file2 = open("/Users/jackiemzh/Documents/DS/python_learning/000_basics/txt/index.html", "w")
employee_file2.write("<p>This is HTML </p>")
employee_file2.close()



# 25 Modules & pip -----
# https://docs.python.org/3/py-modindex.html
# source script

# current directory
import os
print(os.getcwd())

# change directory
os.chdir("/Users/jackiemzh/Documents/DS/python_learning/000_basics/source_funcs")

#import useful_tools.py
import useful_tools

# roll_dice is a function within useful_tools
print(useful_tool.roll_dice(10))



# use pip (package manager) to install python docx
# Terminial
# pip3 --version
# pip3 install python-docx
# pip3 uninstall python-docx

#import docx
#docx.


# 26 Classes & objects -----

# from student file, import Student class
import sys
#sys.path.insert(1, '/Users/jackiemzh/Documents/data_science/python_learning/python_learning/000_basics/student.py')
sys.path.append( '/Users/jackiemzh/Documents/data_science/python_learning/python_learning/000_basics/')
from student import Student


student1= Student("Jim", "Maths", 4.1 ,False)
student2= Student("Pola", "Art", 3.6 ,True)

print(student1)
print(student1.name)


# 28 inheritance -----
# copy attributes of one class to another

sys.path.append( '/Users/jackiemzh/Documents/data_science/python_learning/python_learning/000_basics/')
from Chef import chef

myChef = chef()
myChef.make_special_dis()

from CC import chinesechef

myCC = chinesechef()
myCC.make_rice()
myCC.make_special_dis()









