import random
a=[]
n1=random.randrange(5,101)
print('Введите х: ')
x=int(input())
summ=0
flag=False

for i in range(n1):
    n2=random.randrange(0,9999)
    a.append(n2)
    summ=summ+a[i]

def magic(summ,x):
    if (summ%x==0):
        flag=True
        print('Сумма чисел делится на х')
    else:
        flag=False
        print('Сумма чисел не делится на х')
    print(flag)
magic(summ,x)