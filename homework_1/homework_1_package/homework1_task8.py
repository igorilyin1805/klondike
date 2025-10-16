"""
    Напишите функцию, которая вернет true, если список является полностью возрастающим,
    т.е. каждый следующий элемент больше предыдущего
"""

'''
def is_list_growing(lst: list[float]) -> bool:
    for elem in range(len(lst) - 1):
        if lst[elem] < lst[elem + 1]:
            return True
    return False

assert not is_list_growing([1,1,1])
assert not is_list_growing([3,2,1])
assert not is_list_growing([])
assert not  is_list_growing([-1,-2,-3])
assert is_list_growing([-3,2,1])
assert is_list_growing([0,1,2])
print('tests passed')
'''

def is_list_growing(lst: list[float]) -> bool:
    return all(lst[i] < lst[i+1] for i in range(len(lst)-1))




