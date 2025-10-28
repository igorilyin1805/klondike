
#Соединить два списка в словарь

from typing import Dict

# def two_lists_to_dict(keys: list[str],income:list[int]) -> Dict[str,int]:
#     new_lst = list(zip(keys,income))
#     return {k:v for k,v in new_lst}
# print(two_lists_to_dict(["USA", "Russia", "France"],[100, 10, 25]))


#вариант из книги

def two_lists_to_dict(keys: list[str],income:list[int]) -> Dict[str,int]:
    return dict(zip(keys, income))
print(two_lists_to_dict(["USA", "Russia", "France"],[100, 10, 25]))



