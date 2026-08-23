def NumberSequence(Start, End, Even=True):
    for i in range(Start, End + 1):
        if Even and i % 2 == 0:
            yield i
        if not Even and i % 2 != 0:
            yield i

Start = int(input("введите начало диапазона: "))
End = int(input("введите конец диапазона: "))
Choice = input("чётные или нечётные (ч/н): ")

if Choice.lower() == 'ч':
    Numbers = list(NumberSequence(Start, End, True))
else:
    Numbers = list(NumberSequence(Start, End, False))

print(Numbers)