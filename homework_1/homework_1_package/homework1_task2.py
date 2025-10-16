"""
Напишите функцию, которая возвращает true, если число является простым
Больше 1 (1 не является простым числом)
2 - единственное простое чётное число
Делится только на 1 и на себя без остатка
Не имеет других делителей

def is_prime(n: int) -> bool: # n=3
    for i in range(2, n): # list(range(2,2)) = []
        if n % i == 0:
            return False
    return True


assert is_prime(0) < 2
assert is_prime(2)
assert is_prime(17) 
print('tests passed')
"""

def is_prime(n: int) -> bool:
    return all(n % i !=0 for i in range(2,n))





