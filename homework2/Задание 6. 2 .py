name1 = input('Введите назавание первого товара: ')
price1 = int(input('Введите цену перого товара: '))
Quantity1 = int(input('Введите количество первого товара: '))
name2 = input('Введите название второго товара: ')
price2 = int(input('Введите цену второго товара: '))
Quantity2 = int(input('Введите количество второго товара: '))
name3 = input('Введите название третьего товара:  ')
price3 = int(input('Введите цену третьего товара: '))
Quantity3 = int(input('Введите количество третьего товара: '))
userItem1 = ({'name': [name1], 'price': [price1], 'Quantity': [Quantity1], 'Units': ['шт']})
userItem2 = ({'name': [name2], 'price': [price2], 'Quantity': [Quantity2], 'Units': ['шт']})
userItem3 = ({'name': [name3], 'price': [price3], 'Quantity': [Quantity3], 'Units': ['шт']})
print('Название:', userItem1['name'] + userItem2['name'] + userItem3['name'])
print('Стоймость:', userItem1['price'] + userItem2['price'] + userItem3['price'])
print('Количество:', userItem1['Quantity'] + userItem2['Quantity'] + userItem3['Quantity'])
