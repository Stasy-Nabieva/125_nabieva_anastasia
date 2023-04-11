print('Введите первое слово')
subst=input()
print('Введите второе слово')
st=input()
def search_substr(subst, st):
    if subst.lower() in st.lower():
        print('Есть контакт!')
    else:
        print('Мимо!')

search_substr(subst, st)