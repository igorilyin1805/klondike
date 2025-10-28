#Соединить два словаря
from typing import Dict


# def concat_dicts(developed_markets:dict[str,int],emerging_markets:dict[str,int]) -> Dict[str,int]:
#     return {keys: values for dictionary in [developed_markets,emerging_markets] for keys, values in dictionary.items()}
# print(concat_dicts({
#         "USA": 100,
#         "Japan": 90,
#         "France": 25
#     },{
#         "China": 80,
#         "India": 50,
#         "Russia": 5
#     }))


# из книги
def concat_dicts(developed_markets: dict[str, int], emerging_markets: dict[str, int]) -> Dict[str, int]:
    new_dict = developed_markets.copy()
    new_dict.update(emerging_markets)
    return new_dict
print(concat_dicts({
    "USA": 100,
    "Japan": 90,
    "France": 25
},{
    "China": 80,
    "India": 50,
    "Russia": 5
}))
