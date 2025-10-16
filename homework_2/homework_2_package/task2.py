"""
    Дан список, содержащий нули. Вернуть список, где все нули сдвинуты вправо,
    сохранив порядок исходного списка:
    move_zeros([1, 0, 0, 2, 3, 0, 1]) -> [1, 2, 3, 1, 0, 0, 0]

    Решить в двух вариантах:
    - функция принимаем список и возвращает НОВЫЙ список
    - функция изменяет список, который был передан в аргументе функции
    (функция ничего не возвращает)
"""

#new lst

def move_zeros(lst: list[float]) -> list:
    lst_no_zero = [i for i in lst if i > 0]
    lst_zero = [i for i in lst if i == 0]
    new_lst = lst_no_zero + lst_zero
    return new_lst


#change lst

def move_zeros(lst: list[float]) -> list:
    lst_no_zero = [i for i in lst if i > 0]
    lst_zero = [i for i in lst if i == 0]
    lst.clear()
    lst.extend(lst_no_zero)
    lst.extend(lst_zero)
    return lst





