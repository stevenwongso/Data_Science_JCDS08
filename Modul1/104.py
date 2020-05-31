# a = 10
# a = a + 1
# a += 1
# print (a)
# a -= 2
# print (a)
# a *= 10
# print (a)
# a /= 103
# print (a)
# a **= 2
# print (a)

#list
# student = ['Andi','Budi','Caca','Andi','andi']
# print(type(student))
# print(student)
# print(student[0])
# print(student[2])
# print(type(student[2]))
# # kalau misalkan jumlah elemen banyak, maka untuk memanggil elemen terakhir
# print (student[len(student)-1])
# print(student [-1] )

# print(student.index('Budi'))
# print(student[student.index('Budi')])
# print(student.count('Andi'))
# print(student[0:])
# print(student[:5])
# print(student[::-1])
# print('Budi' in student)
# print('Budi' in student[::2])

# # most likely element dari list satu kategori 

# hari = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']

# print(hari[0])
'''
Sekarang hari Rabu, hari apakah 100 hari lagi?
Sekarang hari Rabu, hari apakah 100 hari yang lalu?
'''
# waktu = int(input('waktu yang dibutuhkan :'))
# print(waktu, 'hari lagi adalah hari', hari[(waktu+hari.index('Rabu'))%7])
# print(waktu, 'hari yang lalu adalah hari', hari[hari.index('Rabu')-(waktu % 7)])

# cara yang lebih simple

# now = input("Hari ini hari apa? ").capitalize()
# harilagi = int(input("Berapa hari lagi ? "))
# sisaHari = harilagi % len(hari)
# hariYgDicari= hari[(hari.index(now)+sisaHari)% 7]
# print(f'{harilagi} hari lagi adalah hari {hariYgDicari}')

# bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

# now = input("Bulan apa sekarang? ").capitalize()
# blnlagi = int(input("Berapa bulan lagi ? "))
# sisabln = blnlagi % len(bulan)
# blnYgDicari= bulan[(bulan.index(now)+sisabln)% 12]
# print(f'{blnlagi} bulan lagi adalah bulan {blnYgDicari}')

# x= [0,1,2,3,4,5,6,7,8,9]
# y= range (0,1000000,100000)#start, stop, step
# print(y)
# y=list(y)
# y.append(123)
# y.insert(0, True)
# y.insert(1, True)
# print(y)
# y.pop()
# y.remove(True)
# print(y)
# y.insert(0,67)
# print(y)
# y.reverse()
# print(y)
# y.sort()
# print(y)
# y.sort(reverse=True)
# print(y)
# a = 'Purwhadika'
# b = [1,2,3]
# c = 12345 # number tidak dapat dijadikan list secara langsung
# print(list(a))
# print(list(str(c)))

# angka = [52, 2, 4, 6, 7, 8 ,9]
# # output [2,4,52,6,7,8,9]
# c = angka[:3]
# print(c)
# c.sort()
# angka[0:3] = c
# print(angka)

# a = ['apel', 'belimbing', 'cari']
# b = [1,2,3]
# a.extend(b)
# b.extend(a)

# print (a)
# print(a + b)
# print(b + a)
# print(a * 2)
