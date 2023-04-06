"""Вводится список целых чисел в одну строчку через пробел. 
Необходимо оставить в нем только двузначные числа. Реализовать 
программу с использованием функции filter. Результат отобразить на экране 
в виде последовательности оставшихся чисел в одну строчку через пробел."""


def two_pos_numbers(num):
    if 9 < num < 100:
        return True
    else:
        return False

# numbers = [int(i) for i in input("Введите числа:  ").split()]
numbers = map(int, input("Введите числа:  ").split())
res_numbers = filter(two_pos_numbers, numbers)
print(*res_numbers)


