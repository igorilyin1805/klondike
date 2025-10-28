from homework_3.homework_3_package.homework_3_task1 import two_lists_to_dict
from homework_3.homework_3_package.homework_3_task2 import concat_dicts
from homework_3.homework_3_package.homework_3_task3 import sort_dict_values
from homework_3.homework_3_package.homework_3_task4 import to_yearly_sales
from homework_3.homework_3_package.homework_3_task6 import get_distinct_categories


def test_to_lists_to_dict():
    """
        Соединить два списка в словарь
    """
    keys = ["USA", "Russia", "France"]
    income = [100, 10, 25]
    assert two_lists_to_dict(keys, income) == {
        "USA": 100,
        "Russia": 10,
        "France": 25
    }


print('Tests passed')


def test_merge_two_dicts():
    """
        Соединить два словаря
    """
    developed_markets = {
        "USA": 100,
        "Japan": 90,
        "France": 25
    }
    emerging_markets = {
        "China": 80,
        "India": 50,
        "Russia": 5
    }
    assert concat_dicts(developed_markets, emerging_markets) == {
        "USA": 100,
        "Japan": 90,
        "France": 25,
        "China": 80,
        "India": 50,
        "Russia": 5
    }


print('Tests passed')


def test_sort_dict_values():
    """
        Отсортировать словарь по убыванию
    """


d = {
    "USA": 100,
    "Japan": 90,
    "France": 25,
    "China": 80,
    "India": 50,
    "Russia": 5
}
assert sort_dict_values(d) == {
    "USA": 100,
    "Japan": 90,
    "China": 80,
    "India": 50,
    "France": 25,
    "Russia": 5
}

print('Tests passed')

def test_sum_value_of_the_same_key_kinds():
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
    assert to_yearly_sales(monthly_sales) == {
        "2020": 205,
        "2021": 60,
        "2022": 5,
        "2023": 24
    }

print('Tests passed')

def test_get_distinct_categories():
    """
        Вернуть множество уникальных категорий товаров
        Воспользоваться set comprehension (по аналогии с list/dict comprehension)
    """
    assert get_distinct_categories(_sales_data) == {
        "dairy products", "bakery", "drinks"}
print('Tests passed')



