import pandas as pd

grades_dict = {'Wally': [87,96,70],
                'Eva': [100,87,90],
                'Sam': [94,77,90],
                'Katie': [100,81,82],
                'Bob': [83,65,85]}

# when you make a data frame from a dictionary, the keys become the columns and the values become the row
grades = pd.DataFrame(grades_dict)

# create custom indexes for rows
grades.index = ['Test1', 'Test2', 'Test3']

print(grades)

# transpose creates a view with flipped rows and columns
print(grades.T)

# if you were to extract one column from the data frame, a pandas Series (one dimensional array) is returned
print(grades['Eva'])
print(grades.Sam)

# loc method (for extracting rows - still returns a Series)
print(grades.loc['Test2'])
# iloc is integer loc (0 based number indexing)
print(grades.iloc[1])

# indexing 
# ':' means consecutive rows or columns; [','] means nonconsecutive rows or columns
# consecutive rows
print(grades.loc['Test1':'Test3']) # in loc method, UPPER BOUND IS INCLUDED
print(grades.iloc[0:3]) # in iloc method, upper bound is NOT included
# nonconsecutive rows
print(grades.loc[['Test1','Test3']]) # need extra brackets to indicate rows, not rows and columns (location of value)
print(grades.iloc[[0,2]])

# View only Eva and Katie's grades for Test1 and Test2
print(grades.loc['Test1':'Test2',['Katie','Eva']])
# View only Sam through Bob's grades for Test1 and Test3
print(grades.loc[['Test1','Test3'],'Sam':'Bob'])

# Boolean indexing
grades_A = grades[grades >= 90]
print(grades_A)
# NaN stands for Not a Number (NULL value) - pandas ignores these NULL values

grades_B = grades[(grades >= 80) & (grades < 90)] # for 'and', you must use '&'
print(grades_B)

grades_A_or_B = [(grades >= 90) | (grades >= 80)] # for 'or', you must use '|'
print(grades_A_or_B) # returns Boolean

# describe() for data frames returns aggregate data by column
# less decimals (set precision)
pd.set_option('precision',2)
print(grades.describe())
# by row (transposed)
print(grades.T.describe())

# sorting 
# by row index (default)
print(grades.sort_index(ascending=False)) # descending order
# by column index
print(grades.sort_index(axis=1)) # columns in alphabetical order
print(grades.sort_index(axis=1, ascending=False)) # reverse alphabetical order
# by values
print(grades.sort_values(by='Test1', axis=1, ascending=False))
print(grades.T.sort_values(by='Test1', ascending=False))
# sort just Test1 values (do not show other Tests)
print(grades.loc['Test1'].sort_values(ascending=False))