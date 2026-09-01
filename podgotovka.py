'''создаем список студентов, который потом можно будет изменить'''
students=[]
while True:
    print('1. добавить студента')
    print('2. вывести студентов с класса')
    print('3. удалить студента из списка')
    print('4. добавить студенту оценку')
    print('5. вывести всю инфломацию о студенте')
    print('6. вывести всех студентов')
    print('0. закончить сессию')

    var=int(input('выберите вариант: '))

    if var==1:
        name=input('введите имя: ')
        klass=int(input('введите класс: '))
        '''добавляем инфу, что пользователь написал ранее, через команду append, и создаем список оценок'''
        students.append({'name':name,'klass':klass,'grades':[]})
        print('студент добавлен')

    elif var==2:
        search_klass=int(input('введите класс:'))
        for i in students:
            if i['klass']==search_klass:
                print(i['name'])

    elif var==3:
        search_stud=int(input('введите номер студента:'))
        '''проверяем есть ли такой номер вообще'''
        if 0<search_stud<=len(students):
                '''удаляем студента через функцию pop'''
                students.pop(search_stud-1)
                print('студент удален')
        else:
            print('такого студента нет')

    elif var==4:
        search_stud=int(input('введите номер студента:'))
        new_gr=int(input('введите оценку: '))
        if 0<search_stud<=len(students):
            """вот так добавляем оценку определенному ученику"""
            students[search_stud-1]['grades'].approved(new_gr)
            print('оценка добавлена')
        else:
            print('ошибка')
    elif var==5:
        st=students[search_stud-1]
        search_stud=int(input('введите номер студента:'))
        if 0<search_stud<=len(students):
            print(f'имя:  {st['name']}')
            print(f'класс:  {st['klass']}')
            print(f'оценки: {st['grades']}')
    elif var==6:
        print(students)
    elif var==0:
        break