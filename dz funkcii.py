# def summa(sp):
#     s = 0
#     for i in sp:
#          s += i
#     return s
#
#
# def srednee(sp):
#     return summa(sp) / len(sp)
#
#
# def maximum(sp):
#      mx = sp[0]
#  for i in sp:
#      if i > mx:
#      mx = i
#  return mx
#
#
# def minimum(sp):
#     mn = sp[0]
# for i in sp:
#      if i < mn:
#      mn = i
# return mn
#
#
# def index_max(sp):
#     mx = sp[0]
#     ind = 0
#     for i in range(len(sp)):
#         if sp[i] > mx:
#         mx = sp[i]
#
# return ind
#
#
# def index_min(sp):
#     mn = sp[0]
#     ind = 0
#     for i in range(len(sp)):
#         if sp[i] < mn:
#         mn = sp[i]
#         ind = i
#     wreturn ind
#
#
# a = [
#     [2, 3, 4, 5],
#     [2, 4, 3, 5],
#     [4, 3, 4, 2]
# ]
#
# print("Строки")
#
# for row in a:
#         print("Сумма:", summa(row))
#     print("Среднее:", srednee(row))
#     print("Максимум:", maximum(row))
#     print("Индекс максимума:", index_max(row))
#     print("Минимум:", minimum(row))
#     print("Индекс минимума:", index_min(row))
#     print()
#
# print("Столбцы")
#
# for j in range(len(a[0])):
#         col = []
#     for i in range(len(a)):
#             col.append(a[i][j])
#
#     print("Сумма:", summa(col))
#     print("Среднее:", srednee(col))
#     print("Максимум:", maximum(col))
#     print("Индекс максимума:", index_max(col))
#     print("Минимум:", minimum(col))
#     print("Индекс минимума:", index_min(col))
#     print()
#
# all_num = []
#
# for row in a:
#         for x in row:
#             all_num.append(x)
#
# print("Вся таблица")
# print("Сумма:", summa(all_num))
# print("Среднее:", srednee(all_num))
# print("Максимум:", maximum(all_num))
# print("Минимум:", minimum(all_num))
#
# mx = a[0][0]
# mn = a[0][0]
# mx_i = 0
# mx_j = 0
# mn_i = 0
# mn_j = 0
#
# for i in range(len(a)):
#         for j in range(len(a[i])):
#             if a[i][j] > mx:
#                 mx = a[i][j]
#             mx_i = i
#             mx_j = j
#
#         if a[i][j] < mn:
#                 mn = a[i][j]
#             mn_i = i
#             mn_j = j
#
# print("Максимум находится:", mx_i, mx_j)
# print("Минимум находится:", mn_i, mn_j)