"""
    Дан массив цен акций, вывести список, содержащий темпы прироста от периода к периоду.
    Для первого элемента списка выведите значение None. Округлите до целых.
    Например: [100, 150, 300, 400] -> [None, 50%, 100%, 33%]
"""


def get_pct_growth(s: list[float]) -> list[float]:
    lst_percent = [ round((s[p+1] / s[p]-1)*100) for p in range(len(s) - 1) ]
    lst_percent_all = [None] + lst_percent
    lst_percent_all_2 = [f'{p}%' if p is not None else None for p in lst_percent_all]
    return lst_percent_all_2

#непонятный момент с процентами-числами