"""
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""
import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())
print()
print(pd.get_dummies(data['whoAmI']).astype(int))
print()

new_data = pd.DataFrame()

values = data['whoAmI'].unique()
for value in values:
    new_data[value] = (data['whoAmI'] == value).astype(int)

print(new_data.head())
