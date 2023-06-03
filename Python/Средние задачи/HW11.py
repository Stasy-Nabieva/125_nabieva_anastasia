print("Введите 5 и более слов")
string=input()

word=string.split(" ")
w0=word[0]
lenw0=len(word[0])
def maxword(word,w0,lenw0):
    for i in word:
        if (len(i)>lenw0):
            w0=i
    print("Самое длинное слово:")
    print(i)
def compare(word):
    sortedword=sorted(word)
    fl=True
    for i in range(len(sortedword)-1):
        if sortedword[i]==sortedword[i+1]:
            print("Самое часто встречающееся слово")
            print(sortedword[i])
            fl=False
    if fl==True:
        print("Первое слово")
        print(word[0])
if len(string)>=5:
    print("Введено недостаточно слов")
else:
    maxword(word,w0,lenw0)
    compare(word)