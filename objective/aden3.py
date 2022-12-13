# Списки контольная работа по введ.спец

# 1 Вариант
# from random import randint
#
# s = []
# l = int(input('Введите размер списка: '))
# for i in range(l):
#     s.append(randint(1, l))
#
# print(s)
#
# # Решение 1 варианта задач
# e = []
# for i in s:
#     if s.count(i) >= 2:
#         e.append(i)
#
# for q in e:
#     s.remove(q)
# print(s)

# 2 Вариант
# from random import randint
#
# s = []
# l = int(input('Введите размер списка: '))
# for i in range(l):
#     s.append(randint(1, l))
#
# print(s)
#
# e = []
# for i in s:
#     if i % 2 != 0:
#         e.append(i)
#
# index = s.index(max(e))
# s[index] = max(e) * 2
#
# print(s)

# 3 Вариант
# from random import randint
#
# s = []
# l = int(input('Введите размер списка: '))
# for i in range(l):
#     s.append(randint(1, l))
#
# print(s)
# p = 1
# for w in s:
#     if w % 2 != 0:
#         p *= w
#
# print(p)

# L = []
# tur = 0
# u = 0
# o = int(input("Введите кол-во элементов списка: "))
#
# for i in range(o):
#     L.append(int(input(f"Введите {i + 1}-й элемент списка: ")))
#
# print(L)
# c = L.count(0)
# if c >= 2:
#     for j in L:
#         if tur > 2:
#             break
#         elif j != 0 and tur == 1:
#             u += j
#         elif j == 0:
#             tur += 1
#     print(u)
# else:
#     print(0)

# a = input()
# f = list(map(int, a.split()))
# print(f)
# k1 = -1
# k2 = -1
# if 0 in f:
#     k1 = f.index(0)
#     f[k1] = '*'
# if 0 in f:
#     k2 = f.index(0)
# if k1 > -1 and k2 > -1:
#     print(sum(f[k1 + 1: k2]))
# else:
#     print(0)
