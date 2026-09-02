'''num2'''
'''a=int(input())
b=int(input())
if a>b:
    a,b=b,a
for i in range(b,a-1,-1):
    print(i)'''
'''a-1 потому что пайтон считает за одну цифру до указ значения'''
"""num4"""
'''a=input()
k='QWERTYUIOPASDFGHJKLZXCVBNM'
if a in k:
    print('yes')
else:
    print('no')'''
'''NUM5'''
'''list=[]
num=0
for i in range(8):
    
    list.append(num)
    num+=3
    
print(list)'''

def number(list):
    for i in list:
        if i%2==0:
            print(i)


ls=[3,4,5,32,3]
number(ls)
