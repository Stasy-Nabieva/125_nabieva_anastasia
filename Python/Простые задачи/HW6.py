print('Введите сколько денег у Алисы:')
x=int(input())
print('Введите сколько денег у Боба:')
y=int(input())
print('Введите сколько денег у Чарли:')
z=int(input())
print('Введите стоимость подписки: ')
cost=int(input())

def netflix(x,y,z,cost):
    if(cost-(x+y)<cost-(x+z) and cost-(x+y)<cost-(y+z)):
        print('Подписку могут купить Алиса и Боб')
    if(cost-(x+z)<cost-(x+y) and cost-(x+z)<cost-(y+z)):
        print('Подписку могут купить Алиса и Чарли')
    if(cost-(y+z)<cost-(x+y) and cost-(y+z)<cost-(x+z)):
        print('Подписку могут купить Боб и Чарли')    
netflix(x,y,z,cost)