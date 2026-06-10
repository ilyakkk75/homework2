задане1неполучилось
задание2
num = int(input())
if num == 1:
    print('!')
elif num == 2:
    print('@')
elif num == 3:
    print('#')
elif num == 4:
    print('$')
elif num==5:
    print('%')
elif num==6:
    print('^')
elif num==7:
    print('&')
elif num==8:
    print('*')
elif num==9:
    print('(')
elif num==0:
    print(')')
else :
    print('error')
#задание3
num=int(input())
a=num//100
b=(num//10)%10
c=num%10
if a==b or a==c or b==c:
    print('есть')
else:
    print('нет')
z4
year=int(input())
if (year%400==0) or (year%4==0 and year%100 != 0):
    print('високосный')
else :
    print('Нет')
z5idk
z6
usd=float(input())
print('куда конвертировать')
print('eur')
print('uan')
print('azn')
val=str(input())
# eur=usd*1.15
# uan=usd*0,15
# azn=usd*0.59
if val== 'eur':
    print(f'{usd*0.87}')
elif val == 'uan':
    print(f'{usd*6.77}')
elif val == 'azn':
    print(f'{usd*1.70}')
else :
    print('error')
z7
price = float(input())
if price >=200 and price <=300:
    print(f'{price-(price*0.03)}')
elif price>=300 and price <500:
    print(f'{price-(price*0.05)}')
elif price >= 500:
    print(f'{price-(price*0.07)}')
else:
    print(f'{price}')
z8
okr=float(input())
kvad=float(input())
if okr<=kvad :
    print('yes')
else :
    print('no')
z9
print('как меня зовут?')
print('a) илья')
print('b) ваня')
print('c) женя')
a=('a')
ans1=str(input())
if ans1==a:
    print('+2 балла')
else:
    print('неверно')
print('сколько мне лет?')
print('a) 16')
print('b) 17')
print('c) 15')
c=('c')
ans2=str(input())
if ans2==c:
    print('+2 балла')
else:
    print('неверно')
print('где я живу?')
print('a) Ростов-На-Дону')
print('b) Москва')
print('c) СПБ')
b=('b')
ans3=str(input())
if ans3==b:
    print('+2 балла')
else:
    print('неверно')
bll=int(input('введите количество правильных ответов:'))
print(f'{bll*2}')
z10idk