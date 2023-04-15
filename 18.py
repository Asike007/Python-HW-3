# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Enter the length of the list - '))
from random import randint
list_A = [randint(0,10) for i in range(n)]
print(list_A)
x = int(input('Enter the number for search - '))
min_difference = max(list_A)


for i in range(n):
    if abs(x - list_A[i] < min_difference):
        min_difference  = abs(x - list_A[i])
        nearest_number = list_A[i]

print(f'The nearest number value is - {nearest_number}')