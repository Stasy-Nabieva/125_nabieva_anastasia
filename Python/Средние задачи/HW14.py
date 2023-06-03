print("Введите имя пользователя")
name=input()
from random import randint
n = randint(0, 100)
i = 0
print("Введите число")

while True:
    a = int(input())
    if a == n:
        print('Вы угадали')
        break
    if a < n:
        print('загаданное число больше')
    else:
        print('загаданное число меньше')
    i += 1
print(i)
f = open('HW14.txt','w')
f.write('Имя пользователя: ') 
f.write(name)
f.write('\n Количество попыток: ')
f.write(str(i))
f.close()