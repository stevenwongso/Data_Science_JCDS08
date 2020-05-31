# dictionary {key :value}
# x= {
#     'a':'Andi',
#     'b':'Budi',
#     'c':'Caca'
# }
# print(type(x))
# print(x['a'])
# print(x['c'])

# x= {
#     1:'Andi',
#     2:'Budi',
#     3:'Caca'
# }
# print(x[1])
# print (x.get('d', 'Maaf, data tidak ditemukan'))
# x[1] = "Budi"
# x['kota']='Jakarta'
# print(x)
# x.update({2: 'Toyota'}) #update tidak bisa untuk keys, kalau dipaksakan dengan mencocokan value dan mengganti keys akan menghasilkan yang baru
# x.update({5: 'Deni', 6: 'Susi'})
# print(x)
# x.pop('kota')
# del x[3]
# print(x)

# print (list(x.keys()))
# print (list(x.values()))

# a = [1,2,3]
# b = ['Andi', 'Budi', 'Caca']

# c = dict(zip(a,b))
# print(c)

# c= [[1,"Andi"], [2, 'Budi']]
# d = dict(c)
# print(d)

# x = { 'Senin':'Monday', 'Selasa':'Tuesday'}
# keys = list(x.keys())
# values = list(x.values())
# keys[keys.index('Senin')] = 1
# print(keys)
# d = dict(zip(keys,values))
# print(d)

# namaHari = {
#     'Senin':'Monday',
#     'Selasa' : 'Tuesday',
#     'Rabu' : 'Wednesday',
#     'Kamis' : 'Thursday',
#     'Jumat' : 'Friday',
#     'Sabtu' : 'Saturday',
#     'Minggu' : 'Sunday'
# }

# renungan dirumah, misalkan kita input nama hari maka menghasilkan bahasa inggrisnya
# misalkan input bahasa inggris, menghasilkan bahasa dari bahasa inggris itu

# cariValue = input("Silahkan masukkan kata yang ingin di translate ke bahasa inggris : ").capitalize()
# print (f"Bahasa inggris dari {cariValue} adalah {namaHari[cariValue]}")
# nk=namaHari.keys()
# nv=namaHari.values()
# namaHari2 = dict(zip(nv,nk))
# cariKey = input("Please write the words that would be translated into \'Bahasa\' : ").capitalize()
# print (f"{cariKey} translated into \'Bahasa\' equal {namaHari2[cariKey]}")
# print(f"{cariKey} translated into \'Bahasa\' equal {list(namaHari.keys())[list(namaHari.values()).index(cariKey)]}")

# x = {
#     'nama' : "Andi",
#     'usia' : 21,
#     3 : True,
#     'mobil' : ['Pajero', 'Innova'],
#     'coord' : {
#         'lat' : 112.9,
#         'lon' : 45.9,
#         'gps' : [112.9, 45.9]
#     }
# } 

# print (x['coord']['gps'][1])
# print (x['mobil'][0])