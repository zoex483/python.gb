""" task № 1. Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

n = int(input('Введите число: '))
count = 0
n1 = n

while n1 != 0:
    count = count + n1 % 10
    n1 = n1 // 10

print(f"{n} -> {count}")