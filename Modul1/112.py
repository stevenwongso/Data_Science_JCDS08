# membuka file lain

# 'r' = read
# myfile = open('112.txt','r') # apabila berada di folder yang sama
# myfile = open('./Files/112.txt','r') # apabila selevel(.) menginidikasikan folder dimana .py berada (/) untuk masuk ke folder tersebut
# myfile = open('./../files/112.txt', 'r') # (..) mengidikasikan kita keluar folder dimana  .py kita berada
# print(myfile)
# print(myfile.readable()) # menentukan apakah file dapt terbaca atau tidak
# print(myfile.read())

# file yang sering di akses excel,csv,json, database, API
# print(myfile.readline()) #membaca line pertama
# print(myfile.readlines()) 

# for i in myfile.readlines():
#     print (i.replace('\n', ''))

# 'w' = Write
# myfile = open('112.txt','w')
# myfile.write('Andi') #kalau pake w overwrite

# 'a' = Append
# myfile = open('112.txt','a')
# myfile.write('\nBudi')

# rb = readbyte = membaca sebagai binary fie

# myfile = open('17.py','w') #menambahkan file python
# myfile.write('print("Hello!")')

# import os
# os.remove('17.py')

# myfile = open('112.csv','r')

# # cara ubah jadi dictionary melalui file csv 
# data = []
# for i in myfile.readlines()[1:]:
#     no = int(i.split(';')[0])
#     nama = i.split(';')[1].replace('\n', '')
#     x ={'no' : no, 'nama' : nama}
#     data.append(x)
# print(data)

# menambahkan data baru

# cara steven
# x =  1
# a = []

# myfile = open('112.csv','r')
# for i in myfile.readlines()[1:]:
#     no = int(i.split(';')[0])
#     a.append(no)
# nomor = a[len(a)-1]

# myfile = open('112.csv','a')

# while x != 0 :
#     user = input('Ketik nama:')
#     nomor += 1
#     myfile.write(f'\n{nomor};{user}')
#     ulang = input('Ingin menambahkan lagi? (y/n) : ')
#     if ulang =='n':
#         x = 0
#         myfile = open('112.csv','r')
#         print(myfile.read())

# cara kak lintang
# data = []
# myfile = open('112.csv','r')
# for i in myfile.readlines()[1:]:
#     no = int(i.split(';')[0])
#     nama = i.split(';')[1].replace('\n', '')
#     x ={'no' : no, 'nama' : nama}
#     data.append(x)

# user = input("Ketik nama : ")
# new = {'no' : data[-1]['no'] + 1, 'nama' : user}
# data.append(new)
# print(data)
# myfile = open('112.csv','w')
# myfile.write('no;nama\n')


# myfile = open('112.csv','a')
# for i in data:
#     myfile.write(
#         f'{i["no"]};{i["nama"]}\n'
#     )

# x = 1
# while x != 0 :
#     print('Welcome, pilih menu :')
#     print(' 1. Signup')
#     print(' 2. Login')
#     pilihan = input("Ketik opsi (1/2) : ")
#     if pilihan == "1" :
#         data = []
#         myfile = open('112.csv','r')
#         for i in myfile.readlines()[1:]:
#             no = int(i.split(';')[0])
#             nama = i.split(';')[1].replace('\n', '')
#             x ={'no' : no, 'nama' : nama}
#             data.append(x)
#         user = input("Ketik nama : ")
#         new = {'no' : data[-1]['no'] + 1, 'nama' : user}
#         data.append(new)
#         myfile = open('112.csv','w')
#         myfile.write('no;nama\n')
#         myfile = open('112.csv','a')
#         for i in data:
#             myfile.write(
#                 f'{i["no"]};{i["nama"]}\n'
#             )
#         print(f"\n Nama anda terdaftar dengan nomor {data[len(data)-1]['no']} \n")
#         break
#     elif pilihan == "2" :
#         data = []
#         myfile = open('112.csv','r')
#         for i in myfile.readlines()[1:]:
#             no = int(i.split(';')[0])
#             nama = i.split(';')[1].replace('\n', '')
#             x ={'no' : no, 'nama' : nama}
#             data.append(x)

#         nama = input ('Ketik nama : ')
#         nomor =int(input ('Ketik nomor : '))
#         if nama.capitalize() == data[nomor-1]['nama'] :
#             print( "\nSukses Login\n")
#         else :
#             print("\nLogin Gagal\n")
#         break
#     else :
#         print('Pilihan salah silahkan coba lagi \n')

# JSON (JavaScript Object Notation)
# JavaScript Object Notation
# 1. mirip list / dictpython
# 2. semua key & value (string) must be in ""
# 3. dalam satu file jason hanya boleh satu list/dictionary)
# otomatis rapih : prettify JSON
#  {} = object []=Array

# myjson = open('112.json', 'r')
# print(myjson.readable())
# myjson = myjson.readlines()
# print(myjson)

# cara mudah mengakses csv dan json
# ada library yang telah terinstall

# import csv
# baca csv
# with open('112.csv', 'r') as mycsv :
#     # reader = csv.reader(mycsv, delimiter =';')
#     # print(list(reader))
#     reader = csv.DictReader(mycsv, delimiter =';')
#     data=[]
#     for i in reader:
#         data.append(dict(i))
# print(data)

# write csv
# with open('112.csv', 'w') as mycsv :
#     writer = csv.writer(mycsv, delimiter = ';')
#     writer.writerow(['14', 'Rudi'])
# with open('112.csv', 'a', newline='') as mycsv :
    # writer = csv.writer(mycsv, delimiter = ';')
    # writer.writerow(['14', 'Rudi']) #satu list doank
    # writer.writerows([[22, 'Rudi'], [23, 'Budi']])
    # writer = csv.DictWriter(mycsv, delimiter = ';', fieldnames =['no', 'nama']) # Pastikan key dideclare difieldnames dan ikutin di csv
    # writer.writerow({'no' : 33, 'nama' : 'Dedi'})
    # writer = csv.DictWriter(mycsv, delimiter = ';', fieldnames =['no', 'nama']) # Pastikan key dideclare difieldnames dan ikutin di csv
    # writer.writerow({'no' : 33, 'nama' : 'Dedi'})
    # writer.writerows([
    #     {'no' : 66, 'nama' : 'Edi'},
    #     {'no' : 67, 'nama' : 'Fendi'},
    #     {'no' : 68, 'nama' : 'Hadi'}
    # ])

# import json

# with open('112.json', 'r') as myjson:
#     data = json.load(myjson)
# print(data)

# x = [
#     {"nama" : "Ali", "kota" : "BSD"},
#     {"nama" : "Budi", "kota" : "Depok"},
#     {"nama" : "Cici", "kota" : "Jakarta"}
# ]
# with open('112.json', 'w') as myjson:
#     json.dump(x, myjson)

'''
csv
id  nama    kota
1   Andi    Jakarta
2   Budi    Bandung
3   Caca    Jakarta
4   Deni    Semarang
5   Euis    Bandung

json
[
    {"id" : 1 , "nama":"Andi", "kota" : "x"},
    {"id" : 1 , "nama":"Andi", "kota" : "x"},
    {"id" : 1 , "nama":"Andi", "kota" : "x"}
]

csv => json
json => csv
'''

# import csv
# with open('1121.csv','r') as mycsv :
#     reader = csv.DictReader(mycsv, delimiter =';')
#     data=[]
#     for i in reader:
#         data.append(dict(i))
#     print(data)

# import json
# with open ('1121.json','w') as myjson :
#     json.dump(data, myjson)

# import json
# with open ('1122.json','r') as myjson :
#     data = json.load(myjson)
# print(data)

# import csv
# with open('1122.csv','w',) as mycsv :
#     writer = csv.DictWriter(mycsv, delimiter =';', fieldnames = ['id','nama','kota'])
#     writer.writerows([{'id':'id', 'nama':'nama', 'kota':'kota'}])
#     writer.writerows(data)

# import xlrd
# book = xlrd.open_workbook('1121.xlsx')
# sheet = book.sheet_by_index(0)
# sheet = book.sheet_by_name('Sheet1')
# print(sheet.nrows)
# print(sheet.ncols)
# print(sheet.cell_value(0,0))
# print(sheet.cell_value(2,1)) # baris dulu baru kolom

# no = []
# nama=[]
# usia=[]
# kota=[]
# for i in range(1,sheet.nrows) :
#     no.append(sheet.cell_value(i,0))
#     nama.append(sheet.cell_value(i,1))
#     usia.append(sheet.cell_value(i,2))
#     kota.append(sheet.cell_value(i,3))

# print(no, nama, usia, kota)
# data = list(zip(no,nama,usia,kota))

# print(data)
# data = []
# for i in range(1,sheet.nrows) :
#     new = []
#     for j in range(sheet.ncols) :
#         new.append(sheet.cell_value(i,j))
#     data.append(tuple(new))

# print(data)

# for i in range(sheet.nrows) :
#     print(sheet.row_values(i))

# import xlsxwriter

# book = xlsxwriter.Workbook("1121.xlsx")
# sheet = book.add_worksheet("Database")

# sheet.write(row, col, value)
# sheet.write(0,0, 'Budi')
# data = [
#     [1, 'Andi', 'Jakarta'],
#     [2, 'Budi', 'Jakarta']
# ]
# row = 0
# for no, nama, kota in data:
#     sheet.write(row, 0, no)
#     sheet.write(row, 1, nama)
#     sheet.write(row, 2, kota)
#     row += 1

# book.close()

# baca xlxswriter buat nambah sheet tanpa menghapus sheet lainnya

# csv => excel
# import csv
# with open('1121.csv','r') as mycsv :
#     reader = csv.reader(mycsv, delimiter =';')
#     data=[]
#     for i in reader:
#         data.append(i)
#     print(data)

# import xlsxwriter
# book = xlsxwriter.Workbook("1122.xlsx")
# sheet = book.add_worksheet("Database")
# row = 0
# for id, nama, kota in data :
#     sheet.write(row, 0, id)
#     sheet.write(row, 1, nama)
#     sheet.write(row, 2, kota)
#     row += 1
# book.close()
    
# json => excel
# import json
# with open ('1122.json','r') as myjson :
#     data = json.load(myjson)
# print(data)

# import xlsxwriter
# book = xlsxwriter.Workbook("1123.xlsx")
# sheet = book.add_worksheet("Database")
# row = 1
# sheet.write(0,0,'id')
# sheet.write(0,1,'nama')
# sheet.write(0,2,'kota')
# for i in range(0,len(data)) :
#     sheet.write(row, 0, data[i]['id'])
#     sheet.write(row, 1, data[i]['nama'])
#     sheet.write(row, 2, data[i]['kota'])
#     row += 1
# book.close()

# excel => csv
# import xlrd
# book = xlrd.open_workbook('1121.xlsx')
# sheet = book.sheet_by_index(0)
# data = []
# for i in range(0,sheet.nrows) :
#     new = []
#     for j in range(sheet.ncols) :
#         new.append(sheet.cell_value(i,j))
#     data.append(new)
# print(data)
# import csv
# with open('1123.csv', 'w', newline='') as mycsv :
#     writer = csv.writer(mycsv, delimiter = ';')
#     writer.writerows(data)

# excel => json

# import xlrd
# book = xlrd.open_workbook('1121.xlsx')
# sheet = book.sheet_by_index(0)
# data = []
# for i in range(0,sheet.nrows) :
#     new = []
#     for j in range(sheet.ncols) :
#         new.append(sheet.cell_value(i,j))
#     data.append(new)
# print(data)
# import json
# with open ('1121.json','w') as myjson :
#     json.dump(data, myjson)
