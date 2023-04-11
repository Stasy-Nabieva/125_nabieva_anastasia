import random
a=float(random.uniform(1000,99999))
b=float(random.uniform(1000,99999))
flag=True
c=a+b
if a>b:
    eps=0.0001*a
else:
    eps=0.0001*b
def eqv(a,b,c):
    if (c-(a+b) < c-(a+b)+eps) or (c-(a+b) > c-(a+b)-eps):
        flag = True
    else:
        flag = False
    print(flag)  
print('a=' "{:10.5f}".format(a))
print('b=' "{:10.5f}".format(b))
print('c=' "{:10.5f}".format(c))
eqv(a,b,c)