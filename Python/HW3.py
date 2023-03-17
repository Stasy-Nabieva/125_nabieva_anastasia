import json
from datetime import *
path='/Users/nabie/Desktop/2022-2023 уч. год/Программирование/names.json'
with open(path,'r', encoding="utf8") as file:
    names = json.load(file)
data=[]
for i in range(4):
    data.append(names[i] ["birthday"])
    
data1=data[0]
str1=datetime.strptime(data1, '%d/%m/%Y').date()
data2=data[1]
str2=datetime.strptime(data2, '%d/%m/%Y').date()
data3=data[2]
str3=datetime.strptime(data3, '%d.%m.%Y').date()
data4=data[3]
str4=datetime.strptime(data4, '%Y-%m-%d').date()

today=datetime.now().date()

age1=(today.year-str1.year)-((today.month, today.day) < (str1.month,str1.day))
age2=(today.year-str2.year)-((today.month, today.day) < (str2.month,str2.day))
age3=(today.year-str3.year)-((today.month, today.day) < (str3.month,str3.day))
age4=(today.year-str4.year)-((today.month, today.day) < (str4.month,str4.day))

middle_age=(age1+age2+age3+age4)/4
print(middle_age)







