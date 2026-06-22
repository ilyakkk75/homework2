import random
play="да"
while play=='да':
    number = random.randint(1,99)
    human = 0
    computer = 0
    print('добро пожаловать в игру')
    for i in range(5):
        n=int(input('введите число :'))
        if n > number:
            print('нет, меньше')
        elif n < number:
            print('нет, больше')
        else:
             break
    if n == number:
        human+=1
    else:
        computer+=1
    print('вы: ', human)
    print('компьютер: ',computer)
play=str(input('сыграть еще раз? (да/нет'))