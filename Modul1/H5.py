# 05 lambda exp, tuples, etc
# Solved it! 1
def saring(kata) :
    return cari in kata
listword = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari ayam']
cari = input('Search : ').lower()
for item in range(len(listword)):
    listword[item] = listword[item].lower()
listword = list(filter(saring, listword))
for item2 in range(len(listword)) :
    listword[item2] = listword[item2].capitalize()
print(listword)