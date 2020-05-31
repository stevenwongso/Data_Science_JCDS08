# string
# print("jum'at")
# print('jum\'at') # backslash untuk menunjukkan bahwa bukan akhir string
# print('Andi\tBudi') # backslash t untuk menunjukkan tab
# print('Andi\nBudi') # backslash n untuk menunjukkan new line

# x = 'Purwhadika'
# y = 'Startup & Coding School'
# print (x,y)

# z = '12'
# a = 12
# print (z + z)
# print (int(z) + int(z))
# print (a + a)
# print (str(a) + str(a))

x='ini string'
print(x.lower())
print(x.upper())
print(len(x))
# print(x.lower().islower())
# print(x.upper().islower())
# print(x.upper().isupper())
# print(x.lower().isupper())
# print(x[0])
# print(x[0:5])
# print(x[0:10:2])
# print(x.index('i')) #hanya urutan yang pertama

# z = 'Andi ditara'
# print(z.replace("a","o"))
# print(z.replace("di","na"))
# print(z.replace('a','o').replace('i','o'))


#template string

# nama = 'Budi'
# usia = 22
# print('Halo saya '+ nama + ' usia ' + str(usia))
# print('Halo saya %s usia %d' % (nama, usia)) # persen s untuk string persen d untuk digit
# print('Halo saya {} usia {}'.format(nama, usia)) #bebas tipe data
# print(f'Halo saya {nama} usia {usia}')

kata = 'Purwhadika Startup and Coding School'
#berapa huruf kata di atas
print(len(kata))
print(len(kata.replace(" ","")))

#ada berapa huruf a kata diatas?
print(kata.count("a"))
print(len(kata) - len (kata.replace('a', '')))

#ada berapa huruf p kata diatas?
print(kata.lower().count("p"))

kata = 'Hari ini Hari tidak masuk sekolah karena hari libur'
#berapa kata hari
print((len(kata)-len(kata.lower().replace('hari','')))/ len('hari'))