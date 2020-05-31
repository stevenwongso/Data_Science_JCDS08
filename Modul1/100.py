# ini kode pertamaku
# print("Hello World!")
# print('Hello World!')
# print(12345)

# Shortcut penting  komentar CTRL + /
'''
single quote tiga kali bisa digunakan sebagai komentar
untuk beberapa baris
yang ingin dijadikan komentar
'''

# variables
# 2x=15000
# x=7500
# 3x =?
# nama variables tidak boleh dua kata, kalau ada dua kota digabungin
nama = "Andi"
usia = 21
# print('Halo,namaku', nama, 'usiaku', usia)
# print('Halo,namaku' + nama)
# print('Halo,namaku' + nama + 'usiaku' + usia) ga bisa karena usia bukan str
# print('Halo,namaku' + nama + 'usiaku' + str(usia))
# print(nama, usia)
# print(nama)
# print(usia)

# type variables
print (type(nama)) #str
print (type(usia)) #int

massa = 78.91
print (type(massa)) #float (desimal pake titik)

isMarried = True
print (type (isMarried)) #boolean nilai true atau false

# setiap variable harus ada valuenya
x = None
print (type (x)) #NoneType

y = 5j
print (type (y)) #complex j mengindikasikan bilangan imajiner