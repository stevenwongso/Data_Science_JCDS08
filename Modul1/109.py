# Function

# def namaFunc() :
#     programmes

# def halo() :
#     print('Halo!')
# halo()

# def hai(nama) :
#     print("Hai", nama)
# hai("Andi")
# hai("Budi")

# def kali(angka1, angka2) :
#     print (angka1 * angka2)
# kali(3,4)
# kali(9,8)

# hai(input("ketik nama Anda: ")) 

# def luaspersegi(sisi) :
#     luas = sisi ** 2
#     print(f'Luas persegi sisi = {sisi} adalah (luas)

# luaspersegi(2)
# luaspersegi(8)
# luaspersegi(7)

# Konverter USD <=> IDR

# def konvertusd():
#     y = float(input("Masukkan nominal : "))
#     print(f'{y} USD = {y * 13753.80} IDR')

# def konvertidr():
#     y = float(input('Masukkan nominal : '))
#     print(f'{y} IDR= {round(y / 13753.80, 2)} USD')
    
# print("Pilih metode konversi: \n 1. USD => IDR \n 2. IDR => USD")
# x = int(input ('Metode pilihan : '))
# if x == 1 :
#     konvertusd()
# elif x == 2 :
#     konvertidr()
# else :
#     print('Mohon maaf hanya melayani pilihan 1 ataupun 2 !')
    
# kurs = {1 : 13753.80, 2 : 0.00007}

# def konversi() :  
#     print("Pilih metode konversi: \n 1. USD => IDR \n 2. IDR => USD")
#     x = int(input ('Metode pilihan : '))
#     if x == 1 :
#         y = float(input("Masukkan nominal : "))
#         print(f'{y} USD = {y * kurs[x]} IDR')
#     elif x == 2 :
#         y = float(input("Masukkan nominal : "))
#         print(f'{y} IDR= {(y * kurs[x])} USD')
#     else :
#         print('Mohon maaf hanya melayani pilihan 1 ataupun 2 !')
#         konversi() #Recrusive function

# konversi()

# x = 99
# def halo() :
#     global x #tanpa keyword ini, variabel local didalam function tidak boleh merubah variable global yang diluar function
#     x = x + 5 
#     print (x)

# halo()
# print(x)

# return function

# x = 12
# def halo():
#     print('Halo')
# print(halo()) # none karena tidak memiliki value (tanpa return function)\
# x = 12
# def halo() :
#     return 12
# print(halo() * halo())

# def luascircle(rad) :
#     area = 3.14 * rad * rad
#     return area

# print(luascircle(7))
