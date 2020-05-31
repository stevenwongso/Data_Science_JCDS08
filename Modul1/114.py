#  Class dan Object

# class mobil:
    # statis
    # warna = Merah
    # tipe = SUV 
    
    # dynamic
    # def __init__(self, warna, tipe, seat) : #special variable di python : init, main, menu, name
    #     self.warna = warna
    #     self.tipe = tipe
    #     self.seat = seat
    # def mahal(self) :
    #     if self.seat <= 4:
    #         return False
    #     else :
    #         return True
#  warna dan tipe merupakan property
#  property dapat berupa function : method

# print(mobil)
# print(type(mobil))
# print(mobil.warna)
# print(mobil.tipe)

# pajero = mobil('Hitam','SUV',6)
# print(pajero.warna, pajero.tipe, pajero.mahal())

# agya = mobil('Merah','Hatchback',4)
# print(agya.warna, agya.tipe)

# agya2 = mobil('Kuning','Hatchback',4)
# print(agya2.warna,agya2.tipe)

'''
class pizza
props= ukuran: 35 cm, topping: bebas ditentukan object
'''

# class Pizza :
#     def __init__(self, topping):
#         self.ukuran = '35 cm'
#         self.topping = topping
#     def harga(self) :
#         return len(self.topping)*10000

# pizzaA = Pizza('jagung')
# pizzaB = Pizza('Keju')

# print(pizzaA.ukuran, pizzaA.topping, pizzaA.harga())
# print(pizzaB.ukuran, pizzaB.topping, pizzaB.harga())

'''
class x

obj,luaspersegi(x)
'''

# class x :
#     y = [1,2,3,4,5]
#     z = {'nama': 'Andi'}
#     def luaspersegi(self,sisi):
#         return sisi * sisi
#     def kelilingpersegi (self,sisi):
#         return 4 * sisi
# obj = x()
# print (obj.luaspersegi(12), obj.kelilingpersegi(12), obj.y[0], obj.z['nama'])

# class A :
#     def __init__(self, name, city):
#         self.nama = name
#         self.kota = city
#     # nama = 'Andi'
#     # alamat = 'Jakarta'

# class B(A):
#     pass # class B akan sama dengan A tanpa ada tambahan
#     # nama = 'Andi' dan alamat = 'Jakarta' #bisa diambil dari kelas a => inheritance  
#     gaji ='Rp 10.000.000'

# class C(A) :
#     def __init__(self, name, city) :
#         A.__init__(self, name, city)

# class D(A) :
#     def __init__(self, name, city) :
#         super().__init__(name, city)

# objB = B('Budi', 'Kediri')
# objC = C('Deni', 'Manokwari')
# objD = D('Ani', 'Manokwari')

# print (objB.nama, objB.kota)
# print (objC.nama, objC.kota)
# print (objD.nama, objD.kota)

# class Manusia:
#     def __init__(self, nama) :
#         self.nama = nama

# class Pria(Manusia):
#     def __init__(self, nama) :
#         Manusia.__init__(self, nama)
#         self.gender = 'Pria'

# class Bencong(Pria):
#     def __init__(self, nama):
#         Pria.__init__(self,nama)
#         self.feminime = True

# class Wanita(Manusia):
#     def __init__(self, nama) :
#         Manusia.__init__(self, nama)
#         self.gender = 'Wanita'


# Andi = Bencong('Andi')
# print(Andi.nama, Andi.gender, Andi.feminime)

# class A :
#     nama = 'Andi'

# class B :
#     jabatan = 'Supervisor'

# class C(A,B) :
#     alamat = 'jakarta'

# objC = C()
# print(objC.nama, objC.jabatan, objC.alamat)

# class A() :
#     nama = "Andi"
#     def __init__(self,kota) :
#         self.kota = kota
# class B(A):
#     def __init__(self,kota, prodi) :
#         A.__init__(self,kota)
#         self.prodi=prodi
#     def test(self) :
#         return True


# objA = A('Jakarta')
# print (objA.nama, objA.kota)

# objB = B('Jakarta', 'Teknik Sipil')
# print (objB.nama, objB.kota, objB.prodi, objB.test())
# print(getattr(objB, 'nama'), getattr(objB, 'kota'), getattr(objB, 'prodi'))
# print (hasattr(objB, 'prodi'))
# objB.alamat= 'BSD'
# setattr(objB,'kampus', 'UnivA')
# print(objB.kampus, objB.alamat)
# print(hasattr(objB, 'kampus'))
# delattr(objB, 'kampus')
# print(hasattr(objB, 'kampus'))
# print(vars(objB))
# print(list(vars(objB).keys())) #yang dipanggil oleh vars hanya yang memiliki value dan non method
# print(list(vars(objB).values()))


# x = {
#     'kota' : 'Jakarta',
#     'prodi' : 'Teknik Sipil',
#     'alamat' : 'BSD'
# }
# b = list(x.keys())
# c = list(x.values())

# class test:
#     a = 0

# for i in b :
#     setattr(test, i, c[test.a])
#     test.a += 1

# print(test.kota, test.prodi, test.alamat)

# ketika menginport suatu file dapat menjadi object

# import tes114 as x
# print (x.nama)
# print (x.tesfunc('Budi'))
# objA = x.A()
# print(vars(objA))
# print(objA.nama)
# print(x.d)

# from tes114 import jsonku
# jsonku = jsonku('tes114.json')
# print(jsonku.buka())

# import datetime

# x= datetime.datetime.now()

# # print(x)
# print(x.strftime('%A')) # nama hari
# print(x.strftime('%d')) # tanggal
# print(x.strftime('%B')) # Nama bulan
# print(x.strftime('%m')) # index bulan
# print(x.strftime('%Y')) # tahun full year
# print(x.strftime('%y')) # tahun 2 digit paling belakang
# print(x.strftime('%H')) # sistem 24
# print(x.strftime('%I')) # sistem 12
# print(x.strftime('%p')) # AM / PM
# print(x.strftime('%M')) # menit
# print(x.strftime('%S')) # second

'''
bikin package waktu
nanti bisa diakses
ketik di import saya dapat hari dan bulan
 
misal 
import idwaktu
x= idwaktu.waktu()
print(waktu.hari()) => rabu
print(waktu.bulan()) => februari
'''
from tes1141 import waktu
print(waktu.hari())
print(waktu.bulan())