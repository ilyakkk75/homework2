# def row_sum(a, i):
#     return sum(a[i])
#
# def row_avg(a, i):
#     return sum(a[i]) / len(a[i])
#
# def row_max(a, i):
#     return max(a[i])
#
# def row_max_index(a, i):
#     return a[i].index(max(a[i]))
#
# def row_min(a, i):
#     return min(a[i])
#
# def row_min_index(a, i):
#     return a[i].index(min(a[i]))
#
#
# def col_sum(a, j):
#     return sum(row[j] for row in a)
#
# def col_avg(a, j):
#     return col_sum(a, j) / len(a)
#
# def col_max(a, j):
#     return max(row[j] for row in a)
#
# def col_max_index(a, j):
#     return [row[j] for row in a].index(col_max(a, j))
#
# def col_min(a, j):
#     return min(row[j] for row in a)
#
# def col_min_index(a, j):
#     return [row[j] for row in a].index(col_min(a, j))
#
#
# def total_sum(a):
#     return sum(sum(row) for row in a)
#
# def total_avg(a):
#     return total_sum(a) / (len(a) * len(a[0]))
#
# def total_max(a):
#     mx = max(max(row) for row in a)
#     for i in range(len(a)):
#         if mx in a[i]:
#             return mx, i, a[i].index(mx)
#
# def total_min(a):
#     mn = min(min(row) for row in a)
#     for i in range(len(a)):
#         if mn in a[i]:
#             return mn, i, a[i].index(mn)
#
#
# n = int(input("Строк: "))
# m = int(input("Столбцов: "))
#
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for i in range(n):
#     print("\nСтрока", i)
#     print("Сумма:", row_sum(a, i))
#     print("Среднее:", row_avg(a, i))
#     print("Максимум:", row_max(a, i), "Индекс:", row_max_index(a, i))
#     print("Минимум:", row_min(a, i), "Индекс:", row_min_index(a, i))
#
# for j in range(m):
#     print("\nСтолбец", j)
#     print("Сумма:", col_sum(a, j))
#     print("Среднее:", col_avg(a, j))
#     print("Максимум:", col_max(a, j), "Индекс:", col_max_index(a, j))
#     print("Минимум:", col_min(a, j), "Индекс:", col_min_index(a, j))
#
# print("\nВся таблица")
# print("Сумма:", total_sum(a))
# print("Среднее:", total_avg(a))
#
# mx, i, j = total_max(a)
# print("Максимум:", mx, "Строка:", i, "Столбец:", j)
#
# mn, i, j = total_min(a)
# print("Минимум:", mn, "Строка:", i, "Столбец:", j)
