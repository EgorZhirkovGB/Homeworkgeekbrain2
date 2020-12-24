userAnswer = int(input('Введите цифру месяца: '))
seasons = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'fall': [9, 10, 11]}

if userAnswer in seasons['winter']:
    print('Зима')
elif userAnswer in seasons['spring']:
    print('Весна')
elif userAnswer in seasons['summer']:
    print('Лето')
elif userAnswer in seasons['fall']:
    print('Осень')