"""
1. Работать с файлом california_housing_train.csv, который находится в папке sample_data.
Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).


2. Узнать какая максимальная households в зоне минимального значения population.
"""

import pandas as pd

data = pd.read_csv('california_housing_train.csv')

# 1
res_1 = data[(data['population'] >= 0) & (data['population'] <= 500)]['median_house_value'].mean().round(2)
print(res_1)

# res_1 = data[data['population'] <= 500]['median_house_value'].mean() #количество людей не может быть отрицательным
# print(res_1)
print()

# 2
res_2 = data[data['population'] == data['population'].min()][
    'households'].max()
print(res_2)
