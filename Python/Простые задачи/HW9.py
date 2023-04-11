string1="Мороз и солнце; день чудесный!"
l=len(string1)
string2=[]
j=0
for i in range(l):
    if (string1[i]==" "):
        string2.append(" ")
        continue    
    if (string1[i]==":"):
        string2.append(":")
        continue
    if (string1[i]==";"): 
        string2.append(";")
        continue
    if (string1[i]==","): 
        string2.append(",")
        continue
    if (string1[i]=="-"):
        string2.append("-")
        continue
    if j%2==0:
        string2.append(string1[i].lower())
        j+=1
    else:
        string2.append(string1[i].upper())
        j+=1
print(*string2)
