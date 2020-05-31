# looping
# While\
# while condition :
#   programmes

# x = 0
# while x <= 2:
#     print('x = = 2')
#     x = x + 1

# x = 0
# while x <= 1 :
#     print (x)
#     x += 

# x = list(range(0,10000))
# i = 0
# while i < len(x)
# print(x[i])
# i +=1

# x = list(range(0,10000))
# i = 0
# while i < len(x) :
#     x[i] = x[i] * 2
#     i += 1

# print(x)

# i = 0
# while i == 0:
#     password = input('Masukkan Password anda : ')
#     if password == '12345' :
#         print ('Password benar, welcome back ! \n' )
#         i = i + 1
#     else :
#         print ('Mohon maaf password salah ! \n')

# password = '12345'
# inputuser = ''
# while inputuser != password :
#     inputuser = input ('Ketik password : ')
#     if inputuser != password :
#         print ('Password Salah!')
#     else :
#         print ('Password Benar!')

# kesempatan = 5
# while kesempatan != 0 :
#     password = input('Masukkan Password anda : ')
#     if password == '12345' :
#         print ('Password benar, welcome back ! \n' )
#         kesempatan = 0
#     else :
#         print (f'Mohon maaf password salah ! ')
#         kesempatan -= 1
#         if kesempatan == 0 :
#             print('Kesempatan anda telah habis, akun terblokir \n')
#         else :
#             print (f'Sisa kesempatan : {kesempatan} \n')

# x = 'Aliando'
# #  aloandi
# i = 0
# while i < len(x) :
#     if x[i] == 'i' :
#         x = x[:i] + 'o' + x[i+1:]
#     elif x[i] == 'o' :
#         x = x[:i] + 'i' + x[i+1:]
#     i += 1

# print (x)

# x = [
#     {'nama' : 'Andi', 'kota' : 'BSD'},
#     {'nama' : 'Budi', 'kota' : 'Jakarta'},
#     {'nama' : 'Caca', 'kota' : 'Bandung'}
# ]
# i = 0
# j = 0
# while i < len(x) :
#     print(x[i]['nama'])
#     i += 1
# while j < len(x) :
#     print(x[j]["kota"])
#     j += 1

# x = [1, 2, 3, 4, 5]

# for elemen in x :
#     print(elemen)

# for i in x :
#     print(i)

# for i in range(1,10,2):
#     print(f'Index ke-{i}')

# nama = ['Andi', 'Budi', 'Caca']
# for name in nama:
#     print(f'{nama.index(name) + 1} - {name}')

# for num in range(10,0,-1) :
#     print(num)

'''
fizzbuzz
output 1-100
kelipatan 3 = 'Fizz'
kelipatan 5 = 'Buzz'
kelipatan 3 dan 5 ='FizzBuzz'
'''
# def fizzbuzz(num) :
#     for i in range(1, num + 1) :
#         if i % 3 == 0 and i % 5 == 0 :
#             print("FizzBuzz")
#         elif i % 3 == 0 :
#             print('Fizz')
#         elif i % 5 == 0 :
#             print('Buzz')
#         else :
#             print (i)

# x = int(input('Silahkan masukkan angka yang diinginkan : '))
# fizzbuzz(x)

a = ['a','b','c','d']
#bikin function tanpa menggunakan reverse, step, list(reversed(a))

# def membalik(x) :
#     temp = []
#     for i in range((len(x))):
#        temp.append(x[len(x)-1-i]) #atau 
#     #    temp.insert(0, x[i])
#     return temp
# print(membalik(a))

# def balik(x) :
#     for i in range(round(len(x)/2)) :
#         y = x[i]
#         x[i]= x[len(x)-1-i]
#         x[len(x)-1-i] = y
#     return x
# print(balik(a))

# def pangkat(x,y) :
#     z = x
#     for i in range(y-1) :
#         x *= z
#     return x
# print(pangkat(2,3))

# def pangkat2(x,y) :
#     if y == 1:
#         return x
#     else :
#         return x * pangkat(x, y-1)
# print(pangkat2(2,3))

# star = ""
# for i in range (5) :
#     star += " * "
#     print (star)

# num = ''
# for i in range (5):
#     star += f' {str(i+1)} '
#     print (star)

'''
for row in x:
    for col in row:
        print(col)
'''

# x = ' '
# for i in range (0, 6) :
#     for j in range (0, i) :
#         x += (str(i) + " ")
#         print(x)
#     i += 1
#     x += '\n'
