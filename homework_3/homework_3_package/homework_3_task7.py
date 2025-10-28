"""
    Показать сумму покупок по категориям. Отсортировать категории по возрастанию суммы
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

def get_sorted_category_sum(_sales_data: list):
    category_sum = {}
    for dictionary in _sales_data:
        category = dictionary['category']
        total_sum = dictionary['price_rub'] * dictionary['count']
        if category in category_sum:
            category_sum[category]+=total_sum
        else:
            category_sum[category] = total_sum
    return category_sum
print(get_sorted_category_sum(_sales_data))


"""
    Показать сумму покупок по категориям. Отсортировать категории по возрастанию суммы
"""
#[("bakery", 115),("drinks", 390),("dairy products", 440)]

