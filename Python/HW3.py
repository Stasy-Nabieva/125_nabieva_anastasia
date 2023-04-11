from random import *
S1=[]
N1=randint(50,100)
for i in range(N1):
    s1=randint(0,9999)
    S1.append(s1)
S1.sort()
print(*S1)

S2=[]
N2=randint(50,100)
for i in range(N2):
    s2=randint(0,9999)
    S2.append(s2)
S2.sort()
print(*S2)

S3=[]
for i in range(N1):
    if S1[i] in S2 :
        S3.append(S1[i])
S3.sort()
if len(S3)==0:
    print('Одинаковых элементов нет')
else:
    print(*S3)
            
    
