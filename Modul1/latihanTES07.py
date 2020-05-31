# # Soal nomor 1
#
# '''
# Diketahui:
#
# A = himpunan (set) bilangan genap antara 1 dan 20.
# B = himpunan (set) bilangan ganjil antara 1 dan 20.
# C = himpunan (set) bilangan negatif lebih dari -10.
# D = himpunan (set) bilangan prima antara 1 dan 20.
# E = himpunan (set) bilangan komposit antara 1 dan 20.
# Definisi & kategori bilangan dapat Anda simak di laman Wikipedia. Buatlah sebuah file python (.py) yang dapat menyelesaikan permasalahan himpunan berikut:
#
# a. A ∪ B ∪ C ∪ D ∪ E
#
# b. (A ∩ B) ∪ (D ∩ E)
#
# c. (A ∪ B) ∩ (D ∪ E)
#
# d. (A ∪ B) - (D ∪ E)
#
# e. (A ∪ B ∪ C) - (A ∩ E)
#
# '''
#
# a = set(range(2,20,2))
# b = set(range(3,20,2))
# c = set(range(-10,0))
# d = {2, 3, 5, 7, 11, 13, 17, 19}
# e = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18}
#
# print('1. ', (a|b|c|d|e))
# print('2. ', ((a&b)|(d&e)))
# print('3. ', ((a|b)&(d|e)))
# print('4. ', ((a|b)-(d|e)))
# print('5. ', ((a|b|c)-(a&e)))
#
# # Soal nomor 2
#
# def segitigaKata(kata):
#     syarat = [1]
#     awal = 1
#     hasil = ''
#     penambahan = 0
#     kata = kata.replace(' ','')
#     for i in range(2,len(kata)):
#         awal += i
#         syarat.append(awal)
#     if len(kata) in syarat:
#         for i in range(syarat.index(len(kata))+2):
#             for j in range(i):
#                 hasil += kata[penambahan]
#                 penambahan += 1
#             hasil += '\n'
#         penambahan = 0
#         for i in range(syarat.index(len(kata))+1, 0, -1):
#             for j in range(i):
#                 hasil += kata[penambahan]
#                 penambahan += 1
#             hasil += '\n'
#         print(hasil)
#     else:
#         print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
#
# segitigaKata('Purwadhika')
# segitigaKata('Purwadhika Startup and Coding School @BSD')
# segitigaKata('kode')
# segitigaKata('kode python')
# segitigaKata('lintang')

# # Soal 3
# import re
# import requests
# jsonData = requests.get('https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS07/master/ccNasabah.json')
# data = jsonData.json()
#
# listNama = []
# listCC = []
# for dataPersonal in data:
#     listCC += [dataPersonal['noCreditCard']]
#     listNama += [dataPersonal['nama']]
#
# listCCValid = []
# listNamaValid = []
# listCCInvalid = []
# listNamaInvalid = []
# dictValid = []
# for nomorCC in listCC:
#     valid = re.findall((('^[456][0-9]{3}[-][0-9]{4}[-][0-9]{4}[-][0-9]{4}$|^[456][0-9]{3}[0-9]{4}[0-9]{4}[0-9]{4}$')),nomorCC)
#     print(valid)
#     for cc in valid:
#         index = listCC.index(cc)
#         validName = listNama[index]
#         listNamaValid += [validName]
#         listCCValid += [cc]
#         validCC = {'nama':validName}
#         validCC.update({'noCreditCard': cc})
#         print(validCC)
#         dictValid.append(validCC)
#
# dictInvalid = []
# for nomorCC in listCC:
#     if nomorCC not in listCCValid:
#         listCCInvalid += [nomorCC]
#         listNamaInvalid += [listNama[listCC.index(nomorCC)]]
#         InvalidNama = {'nama':listNama[listCC.index(nomorCC)]}
#         InvalidNama.update({'noCreditCard': nomorCC})
#         dictInvalid.append(InvalidNama)
#
# print(dictValid)
# print(dictInvalid)
#
#
# import json
#
# with open('ccValid.json', 'w') as myjson:
#     json.dump(dictValid, myjson)
# with open('ccInvalid.json', 'w') as myjson:
#     json.dump(dictInvalid, myjson)
#
# # soal 4
#
# import xlrd
# import xlsxwriter
#
# # read dulu dan ubah data
# book = xlrd.open_workbook('tesch.xlsx')
# sheet = book.sheet_by_index(0)
#
# dataSheet1 =[]
# dataSheet2 =[]
# dataSheet3 =[]
# for i in range(sheet.nrows):
#     dataSheet1.append(sheet.row_values(i))
# for i in range(sheet.ncols):
#     dataSheet2.append(sheet.col_values(i))
# for i in range(sheet.nrows):
#     dataSheet3.append(sheet.row_values(i))
# # reverse datasheet3
# for data in dataSheet3:
#     data.sort(reverse=True)
#
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))
#
# # ambil datasheet 4 dari datasheet 2 yang di reverse dan reverse isinya
# dataSheet4 = dataSheet2[::-1]
# for data in dataSheet4:
#     data.sort(reverse=True)
#
# # write ke new sheet
# book = xlsxwriter.Workbook('tesch.xlsx')
# sheet1 = book.add_worksheet('Sheet 1')
# sheet2 = book.add_worksheet('Sheet 2')
# sheet3 = book.add_worksheet('Sheet 3')
# sheet4 = book.add_worksheet('Sheet 4')
#
# # print((data))
#
# row = 0
# for angka1, angka2, angka3 in dataSheet1:
#     sheet1.write(row, 0, angka1)
#     sheet1.write(row, 1, angka2)
#     sheet1.write(row, 2, angka3)
#     row += 1
#
# row = 0
# for angka1, angka2, angka3 in dataSheet2:
#     sheet2.write(row, 0, angka1)
#     sheet2.write(row, 1, angka2)
#     sheet2.write(row, 2, angka3)
#     row += 1
#
# row = 0
# for angka1, angka2, angka3 in dataSheet3:
#     sheet3.write(row, 0, angka1)
#     sheet3.write(row, 1, angka2)
#     sheet3.write(row, 2, angka3)
#     row += 1
#
# row = 0
# for angka1, angka2, angka3 in dataSheet4:
#     sheet4.write(row, 0, angka1)
#     sheet4.write(row, 1, angka2)
#     sheet4.write(row, 2, angka3)
#     row += 1
#
# book.close()
#
# # soal remidial 1
#
# thnKabisat = 2020
# thnInput = int(input('Input tahun : '))
# selisihThn = abs(thnInput - thnKabisat)
#
# if selisihThn % 4 == 0:
#     print('Hasil = TAHUN KABISAT')
# else:
#     print('Hasil = BUKAN TAHUN KABISAT')

# soal remidial 2
# import re
# def validemail(emailInput):
#     listKata = []
#     listKata += emailInput.split(' ')
#     email = re.findall('[\w.-]+[@]+[\w]+[.][\w]{2,5}$', emailInput)
#     if len(email)>0:
#         print(f'Email {emailInput}')
#         print('EMAIL VALID')
#     else:
#         print(f'Email {emailInput}')
#         print('EMAIL TIDAK VALID')

# validemail('lintangwisesa@ymail.com')
# validemail('lintang@purwadhika.com')
# validemail('lintang123@ironman123.space')
# validemail('l/nt*ngw:s=s!@ym~il.com')
# validemail('lintang@purwadhika.community')
# validemail('lintang123@ironman123')
