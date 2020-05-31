
# Pip install flask

# Pertemuan 310320

# from flask import Flask, render_template, jsonify, redirect
# app = Flask(__name__)

# x= [
#     {
#         'nama':'Andi', 'usia':21
#     },
#     {
#         'nama':'Budi', 'usia':21
#     },
#     {
#         'nama':'Caca', 'usia':22
#     }
# ]

# @app.route('/') #domain kita slash
# def home():
#     return '<h1>Hello Everyone!</h1>' #bisa pake html

# @app.route('/html')
# def html():
#     return render_template('300.html')
#     #render template dia akan merender file-file difolder templates sehingga 300.html harus ada difolder templates

# @app.route('/data')
# def data():
#     return jsonify(x)

# # Dynamic route

# # @app.route('/data/<string:nama>')
# # # Pastikan berbentuk string
# # def nama(nama):
# #     return f'Halo {nama}!'

# @app.route('/data/<int:id>')
# def nama(id):
#     return jsonify(x[id-1])

# @app.errorhandler(404)
# def notfound(error):
#     # return '<h1>Mohon maaf, File not found!</h1>'
#     return jsonify([{'status':'404', 'Message':'Error Not Found'}])

# # Redirect
# @app.route('/students')
# def student():
#     return redirect('/data')

# if __name__ == "__main__":
#     app.run(debug=True, host='127.1.2.3', port=1234) #default localhost

# ''' 
# dengan flask create => Web Profil Biodata
# /   => halaman depan
# /gallery => halaman berisi galeri foto
# /contact => form , pasif 
# '''

# Pertemuan 010420

# # Backend : flask(python based)(ringan,efisien) alternative : Django(ada beberapa template)
# # Apabila lebih dari satu flask ingin dijalankan pastikan port berbeda

# from flask import Flask, render_template, url_for,jsonify,request
# app = Flask(__name__)


# @app.route('/')
# def home():
#     # return "tes 1 2 3"
#     return render_template('300.html')

# @app.route('/vars')
# def variabel():
#     x ={'nama':'andi','usia':22}
#     return render_template('3001.html', y = x)

# @app.route('/json')
# def json():
#     x ={'nama':'Andi','usia':29, 'kota':'jakarta'}
#     return jsonify(x)

# # HTTP METHOD : CRUD (create,read,update,delete)
# # C => Method POST (send data)
# # R => Method GET
# # U => Method PUT/PATCH (send data)
# # D => method DELETE
# # route GET & POST, import request!

# @app.route('/method', methods=['GET','POST','PUT','DELETE'])
# def method():
#     if request.method == 'GET' :
#         return 'Anda nge-GET ke /method'
#     elif request.method == 'POST':
#         body = request.json
#         print(body)
#         # return 'Anda nge-POST ke /method'
#         return jsonify({
#             'status':'sukses',
#             'name':body['nama'],
#             'city':body['kota'],
#             'usia':body['usia'],
#             'pensiun' : 60 - body['usia']
#             })
#     else :
#         return 'Maaf hanya melayani GET & POST'

# if __name__ == "__main__":
#     app.run(debug=True, port=1234) 

# Pertemuan 02420

# # from flask import Flask, render_template, url_for,jsonify,request
# # app = Flask(__name__)

# # @app.route('/')
# # def home():
# #     return render_template('home.html')

# # @app.route('/tes', methods=['GET','POST'])
# # def tes():
# #     if request.method == 'GET' :
# #         return jsonify({'status': 'Anda nge-GET'})
# #     else:
# #         data = request.form
# #         # print(data)
# #         # name = data['nama']
# #         # age = data['usia']
# #         # return jsonify({'status': 'OK', 'name':name, 'age':age})
# #         return render_template('hasil.html', data=data)
# # if __name__ == "__main__":
# #     app.run(debug=True, port=1234) 

# '''
# Latihan JCDS05 Flask
# '''

# from flask import Flask, render_template, url_for,jsonify,request
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('pokehome.html')

# @app.route('/hasil', methods=['GET','POST'])
# def hasil():
#     if request.method == 'GET' :
#         return jsonify({'status': 'ok'})
#     else:
#         import requests
#         data = request.form
#         url = 'https://pokeapi.co/api/v2/pokemon/' + str(data['nama'].lower())
#         datapoke = requests.get(url)
#         if datapoke.status_code == 200 : #ketika response 200 ok artinya valid baru tanya datanya
#             hasilpoke = datapoke.json()
#             return render_template('pokehasil.html', hasilpoke=hasilpoke )
#         else :
#             return render_template('pokegagal.html')
# if __name__ == "__main__":
#     app.run(debug=True, port=1234)

# Pertemuan 03420

# from flask import Flask,render_template, redirect, jsonify, request, send_from_directory
# from werkzeug.utils import secure_filename
# import os

# app = Flask(__name__, static_url_path='')
# app.config['UPLOAD_FOLDER'] = './storage'

# @app.route('/')
# def home():
#     return render_template('uploadhome.html')

# # cara membuat storage as static directory
# @app.route('/storage/<path:x>')
# def storage(x):
#     return send_from_directory('storage', x)

# #upload
# @app.route('/upload', methods=['GET','POST'])
# def upload():
#     if request.method == 'POST':
#         f = request.files["fileku"]
#         # print(f)
#         # print(f.filename)
#         fname=secure_filename(f.filename) #dapat digunakan untuk merubah nama
#         f.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
#         return redirect(f'/storage/{fname}')

# #apabila storage error basedir = os.path.abspath(os.path.dirname(__file__))


# if __name__ == "__main__":
#     app.run(debug=True, port=1234)

''' 
Silahkan dicoba dirumah

FLASK:
route /  :  Berisi Formulir 
            input untuk ketik Nama, Usia, dan Submit

ketika submit diklik, data nama dan usia masuk ke database:
MYSQL, Mongo DB

nanti dialihkan

route /result : notifikasi bahwa data sukses terkirim ke database

kalau user ke 

route / data : tabel berisi data yang ada di database(DB)

konek flask <=> MySQL
konek flask <=> Mongo DB

flask-mysqldb => berbasis mysqlclient

'''
# Flask <=> mysql

from flask import Flask, render_template, redirect, request
import mysql.connector
import pandas as pd

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '0101steven',
    database = 'flaskmysql')

db = dbku.cursor()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('mysqlhome.html')

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == "GET" :
        return redirect('/')
    else :
        dataform = request.form
        nama = dataform['nama']
        usia = dataform['usia']
        query = 'insert into userflask values (%s,%d)'
        insertdata = (nama,usia)
        db.execute(query,insertdata)
        dbku.commit()
        return render_template('mysqlhasil.html', nama = nama, usia = usia)

@app.route('/data')
def data():
    query = 'select * from userflask'
    df = pd.read_sql(query,dbku)
    return render_template('mysqldata.html',df = df)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
