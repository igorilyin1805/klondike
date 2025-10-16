from homework_2.homework_2_package.task1 import get_views_count
from homework_2.homework_2_package.task2 import move_zeros
from homework_2.homework_2_package.task3 import clean_name
from homework_2.homework_2_package.task4 import get_pct_growth
def test_get_views_count():
    assert get_views_count(-1) == 'Введите положительное число'
    assert get_views_count(0) == '0 просмотров'
    assert get_views_count(1) == '1 просмотр'
    assert get_views_count(101) == '101 просмотр'
    assert get_views_count(2) == '2 просмотра'
    assert get_views_count(22) == '22 просмотра'
    assert get_views_count(11) == '11 просмотров'
    assert get_views_count(25) == '25 просмотров'

def test_move_zeros():
    assert move_zeros([1, 0, 0, 2, 3, 0, 1]) == [1, 2, 3, 1, 0, 0, 0]

def test_clean_name():
    assert clean_name("игорuiь") == "игорь"
    assert clean_name('Илfdgьин Игfgdорь Алексан65g!дрович') == 'Ильин Игорь Александрович'
    assert clean_name("Иsвtrан Ив^%ан Ива?но)вич") == 'Иван Иван Иванович'

def test_get_pct_growth():
    assert get_pct_growth([100, 150, 300, 400]) == [None, '50%', '100%', '33%']