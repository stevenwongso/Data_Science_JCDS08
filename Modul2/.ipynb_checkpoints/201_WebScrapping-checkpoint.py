'''
Web Scrapping

Selama data yang ada terdapat dalam page source maka dapat dilakukan web scrapping

install beautifulsoup4 : pip install beautifulsoup4

'''

# from bs4 import BeautifulSoup

# html = open('202.html','r')
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# print(soup.p)
# print(soup.h1)
# print(soup.h1.text)
# print(soup.h1.string)
# print(soup.get_text())

# print(soup.ul.text)
# print(soup.ul.li.text)
# print(soup.find("ul"))
# print(soup.find("li"))
# print(soup.find("ul").text)

# print(soup.find_all("li")) #langsung dapet list
# nama =[]
# for i in soup.find_all('li'):
#     nama.append(i.text)
# print(nama)

# print(soup.find(class_='students'))
# print(soup.find(id='1'))

# HTML dari link
# import requests

# url = 'https://www.bi.go.id/id/moneter/informasi-kurs/transaksi-bi/Default.aspx'
# html = requests.get(url)
# soup = BeautifulSoup(html.content, 'html.parser')

# print(soup.find(class_='table1'))
# kolomnilai=[]
# for i in soup.find_all('td', class_='alignRight'):
#     kolomnilai.append(i.text)
# print(kolomnilai)

# scrapping trus save jadi file excel

# import requests

# url = 'https://www.bi.go.id/id/moneter/informasi-kurs/transaksi-bi/Default.aspx'
# html = requests.get(url)
# soup = BeautifulSoup(html.content, 'html.parser')

# kolomnilai=[]
# for i in soup.find_all('td', class_='alignRight'):
#     kolomnilai.append(i.text)
# print(kolomnilai)

# kursjual = []
# kursbeli = []
# index = 0
# for i in soup.find_all('td', style="text-align:right;") :
#     if (index + 1) % 2 == 0 :
#         kursbeli.append(i.text)
#     else :
#         kursjual.append(i.text)
#     index += 1
# print (kursjual)
# print (kursbeli)

# matauang= []
# index = 0
# x =str(soup.find("table", id="ctl00_PlaceHolderMain_biWebKursTransaksiBI_GridView1"))
# soup2 = BeautifulSoup(x, 'html.parser')
# for i in soup2.find_all('td'):
#     if index % 5 == 0 :
#         matauang.append(i.text)
#     index += 1
# # print(matauang)

# import xlsxwriter
# book = xlsxwriter.Workbook("202.xlsx")
# sheet = book.add_worksheet("Table_Kurs_Uang")
# row = 1
# sheet.write(0,0,'Matauang')
# sheet.write(0,1,'Nilai')
# sheet.write(0,2,'Kurs Jual')
# sheet.write(0,3,'Kurs beli')
# for i in range(0,len(matauang)) :
#     sheet.write(row, 0, matauang[i])
#     sheet.write(row, 1, kolomnilai[i])
#     sheet.write(row, 2, kursjual[i])
#     sheet.write(row, 3, kursbeli[i])
#     row += 1
# book.close()

from bs4 import BeautifulSoup
import requests

url = 'http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

x = soup.find_all("strong")
# print(x)

namaultra =[]
for i in range(2,36) :
    namaultra.append(x[i].text)

namamonster = []
for i in x[37:110] :
    namamonster.append(i.text)

print(namaultra)
print(namamonster)