# Задача 1.4.
# Есть словарь кодов товаров titles
titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}
# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.
store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
  }

# Рассчитайте на какую сумму лежит каждого товара на складе.
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

for keys_titles, values_titles in titles.items():
    for keys_store, values_store in store.items():
        if values_titles == keys_store:
            for i in range(len(values_store)):
                quantity_total = 0
                price_total = 0
                for v in values_store:
                    quantity_total += v['quantity']
                    price_total += v['quantity']*v['price']
            print(f'{keys_titles} - {quantity_total} шт, стоимость {price_total} руб')

# или вариант 2 для вывода на печать))                    
            # titles_total = []
            # titles_total.append(keys_titles)
            # titles_total.append('-')
            # titles_total.append(quantity_total)
            # titles_total.append('шт, стоимость')
            # titles_total.append(price_total)
            # titles_total.append('руб')
            # print(titles_total)
            





