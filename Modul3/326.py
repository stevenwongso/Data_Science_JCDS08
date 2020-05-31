from flask import Flask, render_template, redirect, request
import joblib
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('irishome.html')

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == "GET" :
        return redirect('/')
    else :
        dataform = request.form
        SL = float(dataform['SL'])
        SW = float(dataform['SW'])
        PL = float(dataform['PL'])
        PW = float(dataform['PW'])
        hasil = str(model.predict([[SL,SW,PL,PW]])[0])
        return render_template('irisresult.html', SL = SL, SW = SW, PL = PL, PW = PW, hasil=hasil)

if __name__ == '__main__':
    model = joblib.load('modelJoblib')
    app.run(
        debug = True
    )