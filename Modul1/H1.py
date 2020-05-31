# 01 Intro to Python

# Solved it 0

# tanpa penginputan
# nama = "Baron"
# umur = 20
# kelamin = "Pria"
# pekerjaan = "Guru"
# print("Nama kamu? :", nama)
# print("Umur kamu? :", umur)
# print("Kelamin kamu? :", kelamin)
# print("Pekerjaan kamu? :", pekerjaan)
# print("Nama :", nama)
# print ("Umur :", umur)
# print ("Kelamin :", kelamin)
# print ("Pekerjaan :", pekerjaan)

# menggunakan input
# nama = input("Nama kamu? : ");
# umur = input("Umur kamu? : ");
# kelamin = input("Kelamin kamu? : ");
# pekerjaan = input("Pekerjaan kamu? : ");
# print("Nama : " + nama);
# print("Kelamin : " + kelamin);
# print("Pekerjaan : " + pekerjaan);\
# print("Umur : " + umur);

# x = 'Halo Dunia';
# print(len(x));
# print(x.index('Dunia'));
# print(x.split(' '));
# print(x.lower());
# print(x.upper());
# print(x.capitalize());

# import math
# print(math.pi);
# print(math.fabs(-4.7));
# print(math.pow(8, 2));
# print(math.sqrt(64));
# print(round(4.7));
# print(round(4.4));
# print(math.floor(4.7));
# print(math.ceil(4.4));

# singleQuotes = 'single quotes';
# doubleQuotes = "double quotes";
# combineQuotes = "wrap lot's of other quotes"
# print(singleQuotes);
# print(doubleQuotes);
# print(combineQuotes);

# text = "I'm Baron, nice to meet you";
# print(text[1]);
# print(text[2:]);
# print(text[:4]);
# print(text[2:5]);
# print(text[:]);

# Solved it #1
# import math
# x = input ("x = ")
# y = input ("y = ")
# z = input ("z = ")
# w = math.pow((int(x) + int(y) * int(z)) / (int(x) * int(y)), 2)
# print (w)

# Solved it #2
# import math
# x = input ("Silahkan masukkan angka berapapun : ")
# print("Kuadrat dari 4 =", math.pow(int(x), 2))

# Solved it #3
# import math
# x = 485
# print(math.floor(x/360), "Tahun", math.floor((x % 360)/30), "Bulan", math.floor(((x % 360) % 30) / 7 ), "Minggu", ((x % 360) % 30) % 7, "Hari" )

# Solved it #4
# ratio = 0.4
# jumlah = 49

# budi = jumlah / (ratio+1)
# andi = jumlah - budi
# print(f'Umur Andi 2 tahun lagi {andi + 2} Umur Budi 2 tahun lagi {budi + 2}')

# Solved it #5
# kata = input('Masukkan Kata :')
# huruf = input ('Masukkan Huruf :')
# jumlahhuruf= (len(kata.lower())-len(kata.lower().replace(huruf,'')))/len(huruf)
# print(f'{kata} memiliki huruf \'{huruf}\' sebanyak {jumlahhuruf} buah')

'''
Solved it#6

60 x + 40 x =120
100 x = 120
x=120/100
'''
# import math
# jaraktotal = 120
# keca =60
# kecb =40
# start= 9

# waktutempuh= jaraktotal / (keca+kecb)
# jam= math.floor((start * 60 + waktutempuh * 60) / 60)
# menit = (start * 60 + waktutempuh * 60) % 60
# print(f'A dan B berantakan pada saat jam {jam} lewat {menit}')
