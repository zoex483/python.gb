"""
task№ 18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
 строках записаны N целых чисел Ai. Последняя строка содержит число X

"""

import random

N = int(input('Введите число N: '))
X = int(input('Введите число Х: '))
A = [random.randint(1, 100) for i in range(N)]

sum_x = 0

for i in A and range(N):
    print(A[i])
if X in A:
    sum_x += 1
    print(X)


print('')  # Пустая строка для читаемости.
print('Число X равное', X, 'встречается в этом массиве', sum_x, 'раз')

B = []

for i in A and range(N):
    if X < A[i]:
        dif_1 = A[i] - X
        B.append(dif_1)
    else:
        dif_2 = X - A[i]
        B.append(dif_2)

print('Массив А')
print(A)
print('Массив В (разница значений элементов массива А с X)')
print(B)

print('Минимальное число в массиве В:', min(B))

for i in B and range(N):
    if B[i] == min(B):
        index = i
        print('Индекс этого числа в массиве В:', i)

print('Число c тем же индексом в массиве А ближе других к числу X')
print('А вот и само число: ', A[index])