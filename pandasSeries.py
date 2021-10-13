import pandas as pd

grades = pd.Series([87, 100, 94])

print(grades)

grades2 = pd.Series(98.6, range(3))

print(grades2)

print(grades[0])

# decribe() shows you all of the aggregate functions of the array
print(grades.describe())

# string indexing to label the indexes
grades = pd.Series([87, 100, 94], index = ['Wally', 'Eva', 'Sam'])

# dictionary to pandas series
# in a dictionary, the keys become the indexes
grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})

print(grades)

# for custom indexes, you do not need to know the number index, just the name
print(grades['Eva'])

# . notation also works for referencing custom indexes because the indexes become attributes of the object
print(grades.Wally)

# other functions with . notation
print(grades.dtype)
print(grades.values) # returns a numpy array


# series of string values
hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

# string methods
print(hardware.str.contains('a')) # returns a boolean array (True/False)

print(hardware.str.upper())

