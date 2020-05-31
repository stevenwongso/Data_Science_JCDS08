'''
install package -> pymongo
py -m pip install pymongo
conda install pymongo

untuk akses database mongoDB, pastikan terminal/compass sudah aktif terlebih dahulu
'''
# cara connect database MongoDB ke python
# import pymongo
# urldb = "mongodb://127.0.0.1:27017"
# mongoku = pymongo.MongoClient(urldb)
# dbku = mongoku['ptxyz']    # use ptxyz
# colku = dbku['karyawan']

# show dbs
# print(mongoku.list_database_names())

# show collections
# print(dbku.list_collection_names())

# db.karyawan.find()
# print(list(colku.find()))

# db.karyawan.find({kota:'Jakarta'})
# print(list(colku.find({'kota': 'Jakarta'})))

# Bikin database MongoDB dari python
# import pymongo
# urldb = "mongodb://127.0.0.1:27017"
# mongoku = pymongo.MongoClient(urldb)
# dbku = mongoku['ptabc']    # use ptabc
# colku = dbku['pegawai']    # db.createCollection('pegawai')

# db.karyawan.insertOne({nama:"Hadi"})
# data = {'nama':'Hadi','kota':'Bandung'}
# send = colku.insert_one(data)
# print(send.inserted_id) # untuk tau id data baru yang di insert

# mencari data dengan id tertentu
# newData = list(colku.find({'_id':send.inserted_id}))
# print(newData)

# Agar tampilan dalam bentuk dictionary
# newData = list(c

# Insert multiple data
# db.pegawai.insertMany([{},{},{}])
# data = [
#     {'nama': 'Zizi', 'kota': 'Kediri'},
#     {'nama': 'Zizi', 'kota': 'Surabaya'},
#     {'nama': 'Zizi', 'kota': 'Sleman'}
# ]
# insert data
# kirim = colku.insert_many(data)

# untuk dapat notif nomor id data yang di insert
# print(kirim.inserted_ids)

# Menghapus data
# colku.delete_one({'nama':'Hadi'})

# untuk menghitung berapa data yang terhapus
# hapus = colku.delete_one({'nama':'Zizi'})
# print(hapus.deleted_count)

# untuk menghapus semua yang namanya zizi + dihitung ada berapa data yang terhapus
# hapus = colku.delete_many({'nama':'Zizi'})
# print(hapus.deleted_count)

# menghapus semua data yang ada di database
# hapus = colku.delete_many({})
# print(hapus.deleted_count)

# data = [
#     {'nama': 'Andi', 'kota': 'Kediri'},
#     {'nama': 'Budi', 'kota': 'Surabaya'},
#     {'nama': 'Caca', 'kota': 'Sleman'}
# ]
# kirim = colku.insert_many(data)
# print(kirim.inserted_ids)

# UPDATE DATA
# Update data tertentu
# db.pegawai.updateOne({nama: 'Budi'},{$set: {nama: 'Hudi'}})
# colku.update_one(
#     {'nama':'Caca'},
#     {'$set': {'kota': 'Yogyakarta'}}
# )

# Update all data
# db.pegawai.updateMany({},{$set: {'usia':25}})
# colku.update_many(
#     {},
#     {'$set': {'usia': 25}}
# )

# menampilkan semua data, tanpa dijadikan list
# pegawai = colku.find()  # output berupa object
# for i in pegawai:       # looping jika tidak mau dijadikan list   
#     print(i)

# menampilkan data dengan kriteria tertentu
# db.pegawai.find({},{nama:1}).pretty()            # menampilkan hanya nama saja
# db.pegawai.find({},{nama:1, kota:1}).pretty()    # menampilkan hanya nama dan kota
# pegawai = colku.find({}, {'nama':1, 'usia':1})
# for i in pegawai:                                # alternatif: print(list(pegawai))
#     print (i)

# menampilkan data dengan operator >, <, >=, <=
# db.pegawai.find({usia: {$gt:26}})
# pegawai = colku.find({'usia':{'$gt': 26}})
# for i in pegawai:                           
#     print (i)

# Important queries to master:
# CRUD : Create, Read, Update, Delete

'''CONVERT FILE'''
'''mongodb => json'''
# import json

# data = list(colku.find())
# for i in range(len(data)):
#     data[i]['_id'] = str(data[i]['_id'])

# with open ('mongodbku.json','w') as myjson :
#     json.dump(data, myjson)

'''mongodb => csv'''
# import csv 

# data = list(colku.find())
# for i in range(len(data)):
#     data[i]['_id'] = str(data[i]['_id'])

# with open('mongodbku.csv','w',) as mycsv :
#     writer = csv.DictWriter(mycsv, delimiter =';', fieldnames = ['_id','nama','kota','usia'])
#     writer.writerows([{'_id':'_id', 'nama':'nama', 'kota':'kota','usia':'usia'}])
#     writer.writerows(data)

'''mongodb => excel'''
# import xlsxwriter

# book = xlsxwriter.Workbook("mongodbku.xlsx")
# sheet = book.add_worksheet("Database")

# data = list(colku.find())
# for i in range(len(data)):
#     data[i]['_id'] = str(data[i]['_id'])

# row = 1
# for i in range(len(data)):
#     sheet.write(row, 0, data[i]['_id'])
#     sheet.write(row, 1, data[i]['nama'])
#     sheet.write(row, 2, data[i]['kota'])
#     sheet.write(row, 3, data[i]['usia'])
#     row += 1

# book.close()

'''
Convert File dengan MongoExport dan MongoImport

1. Melalui command prompt, run as administrator
2. Masuk ke direktori mongodb
3. Mongodb => json
   mongoexport --db=ptabc --collection=pegawai --out=buruh.json
   Mongodb => csv
   mongoexport --db=ptabc --collection=pegawai --type=csv --fields=nama,kota,usia --out=buruh.csv
   json => Mongodb
   mongoimport --db=ptabc --collection=buruhjson --file=buruh.json
   csv => Mongodb
   mongoimport --db=ptabc --collection=buruhcsv --type=csv --headerline --file=buruh.csv
4. Hasil export ada di folder bin
5. Pastikan file yang mau di import sudah ada di folder bin
'''
'''
---TASK---
scrap data di: digidb.io/digimon-list/
ada 14 feature yang akan di scrapping (13 kolom + 1 link picture)
convert hasil scrapping ke dalam bentuk: json, csv, excel, mongodb db=digimon col=digimon 
'''