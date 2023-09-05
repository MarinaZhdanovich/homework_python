"""
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]

Вывод: [1, 9, 13, 14, 19]
"""


def find_index(lst, min_element, max_element):
    result = []
    for i in range(len(lst)):
        if min_element <= lst[i] <= max_element:
            result.append(i)
    return result


lst_el = list(map(int, input("Введите элементы по одной цифре через пробел: ").split()))
min_el = int(input("Введите минимальный элемент: "))
max_el = int(input("Введите максимальный элемент: "))

# lst_el = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_el = 7
# max_el = 10

final_result = find_index(lst_el, min_el, max_el)
print(final_result)
