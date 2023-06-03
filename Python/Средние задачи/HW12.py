def sum_range(start, end):
    sum=0
    for i in range(start,end+1):
        sum=sum+i
    print(sum)
print("Input the first number")
a=int(input())
print("Input the second number")
b=int(input())
if a>b:
    sum_range(b,a)
else:
    sum_range(a,b)

