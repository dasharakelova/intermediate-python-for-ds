#loops with 2D arrays
import numpy as np
array = [[ 74 180]
 [ 74 215]
 [ 72 210]]
for x in np.nditer(array):
    print(x)

#loops with DataFrames
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
for label, row in cars.iterrows(): #функция для итерации по строкам
    print(label)
    print(row)
    print(lab + ': ' + str(row['cars_per_cap'])) #данные только одного столбца для каждой строки

#adding columns
for lab, row in cars.iterrows():
    cars.loc[lab,'COUNTRY'] = row['country'].upper()

cars['COUNTRY'] = cars['country'].apply(str.upper) #то же самое, но используется метод apply, который вызывает функцию на Series
