"""
    Вернуть множество уникальных категорий товаров
    Воспользоваться set comprehension (по аналогии с list/dict comprehension)
"""
_sales_data = [
    {
        "category": "dairy products",
        "product": "milk",
        "price_rub": 100,
        "count": 1
    },
    {
        "category": "dairy products",
        "product": "cream",
        "price_rub": 290,
        "count": 1
    },
    {
        "category": "dairy products",
        "product": "yogurt",
        "price_rub": 50,
        "count": 1
    },
    {
        "category": "bakery",
        "product": "white_bread",
        "price_rub": 60,
        "count": 1
    },
    {
        "category": "bakery",
        "product": "black_bread",
        "price_rub": 55,
        "count": 1
    },
    {
        "category": "drinks",
        "product": "water",
        "price_rub": 90,
        "count": 1
    },
    {
        "category": "drinks",
        "product": "apple_juice",
        "price_rub": 300,
        "count": 1
    }
]

#нам нужно из списка, который состоит из словарей, достать уникальные данные по ключу 'category'
# само множество уже фильтрует и оставляет уникальные значения
# что нам даст генератор множества - он создаст список значений, где ключ = 'category'


def get_distinct_categories(_sales_data:list) -> set:

    return {dictionary['category'] for dictionary in _sales_data}
print(get_distinct_categories(_sales_data))