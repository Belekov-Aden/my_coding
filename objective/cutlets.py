#За какое наименьшее время удастся поджарить с обеих сторон n котлет
# k, m, - n
k = int(input('Катлеты в сковороде: '))
m = int(input('Одна сторона обжарки: '))
n = int(input('Кол-во катлеты: '))

if n <= k:
    t = 2*m
elif n * 2 % k == 0:
    t = m * (n * 2 // k)
else:
    t = m * (1 + (n * 2 // k))
print(t)