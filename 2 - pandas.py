import pandas as pd
# # Lists --> Dictionary --> DataFrame
# names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
# dr =  [True, False, False, False, True, True, True]
# cpc = [809, 731, 588, 18, 200, 70, 45]
#
# my_dict = {'country' : names, 'drives_right' : dr, 'cars_per_cap' : cpc}
#
# cars = pd.DataFrame(my_dict)
#
# # Setting row indexing
# row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
# cars.index = row_labels #вместо автоматической нумерации строк

# CSV --> DataFrame
cars = pd.read_csv('cars.csv', index_col=0) #нулевой столбец берется за лейблы

# Selecting with square brackets
print(cars['country']) # the output object would be a Pandas Series
print(cars[['country']])# the output object would be a Pandas DataFrame
print(cars[['country', 'drives_right']])# Series так не может!
print(cars[0:3])

# Selecting with loc and iloc
print(cars.loc[['JAP', 'AUS']])# by label
print(cars.iloc[2])# by index
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])# first specify the rows, then the columns
print(cars.loc[:, 'drives_right']) #columns only
print(cars.loc[[:, 'drives_right']])# same but with DataFrame