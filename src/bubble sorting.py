from random import randint
n = int(input('Введите длину массива '))
a = [randint(0, 100) for i in range(n)]
print('Массив до сортировки')
print(a)
for j in range(n):
    for i in range(n - 1):
	if a[i] > a[i + 1]:
	    a[i], a[i + 1] = a[i + 1], a[i]
print('Массив после сортировки ')
print(a)