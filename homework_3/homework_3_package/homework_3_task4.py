from typing import Dict

"""
    Просуммировать словарь по годам
"""
monthly_sales = {
    "Jan_2020": 100,
    "Feb_2020": 90,
    "Mar_2020": 15,
    "Jan_2021": 10,
    "Feb_2021": 50,
    "Mar_2022": 5,
    "Sep_2023": 12,
    "Oct_2023": 12
}
def to_yearly_sales(monthly_sales: dict[str, int]) -> Dict[int,int]:
    total_sales = {}
    for key, value in monthly_sales.items():
        year = int(key.split('_')[1])
        if year in total_sales:
            total_sales[year] += value
        else:
            total_sales[year] = value
    return total_sales
print(to_yearly_sales({
    "Jan_2020": 100,
    "Feb_2020": 90,
    "Mar_2020": 15,
    "Jan_2021": 10,
    "Feb_2021": 50,
    "Mar_2022": 5,
    "Sep_2023": 12,
    "Oct_2023": 12
}))

#1. разбить строку и взять оттуда только год, переделать из строки - число
#2.  создать новый словарь
#3 просуммировать по годам
