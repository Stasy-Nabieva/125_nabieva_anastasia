import random
s=[]
d=[]
string=[]
n=10
print('Спрос:')
for i in range(n):
    r1=random.randrange(50)
    s.append(r1)
    print(s[i], end=" ")
print(' ')
print('Предложение:')
for i in range(n):
    r2=random.randrange(50)
    d.append(r2)
    print(d[i], end=" ")
print(" ")
for i in range(n):
    if s[i] in d:
        string.append(s[i])
print("Сколько раз спроc равен предложению:")
print(len(string))