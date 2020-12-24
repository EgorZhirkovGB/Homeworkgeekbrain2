print('После ввода слова нажмите Enter')
print('Что бы закончить заполнять список введите STOP')
element = input('Заполните списокж: ')
my_list = []

while element != 'STOP':
        my_list.append(element)
        element = input('Заполните список: ')

parity = int(len(my_list) % 2)
n = 0
if parity == 0:
    while n < len(my_list):
        my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
        n += 2

    print(my_list)
else:
    latest_value = my_list.pop(-1)
    while n < len(my_list):
        my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
        n += 2

    my_list.append(latest_value)
    print(my_list)
