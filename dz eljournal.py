# students=[]
# students_marks=[]
#
# while True:
#     var=int(input('1-добавить,2-удалить,3-список,4-изменить оценку,0-выход: '))
#
#     if var==1:
#         name=input()
#         students.append(name)
#         students_marks.append([])
#     elif var==2:
#         index=int(input())
#         if 1<=index<=len(students):
#             students.pop(index-1)
#             students_marks.pop(index-1)
#         else:
#             print('такого студента нет')
#     elif var==3:
#         for i in range (len(students)):
#             print(f'{i+1},{students[i]}:{students_marks[i]}')
#     elif var==4:
#         index=int(input('введите номер студента'))
#         if index<1 or index>len(students):
#             print('некорректно')
#         else:
#             mark_index=int(input('какую оценку поменять'))
#             if mark_index<1 or mark_index>len(students_marks[index-1]):
#                 print('такой нет')
#             else:
#                 marks = int(input())
#                 students_marks[index-1][mark_index-1]=marks
#     elif var==0:
#         break
#     else:
#         print('некорректно')