# # package untuk mengolah data berupa angka
# # NumPy

# import numpy as np

# # classic way
# x = [2,4,1,6,8,3,12,10]        
# # y = list(filter(lambda z : z % 2 ==0, x))
# # print(y)

# x = np.array(x)
# print(list(x[x%2 == 0]))


# # classic way
# x = [(1,2),(3,4),(5,6)]
# # y =list(map(lambda i : i[1], x))
# # print (y)

# x = np.array(x)
# print(list(x[:,1]))

import numpy as np

'''
NUMPY ARRAY == LIST dengan fitur plus plus
numpy array dapat melakukan filtering secara langsung
type dari seluruh data numpy harus sama
'''

# x = [1,2,3,4,5,6]
# y = np.array([1,2,3,4,5,6]) # bisa juga dalam bentuk tupple

# print(x)
# print(y)
# print(x[1])
# print(y[-1])
# print(x[::2])
# print(y[::2])
# print(y[y%2==0])

# a = {1,2,3,4,5,6}
# b = np.array({1,2,3,4,5,6})

# print(type(b))
# print(b)
# print(b[2])
# walaupun b type numpy array, tetap tidak memliki index


# a =[
#     [1,3,5,7],
#     [2,4,6,8],
#     [3,6,9,12]
# ]
# b = np.array(a)

# print(a[1][2])
# print(a[1,2]) # Error
# print(b[1,2])
# print(b[0:3,2])
# print(b[:,2]) 
# print(b[:,2:])
# print(b[::2,::2])
# print(b[:, [0,3]])
# print(b[:, [3,2,1,0]])

# a[0][0] = 'Andi'
# print(a)
# b[0,0] = 'Budi' # Error karena bukan number

# c = ['a', 'b', 'c']
# d = np.array(c)
# print(d) 
# d[0] = 'andi' #hanya satu karakter
# print (d)

# e = ['a','b','c','d',11, 12, 2000] # maks 4 karakter
# e = ['a','b','c','d',11, 12, 20] # maks 2 karakter
# f = np.array(e)
# print(f)
# f[0] = 190
# f[1] = 'Andi'
# print(f)

# numpy array ketika dibuat akan mencatat karakter terpanjang hanya untuk string
# ketika terjadi perubahan pada numpy array maka maksimum jumlah karakter = karakter terpanjang existing 

# a = [
#     [[1,2],[3,4],[5,6]],
#     [[7,8],[9,10],[11,12]],
#     [[13,14],[15,16],[17,18]]
# ]

# a = np.array(a)
# print(a[1,2,0])
# print(a[:,:,[1,0,0,1]])

# x = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

'''
tanpa numpy dan pakai numpy
jadikan x = [
    [3,2,1]
    [6,5,4]
    [7,8,9]
]
'''
#tanpa numpy
# for i in x :
#     x.append(i.reverse())
#     x.pop()

# x = list(map(lambda i : [i[2],i[1],i[0]], x))
# print(x)

#menggunakan numpy
# y = np.array(x)
# y = y[:,[2,1,0]]

# print(y)

# x = [1,2,3]
# y = [[1,2,3]]
# z = [[[1,2,3]]]

# x = np.array(x)
# y = np.array(y)
# z = np.array(z)

# print(x.ndim, x.dtype, x.size, x.itemsize, x.shape)
# print(y.ndim, y.dtype, y.size, y.itemsize, y.shape)
# print(z.ndim, z.dtype, z.size, z.itemsize, z.shape)
 
# ndim : berapa dimensi, dtype:tipe numpy array, size: berapa value, itemsize: berapa bit, shape : elemen per dimensi

# x = [[1,2],[3,4]]
# x = np.array(x)
# print(x.shape)

# # reshape : walaupun berubah size harus sama dan hasil perkalian atas elemen setiap dimensi sama
# a = x.reshape(4,1)
# print(a)
# print(a.shape)

# x = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

'''

hasil yang diharapkan
x = [
    [7,4,1]
    [8,5,2]
    [9,6,3]
    ]
x = [
    [3,6,9]
    [2,5,8]
    [1,4,7]
    ]
x = [
    [9,8,7]
    [6,5,4]
    [3,2,1]
    ]
x = [
    [1,4,7]
    [2,5,8]
    [3,6,9]
    ]
x = [
    [9,6,3]
    [8,5,2]
    [7,4,1]
    ]

'''
# no numpy dan with numpy

x = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#no numpy
'''
x = [
    [7,4,1]
    [8,5,2]
    [9,6,3]
    ]
'''
# list1 =[]
# list2 =[]
# list3 =[]
# for i in x :
#     list1.insert(0,i[0])
#     list2.insert(0,i[1])
#     list3.insert(0,i[2])
# x = [list1,list2,list3]
# print(x)


'''
x = [
    [3,6,9]
    [2,5,8]
    [1,4,7]
    ]
'''
# list1 =[]
# list2 =[]
# list3 =[]
# for i in x :
#     list1.append(i[0])
#     list2.append(i[1])
#     list3.append(i[2])
# x = [list3,list2,list1]
# print(x)
'''
x = [
    [9,8,7]
    [6,5,4]
    [3,2,1]
    ]
'''

# for i in x :
#     x.append(i.reverse())
#     x.pop()

# y=[]
# for i in x :
#     y.insert(0,i)

# print(y)
'''
x = [
    [1,4,7]
    [2,5,8]
    [3,6,9]
    ]
'''
# list1 =[]
# list2 =[]
# list3 =[]
# for i in x :
#     list1.insert(0,i[0])
#     list2.insert(0,i[1])
#     list3.insert(0,i[2])
# x = [list1,list2,list3]
# for i in x :
#     x.append(i.reverse())
#     x.pop()
# print(x)

'''
x = [
    [9,6,3]
    [8,5,2]
    [7,4,1]
    ]
'''

# list1 =[]
# list2 =[]
# list3 =[]
# for i in x :
#     list1.append(i[0])
#     list2.append(i[1])
#     list3.append(i[2])
# x = [list3,list2,list1]
# for i in x :
#     x.append(i.reverse())
#     x.pop()
# print(x)

# Pertemuan 28 Februari 2020

# y = np.arange(0,21,2)
# print(y)

# a = np.ones((3,3))  # matriks 1
# b = np.zeros((3,3)) # matriks 0
# b = np.zeros((3,3), dtype='int32') # bisa langsung di atur typenya
# print(a)
# print(b)

# print(a.dtype) #float64
# print(b.dtype) #float64

# a = a.astype('int32') # untukk merubah type
# print (a.dtype)
# print (a)

#cek di NumPy terkait type

# a = np.full((3,3), True) #sama seperti zeros dan ones namun valuenya bisa diatur ((size),value)
# a = np.full((3,3), True, dtype='int32') # True = 1, False = 0
# a[1,1] = 0 # angka yang bukan 0 akan berubah jadi True sedangkan 0 akan berubah jadi False
# print(a)
# print(a.dtype)

# contoh sifat boolean
# x = 0 # False
# x = 1 # True 
# if x :
#     print('ok')
# else :
#     print('Not OK')

# b = np.ones((3,3), dtype='bool')
# print(b)

# Generate random number di NumPy

# a = np.random.random(100)
# print(a)
# print(a.dtype)

# a = np.random.rand(3,100)
# print(a.shape)

# a = np.random.randint(5, size=(3,3))
# print(a)

# Spacing
# 1 arr = 10 elemen dimana elemennya tersusun dari 1-10 kemungkinan 1 2 3 4 5 6 7 8 9 10
# 1 arr = 100 elemen dimana elemen tersusun dari 1-10 kemungkinan 0.01, 0.02, ... , 10
# jarak atau space antar elemennya sama 

# a = np.linspace(1, 10, 10)
# b = np.linspace(0, 10, 100)
# print(a)
# print(b)


# Method NumPy

import numpy as np

# x = [4,2,3,6,7]
# x.sort()
# x.sort(reverse=True)
# print(x[::-1])
# print(x)

# x = np.array(x)
# x = np.sort(x)
# x = np.sort(x)[::-1]
# print(x)

# numpy bisa mengurutkan list dalam list

# x = [
#     [10,2,39,1],
#     [21,7,9,4],
#     [3,1,12,12]
# ]
# x = np.array(x)
# print(x)

# y = np.sort(x, axis=0) #urutskan by kolom
# y = np.sort(x, axis=1) #urutkan by baris
# print(y)

# z = np.sort(x) # default axis = 1

# z = np.sort(x, axis = None) # jadi satu dimensi yang diurutkan
# print(z)

# y = x.reshape(1,3, -1) # -1 digunakan untuk menyerhkan pada numpy penentuan angka shape terakhir
# y = x.reshape(1, -1)
# y = x.reshape(4, -1)
# print(y) 

#swapping method
# a = np.arange(9).reshape(3, -1)
# print(a)
# print(a[:,[2,1,0]])
# print(a[:,[0,0,0,0,0,0,0]])
# print(a[[2,1,0],:])

# concatenate : merger
# dimensi pada axis harus sama

# x = np.array([1,2,3]).reshape(3,1)
# y = np.array([4,5,6]).reshape(3,1) 
# y = np.array([4,5,6]).reshape(2,2) # error karena dimensi axisnya beda
# y = np.array([4,5,6]).reshape(2,1) # bisa di axis 0
# y = np.array([4,5,6]).reshape(3,2) # bisa di axis 1

# z = np.concatenate([x,y], axis=0) #concatenate kolom
# print(z)
# z = np.concatenate([x,y], axis=1) #concatenate baris
# print(z)

# a = np.vstack([x,y])
# print(a)
# a = np.hstack([x,y])
# print(a)

# x = [1,3,11,2,5,7]
# print(max(x))
# print(min(x))
# print(sum(x))
# print(sum(x)/len(x))
# print(x.index(max(x)))
# print(x.index(min(x)))


# y = np.array(x)
# apabila dimensi > 1 bisa ditambahkan axis juga

# print(y.max())
# print(y.min())
# print(np.argmax(y))
# print(np.argmin(y))
# print(y.sum()) 

# mean == rata-rata
# median == nilai tengah classic way(urutkan => dicari titik tengahnya)
# modus == value dengan frekuensi paling muncul

# print(np.mean(y))
# print(np.median(y))

# tanpa numpy dan tanpa bantuan library apapun tanpa google cari mean median modus 
# x = [2, 3, 5, 7, 1, 2, 5, 7, 4, 6, 9, 5, 5, 3]

# # mean
# mean = sum(x)/len(x)
# print(f'mean = {mean}')

# # median
# x.sort()
# if len(x) % 2 == 0 :
#     y = int(len(x)/2)
#     median = (x[y-1] + x[y])/2
# else :
#     y =int((len(x)-1)/2)
#     median = x[y]
# print(f'median = {median}')

# # modus
# a = set(x)
# frekuensi = map (lambda z: x.count(z),a)
# b = list(a)
# c = list(frekuensi)
# modus = b[c.index(max(c))]
# print(f'modus = {modus}')


# a = [1,2,3]
# print(a+a)
# print(a+2)  # error ga bisa karena tidak sejenis

# a = np.array(a)
# print(a+a)
# print(a+2) #setiap elemen dijumlahkan dengan 2
# print(a*2)
# print(a-2)
# print(a/2)

# a = [
#     [1,2],
#     [3,4]
# ]

# a = np.array(a)
# b = np.ones((2,2))
# c = np.zeros((2,2)) #matriks identitas penjumlahan
# print(a+b)
# print(a+c)

# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# a = np.array(a)
# print(a)
# print(a+a)

# a[a%2 !=0] += 10
# print(a)

# print(np.sqrt(4))
# print(np.cbrt(27))

# a = [1,4,9,16]
# a = np.array(a)
# b = np.array([1,8,27,64])
# print(np.sqrt(a))
# print(a ** (1/2))
# print(np.cbrt(b))
# print(b ** (1/3))

# e = bilangan euler 
# e : 2.718281828459045
# print(np.exp(1))

# e log 2,71 == e ^ ? =2.71 === 1
# 10 log 1000 == 10 ^ ? = 1000 ===3
# print(np.log(2.718281828459045)) #basis e
# print(np.log(np.exp(30)))
# print(np.log10(1000)) #basis 10

# print(np.pi)
# print(np.sin(np.pi))
# print(np.sin(np.pi/2))

'''
pi * 1 rad = 180 deg

       0     30    45     60     90
sin    0    1/2   v2/2   v3/2     1
cos    1    v3/2  v2/2   1/2      0
tan    0    v3/3    1     v3      -

'''

# sudut = np.array([0,30,45,60,90]) # belum berbentuk radian
# print(np.sin(sudut * (np.pi / 180)))

'''
Sistem persamaan linear

SPLDV

2x + y = 5
x + y = 7

|2 1||x| = |5|
|1 1||y|   |7|

a     c  =  b
'''

# a = np.array ([
#     [2,1],
#     [1,1]
# ])

# b = np.array([5,7])
# c = np.linalg.solve(a,b)
# x,y = np.linalg.solve(a,b)[0],np.linalg.solve(a,b)[1]
# print('x = ', x)
# print('y = ', y)

'''
SPLTV

x + y - z = -3
x + 2y + z = 7
2x + y + z = 4

'''
# a = np.array ([
#     [1,1,-1],
#     [1,2,1],
#     [2,1,1]
# ])
# b = np.array([-3,7,4])
# x,y,z = np.linalg.solve(a,b)[0],np.linalg.solve(a,b)[1],np.linalg.solve(a,b)[2]
# print('x + y + z = ',x+y+z)
# print('x = ', x)
# print('y = ', y)
# print('z = ', z)

# a = np.array([[3]])
# a = np.array([3]).reshape(1,-1)
# b = np.array([15000])
# x = np.linalg.solve(a,b)
# print(x)

# a = np.array([
#     [3,1],
#     [2,5]
# ])

# x = np.linalg.det(a)
# print(x)

# a = np.array([
#     [1,2,1],
#     [3,3,1],
#     [2,1,2]
# ])
# x = np.linalg.det(a)
# print(x)

# a = np.array([
#     [3,2],
#     [1,4]
# ])

# x = np.linalg.inv(a)

'''
dot product
|a|
|b| . |def|
|c|
'''

# x = np.array([[4,6],[9,4]])
# a = np.array([[1,0],[0,1]])
# print(x.dot(a))

'''
cross product
|a|    |d|    |xyz|
|b|  x |e| =  |abc| = (bf-ce)x - (af-cd)y + (ae-bd)z
|c|    |f|    |def|
'''

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.cross(a,b))


'''
transpose
'''
# a = np.array([
#     [1,2],
#     [3,4],
#     [5,6]
# ])

# print(a.transpose())
# print(a.T)