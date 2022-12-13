total = 0
days = 0
temperature = 0

while temperature > -300:
    total += temperature
    days += 1
    temperature = float(input())

print(total / days)