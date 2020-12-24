string = list(input('').split())
n = 0
while n < len(string):
    print(n+1,' строка:',string[n][0:10])
    n += 1