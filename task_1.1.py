# Задача 1.1.
# Есть строка с перечислением песен
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
## определяю начало и конец нужного диапазона
## для первого трека:
print(my_favorite_songs.find('Waste a Moment'))
print(my_favorite_songs.rfind(', Staying\' Alive'))
## для последнего трека:
print(my_favorite_songs.find(' New Salvation'))
print(len(my_favorite_songs))
## для второго трека:
print(my_favorite_songs.find(' Staying\' Alive'))
print(my_favorite_songs.rfind(', A Sorta Fairytale'))
## для второго трека с конца:
print(my_favorite_songs.find(' Start Me Up'))
print(my_favorite_songs.rfind(', New Salvation'))
## задаю диапазоны для вывода на консоль все вместе, исходя из параметров, определенных выше:
print(my_favorite_songs [0:14] + my_favorite_songs[63:77] + my_favorite_songs[15:30] + my_favorite_songs[50:62])
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

## ВАРИАНТ 2
## Нельзя переопределять поняла как - нельзя изменять что-либо в строке - потому что хотелось просто расставить дополнительно запятые.
## Если возможно было бы поправить строку my_favorite_songs в части запятых, то решение было бы другим:
#my_favorite_songs = 'Waste a Moment', 'Staying\' Alive', 'A Sorta Fairytale', 'Start Me Up', 'New Salvation'
#print(my_favorite_songs [0] + str(' ') + my_favorite_songs[-1] + str(' ') + my_favorite_songs[1] + str(' ') + str(' ') + my_favorite_songs[-2])