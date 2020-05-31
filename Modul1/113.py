'''
- request API => server backend => database
- web scraping ( data di website tidak bisa download, tidak ada api. ada syarat dan ketentuan untuk dapat dilakukan) => HTML
tutorial HTML : w3schools.com, youtube : lintang wisesa, developer.mozilla.org
- database rdbms (tabel) dan non rdbms (non tabel)
beberapa program yang digunakan untuk membuat tampilan website (untuk proyek akhir)
- <HTML> (fondasi)
- <CSS> (Mempercantik)
- <javascript> (fasilitas)

protocol : http
method : get

try : https://jsonplaceholder.typicode.com/
untuk nge get API bisa langsung dibrowser asalkan tau routenya
software untuk ngetest API : postman (download appnya, install)
API :https://jsonplaceholder.typicode.com/users
https://jsonplaceholder.typicode.com/users/1 , keluar 1 user aja disebut dynamic roots
untuk kode : bisa cek di http status code

kalau main twitter cari happycoding => vscode

package
pip install / py -m pip install
pip uninstall/ py -m pip uninstall
pip list/ py -m pip list
pip install -- upgrade / py -m pip install --upgrade
pip install pacakge==versi 
'''

# GET request REST API

# import requests # install dulu
# url = 'https://jsonplaceholder.typicode.com/users'
# data = requests.get(url)
# print(data) #ketika response 200 ok artinya valid baru tanya datanya
# if data.status_code == 200 : #ketika response 200 ok artinya valid baru tanya datanya
#     hasil = data.json()
#     print(hasil)
    # print(hasil[0]) #atau bisa juga getnya ke users/1
    # print(hasil[0]['name']) #ketika ingin diambil datanya saja
    # for i in hasil :
    #     print(i['name'])

    # dari data yang ada ingin dibuat dalam bentuk json
    # import json
    # with open ('1131.json','w') as myjson :
    #     json.dump(hasil, myjson)

    # dari data yang ada ingin dibuat dalam bentuk CSV dan excel
    # id name username email adress (street,suite,city,zip), geo(lat,long), phone, web, company(name)
    # dalam bentuk csv
    # import csv
    # with open('1131.csv','w',) as mycsv :
        # writer = csv.DictWriter(mycsv, delimiter =';', fieldnames = ['id','name','username','email','address','geo','website','phone','company'])
    #     writer.writerows([{'id':'id','name':'name','username':'username','email':'email','address':'address','geo' : 'geo','website':'website','phone':'phone','company':'company'}])
    #     writer.writerows(hasil)
    # dalam bentuk excel
    # import xlsxwriter
    # book = xlsxwriter.Workbook("1131.xlsx")
    # sheet = book.add_worksheet("Database")
    # row = 1
    # sheet.write(0,0, "id")
    # sheet.write(0,1, "name")
    # sheet.write(0,2, "username")
    # sheet.write(0,3, "email")
    # sheet.write(0,4, "address")
    # sheet.write(0,5, "geo")
    # sheet.write(0,6, "phone")
    # sheet.write(0,7, "web")
    # sheet.write(0,8, "company")
    # for i in range(0, len(hasil)) :
    #     sheet.write(row,0, hasil[i]['id'])
    #     sheet.write(row,1, hasil[i]["name"])
    #     sheet.write(row,2, hasil[i]["username"])
    #     sheet.write(row,3, hasil[i]["email"])
    #     sheet.write(row,4, (hasil[i]["address"]['street'] + "," + hasil[i]["address"]['suite'] + "," + hasil[i]["address"]['city'] + "," + hasil[i]["address"]['zipcode']))
    #     sheet.write(row,5, (hasil[i]["address"]["geo"]['lat'] + ","+ hasil[i]["address"]["geo"]['lng']))
    #     sheet.write(row,6, hasil[i]["phone"])
    #     sheet.write(row,7, hasil[i]["website"])
    #     sheet.write(row,8, hasil[i]["company"]['name'])
    #     row += 1
    # book.close()
# else :
#     print("Request tidak sukses")
'''
TheSportsDB : untuk data pemain dkk free
kurs.web.id
# '''
# import requests
# url = "https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p="
# nama = input ("Ketik nama Atlet : ")
# data = requests.get(url+nama)

# if data.status_code == 200 :
#     hasil = data.json ()
#     print(hasil)
# else :
#     print ("Request tidak sukses")

# x = 1
# while x != 0 : 
#     print(
#     '''
#     Pilihan menu :
#     1. USD to IDR
#     2. IDR to USD
#     ''' 
#     )
#     pilihan = input("Silahkan pilih menu yang diinginkan (1/2) : ")
#     if pilihan == '1' or pilihan == '2' :
#         url = "https://kurs.web.id/api/v1/"
#         nama = input("Ketik nama bank : ")
#         data = requests.get(url+nama)
#         if data.status_code == 200 and pilihan == "1" :
#             hasil = data.json ()
#             jual = int(hasil['jual'])
#             print(f'1 USD = Rp.{jual}')
#             jumlah = int(input("ingin menukarkan berapa USD? \n"))
#             print(f'{jumlah} USD =Rp.{jumlah*jual}')
#             print('Terima kasih telah menggunakan jasa kami')
#             break
#         elif  data.status_code == 200 and pilihan == "2" :
#             hasil = data.json ()
#             beli = int(hasil['beli'])
#             print(f'Rp.1 = {1 /beli} US$')
#             jumlah = int(input("ingin menukarkan berapa rupiah ? \n"))
#             print(f'Rp.{jumlah} ={jumlah/beli} US$')
#             print('Terima kasih telah menggunakan jasa kami')
#             break
#         else :
#             print ("Request tidak sukses")
#             break
#     else :
#         print("Mohon maaf pilihan tidak terdapat pada menu! Silahkan coba lagi")

'''
untuk akses data weather
openweathermap.org
user key dicantumkan pada URL
'''

# import requests

# myid = '093ccb9ee0087a1f90324d0ea9b2f966'
# kota = input('Ketik nama kota : ')
# url = f'http://api.openweathermap.org/data/2.5/weather?q={kota}&appid={myid}'
# data = requests.get(url)
# print(data.json())

'''
untuk akses data restaurant
zomato bagian developer API
user key dicantumkan pada header

city id
jakarta 74
Bandung 11052
bali 170
'''

# import requests

# cari = input('Ketik apa yang ingin dicari : ')
# apikey = "b67f11b0082251049d6fd20a4d57ab85"
# url = f'https://developers.zomato.com/api/v2.1/search?entity_id=74&entity_type=city&q={cari}'
# header = {
#     'user-key' : apikey
# }
# data = requests.get(url, headers = header)
# # print(data.json())
# resto = data.json()["restaurants"]
# for i in resto :
#     print(i['restaurant']['id'], ':', i['restaurant']['name'], ':', i['restaurant']['location']['address'])

# import requests

# apikey = "b67f11b0082251049d6fd20a4d57ab85"
# url = f'https://developers.zomato.com/api/v2.1/restaurant?res_id=18539657'
# header = {
#     'user-key' : apikey
# }
# data = requests.get(url, headers = header)
# print(data.json())
