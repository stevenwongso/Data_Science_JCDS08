# if-else statement

# if condition :
#     program
# elif condition : 
#     program
# else program

# x = 11

# comparison operator
# == > < >= <= !=

# print(x == 12)
# print(x != 12)
# print(x > 12)
# print(x >= 12)

# if x==12:
#     print('Nilai x == 12')
# elif x>12 :
#     print('Bilai x > 12')
# else :
#     print('Nilai x < 12')

#buatlah sebuah file python yang dapat membedakan ganjil dan genap

# x = int(input("Silahkan masukan angka yang ingin dicoba : "))
# if x % 2 == 0 :
#     print(f'angka {x} merupakan bilangan genap')
# else :
#     print (f'angka {x} merupakan bilangan ganjil')


# namaHari = {
#      'Senin':'Monday',
#     'Selasa' : 'Tuesday',
#     'Rabu' : 'Wednesday',
#     'Kamis' : 'Thursday',
#     'Jumat' : 'Friday',
#     'Sabtu' : 'Saturday',
#     'Minggu' : 'Sunday'
# }
# cari = input("Ketik/write : ").capitalize()
# if cari in list(namaHari.keys()) :
#     print (f"Bahasa inggris dari {cari} adalah {namaHari[cari]}")
# else :
#     print(f"{cari} translated into \'Bahasa\' equal {list(namaHari.keys())[list(namaHari.values()).index(cari)]}")

# TRUE dapat di declare sebagai memiliki value
# FALSE dianggap tidak memiliki value atau 0

# x = 0 

# if x :
#     print('OK')
# else :
#     print("Not OK")

# x = True
# y = False
# print(x or y)


# if x and y:
#     print('and masih jomblo, tapi sudah bekerja')
# if not(x) and y:
#     print('Anda tidak jomblo & sudah kerja !')
# if x and not (y) :
#     print('Anda jomblo + nganggur!')
# else :
#     print('Anda punya pasangan & tapi tidak ada kerjaan')

# a = float(input('Ketik angka 1 : '))
# b = input('Ketik operator (+ - x /): ')
# c = float(input('Ketik angka 2 : '))

# if b == '+' :
#     print (f'Hasil penjumlahan {a} {b} {c} = {a + c}')
# elif b == '-' :
#     print (f'Hasil pengurangan {a} {b} {c} = {a - c}')
# elif b == "x" :
#     print (f'Hasil perkalian {a} {b} {c} = {a * c}')
# else :
#     print (f'Hasil pembagian {a} {b} {c} = {a / c}')

# massa = int(input(" Masukkan Massa (kg) : "))
# tinggi = int(input(" Masukkan Tinggi (cm) : "))
# print("Massa", massa, "kg", "& Tinggi", float(tinggi)/100,"m")
# IMT = massa/((tinggi/100) ** 2)
# if (IMT < 18.5):
#     print("IMT =", IMT, "Berat Badan Kurang" )
# elif (IMT >= 18.5 and IMT <= 24.9) :
#     print("IMT =", IMT, "Berat Badan ideal" )
# elif (IMT >= 25.0 and IMT <= 29.9) :
#     print("IMT =", IMT, "BB Berlebih" )
# elif (IMT >= 30.0 and IMT <= 39.9) :
#     print("IMT =", IMT, "BB Sangat Berlebih" )
# else :
#     print("IMT =", IMT, "Obesitas" )

# If else statement in one line
# VALifTrue if condition else VALifFALSE
# x = 12
# print('Genap' if x % 2 == 0 else "Ganjil")

# x = 11

# print ("x = 12" if x == 12 else ("x > 12" if x > 12 else "x < 12"))

# username = ["Andi", "Budi", "Caca"]
# password = [ "12345", "8989abc","098poi"]

# user = input ("Ketik username : ").capitalize()
# pwd = input ("Ketik Password : ")

# if user in username and pwd == password[username.index(user)] :
#     print (f'Selamat {user}, anda telah berhasil login')
# elif user in username and pwd != password[username.index(user)] :
#     print ('Password Salah!')
# else :
#     print (f'Nama {user} tidak terdaftar!')

