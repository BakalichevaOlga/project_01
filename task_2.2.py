# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

# честно говоря, за решение взяла основу из других задач
# Вариант первый (с if-elif-else. основа из задачи 1.3)
def quarter_of(month):
    pass
month = int(input('Введите номер месяца:'))
if month == 1:
    print('месяц', month, '(январь) является частью первого квартала')
elif month == 2:
    print('месяц', month, '(февраль) является частью первого квартала')
elif month == 3:
    print('месяц', month, '(март) является частью первого квартала')
elif month == 4:
    print('месяц', month, '(апрель) является частью второго квартала')
elif month == 5:
    print('месяц', month, '(май) является частью второго квартала')
elif month == 6:
    print('месяц', month, '(июнь) является частью второго квартала')
elif month == 7:
    print('месяц', month, '(июль) является частью третьего квартала')
elif month == 8:
    print('месяц', month, '(август) является частью третьего квартала')
elif month == 9:
    print('месяц', month, '(сентябрь) является частью третьего квартала')
elif month == 10:
    print('месяц', month, '(октябрь) является частью четвертого квартала')
elif month == 11:
    print('месяц', month, '(ноябрь) является частью четвертого квартала')
elif month == 12:
    print('месяц', month, '(декабрь) является частью четвертого квартала')
else:
    month >= 13 or month < 0
    print('Такого месяца нет!')
quarter_of(month)

# Вариант второй (со словарем, основа из задачи 2.3)
i = int(input('Введите номер месяца:'))
month = {
    1: '(январь) является частью первого квартала', 
    2: '(февраль) является частью первого квартала', 
    3: '(март) является частью первого квартала', 
    4: '(апрель) является частью второго квартала', 
    5: '(май) является частью второго квартала', 
    6: '(июнь) является частью второго квартала', 
    7: '(июль) является частью третьего квартала', 
    8: '(август) является частью третьего квартала', 
    9: '(сентябрь) является частью третьего квартала', 
    10: '(октябрь) является частью четвертого квартала', 
    11: '(ноябрь) является частью четвертого квартала', 
    12: '(декабрь) является частью четвертого квартала'}
def quarter_of(month):
    pass
print('месяц', i, month.get(i))
quarter_of(month)