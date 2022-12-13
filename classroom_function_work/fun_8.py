
from datetime import datetime, date

now = datetime.now()

print(f'Ваше текущее время {now.date()}')

month_today = now.month

winter = print
spring = print
summer = print
autumn = print

def season(month):
    if month == 1 or month == 2 or month == 12:
        winter(f' Месяц {month_today} зима')
    elif month == 3 or month == 4 or month == 5:
        spring(f'Месяц {month_today} весна')
    elif month == 6 or month == 7 or month == 8:
        summer(f'Месяц {month_today} лето')
    elif month == 9 or month ==  10 or month == 11:
        autumn(f'Месяц {month_today} осень')

season(month_today)