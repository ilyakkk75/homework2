# пузырек
# a=[6,7,4,56,4]
# for i in range(len(a)):
#     for j in range(len(a)-1-i):
#         if a[j+1]<a[j]:
#             a[j+1],a[j]=a[j],a[j+1]
# print(a)
# вставками
# a=[6,7,4,56,4]
# for i in range(1,len(a)):
#     for j in range(i,0,-1):
#         if a[j]<a[j-1]:
#             a[j],a[j-1]=a[j-1],a[j]
#         else:
#             break
# print(a)
# viborom
# a=[6,7,4,56,4]
# for i in  range(len(a)):
#     min_index=i
#     for j in range(i+1,len(a)):
#         if a[j]<a[min_index]:
#           a[min_index],a[j]=a[j],a[min_index]
# print(a)
# idk shaker