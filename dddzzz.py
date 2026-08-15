# этот код был написан и подкорректирован под наблюденинем и с помощью ии,ибо задание вызвало сложность
# students = []
# next_id = 1
#
# while True:
#     print("\n меню:")
#     print("1. добавить студента")
#     print("2. показать всех из класса")
#     print("3. удалить студента по ID")
#     print("4. поставить оценку")
#     print("5. посмотреть данные одного студента")
#     print("6. список (ID, имя, класс)")
#     print("0. выход")
#
#     choice = input("выберите действие: ")
#
#     if choice == '1':
#         name = input("имя: ")
#         class_name = input("класс: ")
#
#         student = {
#             'id': next_id,
#             'name': name,
#             'class': class_name,
#             'grades': []
#         }
#         students.append(student)
#         print(f"студент добавлен с ID {next_id}")
#         next_id += 1
#
#     elif choice == '2':
#         search_class = input("введите класс для поиска: ")
#         found = False
#         for s in students:
#             if s['class'] == search_class:
#                 print(f"ID: {s['id']}, Имя: {s['name']}")
#                 found = True
#         if not found:
#             print("таких студентов не найдено.")
#
#     elif choice == '3':
#         del_id = int(input("введите ID для удаления: "))
#         # Оставляем в списке только тех, чей ID не совпадает с удаляемым
#         initial_count = len(students)
#         students = [s for s in students if s['id'] != del_id]
#
#         if len(students) < initial_count:
#             print("удалено.")
#         else:
#             print("ID не найден.")
#
#     elif choice == '4':
#         grade_id = int(input("введите ID студента: "))
#         # Ищем нужного студента в цикле
#         for s in students:
#             if s['id'] == grade_id:
#                 grade = float(input("оценка от 0 до 5: "))
#                 s['grades'].append(grade)
#                 print("оценка добавлена.")
#                 break
#         else:
#             print("студент с таким ID не найден.")
#
#     elif choice == '5':
#         view_id = int(input("введите ID студента: "))
#         for s in students:
#             if s['id'] == view_id:
#                 grades_str = ", ".join(map(str, s['grades'])) if s['grades'] else "Нет оценок"
#                 print("-" * 20)
#                 print(f"ID: {s['id']}")
#                 print(f"имя: {s['name']}")
#                 print(f"класс: {s['class']}")
#                 print(f"оценки: [{grades_str}]")
#                 break
#         else:
#             print("студент не найден.")
#
#     elif choice == '6':
#         print("(ID, имя, класс):")
#         for s in students:
#             print((s['id'], s['name'], s['class']))
#
#     elif choice == '0':
#         print("пока")
#         break
#
#     else:
#         print("неверный выбор.")