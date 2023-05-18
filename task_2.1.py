# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

# arr = [input(f'{i} elem: ') for i in range(int(input('Length: ')))]
# def minimum(arr):
#    pass
# def maximum(arr):
#    pass

# Первый вариант - здесь нужный список задаем изначально (как и требовалось по условию задачи):
# создаем функцию по минимуму:
def minimum(a, b):
    if a < b:
        return a
    else:
        return b
# список задаю один и на минимум и на максимум:
arr = [10, 20, 300, -1, 100, 1, 50, -15]
# задаем что будет минимальным значением:
min_num = arr[0]
for i in arr:
    min_num = minimum(min_num, i)
    pass
# создаем функцию по максимуму:
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
# задаем что будет максимальным значением:
max_num = arr[0]
for i in arr:
    max_num = maximum(max_num, i)
    pass
# Выводим результат:
print('min =', min_num, ',', 'max =', max_num)

# Второй вариант - в нем список берется произвольный через random, захотелось еще так попробовать:)
# задаем условия по списку:
import random
arr = [random.randint(-10, 50) for i in range(20)]
# создаем функцию по минимуму:
def minimum(a, b):
    if a < b:
        return a
    else:
        return b
# задаем переменную, что будет минимальным значением:
min_num = arr[0]
for i in arr:
    min_num = minimum(min_num, i)
    pass
# создаем функцию по максимуму:
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
# задаем переменную, что будет максимальным значением:
max_num = arr[0]
for i in arr:
    max_num = maximum(max_num, i)
    pass
# Выводим результат (+ список, чтобы был известен):
print(arr)
print('min =', min_num, ',', 'max =', max_num)