from homework_1.homework_1_package.homework1_task1 import is_event
from homework_1.homework_1_package.homework1_task2 import is_prime
from homework_1.homework_1_package.homework1_task3 import is_arifm_progression
from homework_1.homework_1_package.homework1_task4 import get_triangle_kind
from homework_1.homework_1_package.homework1_task5 import is_palindrom
from homework_1.homework_1_package.homework1_task6 import get_words
from homework_1.homework_1_package.homework1_task7 import get_person_short_name
from homework_1.homework_1_package.homework1_task8 import is_list_growing
from  homework_1.homework_1_package.homework1_task9 import get_pairs_number

def test_is_event():
    assert is_event(2) == True
    assert is_event(3) == False

def test_is_prime():
    assert is_prime(0) < 2
    assert is_prime(2)
    assert is_prime(17)

def test_is_arifm_progression():
    assert is_arifm_progression(3, 6, 9)
    assert is_arifm_progression(-3, 1, 5)

def test_get_triangle_kind():
    assert get_triangle_kind(-1, 1, -2) == 'ошибка, нужен ввод положительных чисел'
    assert get_triangle_kind(1, 1, 1) == 'равносторонний'
    assert get_triangle_kind(1, 1, 2) == 'равнобедренный'
    assert get_triangle_kind(1, 2, 3) == 'обычный'

def test_is_palindrom():
    assert is_palindrom('а роза упала на лапу азора')

def test_get_words():
    assert get_words("Александр Сергеевич Пушкин") == ["Александр", "Сергеевич", "Пушкин"]

def test_get_person_short_name():
    assert get_person_short_name("Лермонтов Михаил Юрьевич") == "Лермонтов М. Ю."

def test_is_list_growing():
    assert is_list_growing([1, 1, 1]) == False
    assert is_list_growing([3, 2, 1]) == False
    assert is_list_growing([]) == True
    assert is_list_growing([-1, -2, -3]) == False
    assert is_list_growing([-3, 2, 1]) == False
    assert is_list_growing([0, 1, 2]) == True

def test_get_pairs_number():
    assert get_pairs_number([1], 2) == []
    assert get_pairs_number([1, 2, 3, 4], 5) == [(3, 2), (4, 1)]
    assert get_pairs_number([4, -1], 3) == [(4, -1)]