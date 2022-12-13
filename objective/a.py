# def two_sum(m: list, n: int) -> list:
#     for i in range(len(m)):
#         for e in range(1, len(m)):
#             if m[i] + m[e] == n:
#                 return [m[i], m[e]]
#
#
# print(two_sum([-3, 4, 1, 3, 6], 5))

# def two_sum(m: list, n: int) -> list:
#     s = set()
#     for i in range(len(m)):
#         number_to_find = n - m[i]
#         if s.__contains__(number_to_find):
#             return [number_to_find, m[i]]
#
#         s.add(m[i])
#
#
# print(two_sum([-3, 4, 1, 3, 6], 4))


# def two_sum(m: list, n: int) -> list:
#     m.sort()
#     for i in range(len(m)):
#         number_to_find = n - m[i]
#         l = i + 1
#         r = len(m) - 1
#         while l <= r:
#             mid = l + (r - l) // 2
#             if m[mid] == number_to_find:
#                 return [m[i], m[mid]]
#             elif number_to_find < m[mid]:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#
#     else:
#         return []
#
#
# print(two_sum([0, 3, 3, 6, 10], 9))
