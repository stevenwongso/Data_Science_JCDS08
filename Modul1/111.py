# Lambda function atau anonymous function
# Lambda function pasti return
# a = lambda c : c**2 # c = parameter, : = return
# print(a(3))

'''
def b (w,x):
    return w**x
'''
# b = lambda c,d : c**d
# print(b(2,3))

'''
def b(x):
    if x % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"
print (b(2))
'''
# a = lambda x : 'Genap'if x % 2 == 0 else 'Ganjil'
# print (a(81))

# def f(x) :
#     return lambda a : a ** x

# print (f(3)(2))

# pangkat2 = f(2)
# print (pangkat2(3))

# x = [1, 2, 3, 4, 5]
# dengan lambda function dia bisa ngeprint setiap elemen dari x
# z = [print(i) for i in x] # pengulangan for - in 1 line
# a = lambda x :  [print(i) for i in x]
# a(x)
# s = lambda : 5 # lambda tanpa parameter

# listku = [
#     lambda : 1,
#     lambda : 2,
#     lambda : [4,5,6]
# ]

# print(listku[0]())
# print(listku[2]()[1])


# map ,  filter, and reduce

# map (function, iterable value) = melakukan function untuk setiap elemen iterable value

x= [1, 2, 3, 4, 5]

# for i in range(len(x)) :
#     x[i] += x[i]
# print (x)

# def jumlah (i):
#     return i + i
# y = map (jumlah, x)
# print(list(y))

# y = map (lambda i : i + i, x)
# print (list(y))

# buat sehingga seperti ini [1, 8, 27, 64, 125]
# y = map (lambda a: a**3, x)
# print(list(y))

# x = [1, 2, 3, 4, 5]
# y = [5, 4, 3, 2, 1]
# w = [2, 2, 2, 2, 2]

# a = map(lambda x,y,w : x + y + w  , x, y, w)
# print(list(a))

# a = map(lambda x,y : x ** y, x, y )
# print(list(a))

# a = map(pow, x, y)
# print(list(a))

# Filter(function, iterable value) notes: return berupa True/False (Boolean)

# x = [3, 5, 7, 4, 8 , 9, 2]
# y = []
# for i in x :
#     if i > 4 :
#         y.append(i)
# print(y)

# a = filter(lambda a: True if a > 4 else False, x)
# print(list(a))
# b = filter(lambda a: a > 4, x)
# print(list(b))

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [1,2,12,4,5,13,7,8,19,10]
# z = []
# for i in x :
#     if i in y:
#         z.append(i)
# print(z)
    
# a = filter (lambda b: b in x, y)
# print(list(a))

data = list(range(0, 101))

# filter=> keluarnya hanya bilangan prima

# def prima(x) :
#     if x > 1 :
#         if x == 2:
#             return True
#         else :
#             for item in range (2, x):
#                 if x % item == 0 :
#                     return False
#             return True
#     else:
#         return False

# a = filter(prima, data)
# print(list(a))

# a = filter ((lambda a : True if a > 1 and  [ a % i == 0 for i in range(2, a)] else False),data)
# print(list(a))

# Reduce

# angka = [1,2,3,4,5]

from functools import reduce
# # 1+2+3+4+5
# z= reduce(lambda x,y:x+y, angka)
# print(z)
# # 1*2*3*4*5
# b= reduce(lambda x,y:x*y, angka)
# print(b)

# reduce untuk menentukan nilai max dan min dari sebuah list

# angka = [1, 2, 3, 4, 5]
# z = reduce (lambda x,y: x > y , angka)
# print(z)
 
#fungsi break ; berhenti
# i = 1
# while i < 6 :
#     print(i)
#     if i == 3 :
#         break
#     i += 1

# fugsi continue : skip
# i = 0
# while i < 6 :
#     i += 1
#     if i == 3 :
#         continue 
#     print(i)

# x = [1,2,3,4,5]

# a = filter(lambda i : i % 2 == 0, x)
# b = map(lambda i: i**2, a)
# print(list(b))

# c = map (lambda i : i**2, filter(lambda j:j % 2 == 0, x))
# print(list(c))
# print(list(c)) ga bisa karena c merupakan objek ketika udah diprint ke list c, maka object c telah diambil kefunction sebelumnya