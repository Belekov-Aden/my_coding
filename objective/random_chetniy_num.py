from random import random

q = 0

for i in range(1_000):
    if int(random()*100) % 2 == 0:
        q += 1

print("%.2f%%" % (q / 1_000 * 100))