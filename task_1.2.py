# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random
my_favorite_songs = [
    ['Waste a Moment', 3.03], 
    ['New Salvation', 4.02], 
    ['Staying\' Alive', 3.40], 
    ['Out of Touch', 3.03], 
    ['A Sorta Fairytale', 5.28], 
    ['Easy', 4.15], 
    ['Beautiful Day', 4.04], 
    ['Nowhere to Run', 2.58], 
    ['In This World', 4.02],]
song_1 = random.choice(my_favorite_songs)
song_2 = random.choice(my_favorite_songs)
song_3 = random.choice(my_favorite_songs)
# print(song_1[1])
# print(song_2[1])
# print(song_3[1])
# выше строчки убрала в комменты, так как нет условия выводить время звучания случайных песен по отдельности, но сама конечно смотрела, что там складывается))
print('Три песни звучат', round((song_1[1] + song_2[1] + song_3[1]), 3), 'минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

import random
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,}
song_1 = random.choice(list(my_favorite_songs_dict.values()))
song_2 = random.choice(list(my_favorite_songs_dict.values()))
song_3 = random.choice(list(my_favorite_songs_dict.values()))
# print(song_1)
# print(song_2)
# print(song_3)
# выше строчки убрала в комменты, так как нет условия выводить время звучания случайных песен по отдельности
print('Три песни звучат', round((song_1 + song_2 + song_3), 3), 'минут')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
