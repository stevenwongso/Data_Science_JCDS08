# Connect python ke mySQL   

import mysql.connector

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '0101steven',
    # database = 'world'
    database = 'ptdef'
)

x = dbku.cursor()

# # x.execute({query SQL})
# x.execute('show databases')
# # print(x.fetchall())
# print(list(x))

# x.execute('show tables')
# print(x.fetchall())
# print(x.fetchone())
# print(list(map(lambda z:z[0],list(x))))

# x.execute('use ptdef')
# x.execute('create table karyawan (no int, nama varchar(100))')

# x.execute('create table')
# x.execute('insert into karyawan values (1, "Andi")')
# x.execute('insert into karyawan values(%s, %s)',(2,"Budi"))
# queryinsert = 'insert into karyawan values (%s,%s)'
# datainsert = (input("ketik no : "),input("Ketik nama : "))
# x.execute(queryinsert,datainsert)
# datanew =[(123,'Agus'),(456, 'Bambang'),(789,'Cici')]
# x.executemany(queryinsert,datainsert)

# x = dbku.cursor(dictionary= True)
# x.execute('select * from karyawan')
# x.execute('select * from karyawan where no > 10')
# x.execute('delete from karyawan where no < 5')
# querydelete= 'delete from karyawan where nama =%s'
# deletenama = ('Bambang',)
# x.execute(querydelete, deletenama)
# print(list(x))
# queryupdate = ('update karyawan set nama = %s where nama = "Adi"')
# updatenama = 'Bambang', # Pastikan tupple
# x.execute(queryupdate,updatenama)
# dbku.commit() # untuk melakukan perubahan/penambahan data perlu dilakukan method commit
# print(x.rowcount, "data suskes tersimpan!") # Penambahan buat disend notif berapa data yang masuk

'''
Beberapa extension lainnya
squelize
pymysql
flaskmyql
'''

'''
coba 
db world
3 tables city, country, country language
mysql => 3 buah json
mysql => 3 buah csv
mysql => 3 buah excel
mysql => mongodb

mongodb => json     pymongo json
mongodb => csv      pymongo csv
mongodb => excel    pymongo xlsxwriter   


14 col = 13 col + 1 picture
http://digidb.io/digimon-list/ =>   json
                                    csv
                                    excel
                                    mongodb db = digimon col = digimon
                                    mysql db = digimon table = digimon

11 file python => buat repo => push github #sebelum ujian disetor!!!
'''