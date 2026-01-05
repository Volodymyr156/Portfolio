"""
1. Сумма цифр числа

Напишите рекурсивную функцию, которая находит сумму всех цифр числа.

Данные:

num = 43197

Пример вывода:

24
"""

num = 15

def sum_of_nums(n,acc = 0):
    """
    find total of nums
    """
    n = str(n)
    if not n:
        return acc
    return sum_of_nums(n[1:], acc + int(n[0]))


print(sum_of_nums(num))



def sum_of_nums_non_tail(n):
    n = str(n)
    if not n:
        return 0
    return int(n[0]) + sum_of_nums_non_tail(n[1:])


print(sum_of_nums_non_tail(num))




"""
2. Сумма вложенных чисел

Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.

Данные:

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

Пример вывода:

28"""

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

def calculator(data : list, calc = 0) -> int:
    """
    sum all numbers in nested_numbers
    """
    if not data:
        return calc
    if isinstance(data[0],list):
        return calculator(data[1:] + data[0], calc)
    return calculator(data[1:], calc + data[0])


print(calculator(nested_numbers))

def sum_digits_non_tail(lst):
    if not lst:
        return 0
    if isinstance(lst[0], list):
        return sum_digits_non_tail(lst[0]) + sum_digits_non_tail(lst[1:])

    return lst[0] + sum_digits_non_tail(lst[1:])


print(sum_digits_non_tail(nested_numbers))
