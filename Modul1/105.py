# x = [[1,2,3], [4,5,6]]
# print(len(x))

# print(x[0])
# print(x[1])

# print(x[0][0])
# print(x[1][2])
# y = [x] # Triple List
# print (y)
# print(y[0][1][0])
# print([y[0][0][0], y[0][1][2]])

# Tuple:immutable
# x=(1, 2, 3, 4, 5)
# # x[0] = "Andi" error karena tuple ga boleh diedit
# print(type(x))
# print(x[0:3])

# #cara untuk mengubah isi dalam tuple
# y = list(x)
# y[0] = 'Andi'
# x = tuple(y)
# print(x)
# print('Andi' in x)

# a = ((1,2), (3,4), (5,6), (7,8))


# # (3,4), (1,2), (7,8), (5,6)
# a = (a[1], a[0], a[3], a[2])
# print(a)

# # ((4,3), (2,1), (8,7),(6,5))
# a =list(a) 
# a = [list(a[0]), list(a[1]), list(a[2]), list(a[3])]
# a = ((a[0][1],a[0][0]), (a[1][1],a[1][0]), (a[2][1],a[2][0]), (a[3][1],a[3][0]))
# print(a)

# # ((1, 3), (2, 4), (5, 7), (6, 8))
# a = list(a)
# a = [list(a[0]), list(a[1]), list(a[2]), list(a[3])]
# a = ((a[0][0],a[1][0]), (a[0][1],a[1][1]), (a[2][0],a[3][0]), (a[2][1],a[3][1]))
# print(a)

# keunikan Tuple
# x = ("Andi") #str bukan tupple
# x = "Andi", #tupple
# print(type(x))
# y = "Andi", "Budi", "Caca" #tupple

# Tuple bisa ditambahkan apabila sesama tuple
# x = (1,2,3)
# print(x + x)
# print(x * 5)
# print(1 in x)
# print(1 not in x)

# del x #hapus variable
# print (x) #error karena sudah dihapus di perintah sebelumnya

x = [
(1, ['a','b']),
(3,4)
]
x[0][1][0] = "Andi" #bisa karena yang diubah berada dalam list, meskipun list tersebut berada dalam tuple tapi bukan kekuasaan tupple lagi jadi tetep bisa diubah
print(x) 