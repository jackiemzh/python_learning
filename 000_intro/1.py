# use ** for power calculation
print(100*1.1**7)

mmm = 6
print(type(mmm))


# Create a variable desc

desc = "compound interest"

# Create a variable profitable

profitable= True

doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)


# int(), float() and bool(), str() to convert data types


# Area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)


# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],["bedroom", bed],["bathroom",bath]
         ]

# Print out house
print(house)

# Print out the type of house
print(type(house))


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs

downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]



# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1= areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2

areas_2 = areas_1 + ["garage" , 15.45]


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)


# control + shift + A to run  selected lines

help(round)



# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)


# # # # # # # # # # # # # # # # # # # # # # # # #  methods based on object type
# string methods

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_upper= place.upper()

# Print out place and place_up
print(place)
print(place_upper)

# Print out the number of o's in place
print(place.count("o"))


# list methods, remove(), reverse(), append()

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20))

# Print out how often 9.50 appears in areas
print(areas.count(9.5))


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas = areas.reverse()

# Print out areas
print(areas)

####################################### import

import numpy as np

# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2*math.pi*r

# Calculate A
A = math.pi*(r**2)

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))


# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)



####################################### numpy

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))


# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball, dimention
print(np_baseball.shape)

print(np_baseball[0,1])

# second column
print(np_baseball[:,1])


# Create np_height_in from np_baseball
np_height_in = np.array(np_baseball[:,0])

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))


# --------------------------------
# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))


