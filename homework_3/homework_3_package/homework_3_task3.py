"""
    Отсортировать словарь по убыванию
"""
from typing import Dict
d = {
    "USA": 100,
    "Japan": 90,
    "France": 25,
    "China": 80,
    "India": 50,
    "Russia": 5
}

def sort_dict_values(d: dict[str,int]) -> Dict[str,int]:
    res_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    return res_dict
print(sort_dict_values(d))

