import numpy as np

#comparison in numpy
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
print(my_house>=18)
print(my_house<your_house)

#booleans in numpy
print(np.logical_or(my_house>18.5, my_house<10))
print(np.logical_and(my_house<11, your_house<11))

#filtering DataFrames
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)
dr = cars['drives_right'] #Series object

sel = cars[dr==True]
car_maniac = cars[cars['cars_per_cap']>500]

cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

#enumerating
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
for a,b in enumerate(areas) :
    print('room ' + str(a) + ': ' + str(b))



