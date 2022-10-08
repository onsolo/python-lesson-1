# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

import math

number = float(input('Введите число: '))
number = math.floor(number)

for i in range(1, number):
    if i % 2 == 0:
        print(i, end=' ')
