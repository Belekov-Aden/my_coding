
#Authorization
login = 'Aden'
password = '26.00.00'

print(f'Для входа введите заранее придуманный логин и пароль')
log = input('Логин:')
pas = input('Пароль: ')
if login == log and password == pas:
    print('True')
else:
    print('False')