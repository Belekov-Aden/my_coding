text_palindrom = list(input('Введите слово: '))

if text_palindrom[::-1] == text_palindrom:
    print(f'Это слово палиндром')

else:
    print(f'Слово не палиндром')


def palindrom(a):
    return a == a[::-1]


print(palindrom(text_palindrom))
