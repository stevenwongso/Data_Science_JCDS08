# numpy akses file = txt = number
# khusus untuk number apabila terdapat type lainnya maka tidak dapat dilakukan pengimportan
import numpy as np

# print(np.loadtxt('205.csv',skiprows=1,delimiter=';',unpack=True)) # unpack memisahkan per kolom

x = np.array ([0,1,2,3,4,5,6,7,8])
y = np.array([20,21,22,23,24,25,26,27])
np.savetxt('2051.csv', x, fmt= '%d' , header='X', delimiter=';')

xy = np.array(list(zip(x,y)))
xy = np.array(list(map(lambda x,y : [x,y], x, y)))
# print(xy)

np.savetxt('2052.csv', xy, fmt='%d', header='X;Y', delimiter=';', comments='') #comments untuk menghilangkan hashtag pada header
