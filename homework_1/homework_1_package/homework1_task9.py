"""
    Дан список целых чисел и определенное заданное число. Найти все пары из списка,
    сумма которых равна этому числу.
    Верните из функции список кортежей.
    Например: get_pairs_number([1, 2, 4, 3, 5, 2], 7) -> [(4,3), (5,2)]
"""

'''
def get_pairs_number(lst: list[int], n) -> list[tuple]:
    if not lst or len(lst) < 2:
        return []
    new_lst = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == n:
                new_lst.append((lst[i], lst[j]))
    return new_lst
'''
def get_pairs_number(lst: list[int], n) -> list[tuple]:
    res = set() #множество - уникальные пары, удаление дубликатов
    for i,x in enumerate(lst): #x = 4
        for j,y in enumerate(lst): # y = 4
            if x + y == n and i != j: #условие добавления - разные индексы
                res.add((x,y) if x > y else (y,x)) #сортировка - большее число впереди
                # x = 4, y = 3 4 > 3 -> да -> (4,3)
                # x = 3, y = 4 3 > 4 -> нет -> (4,3)
    return list(res)









