from flask import Flask, render_template, redirect, request
import joblib
import json 

# plotly
import plotly
import chart_studio.plotly as py 
import plotly.graph_objects as go

app = Flask(__name__)

# route untuk visualisasi plotly
@app.route('/dataviz')
def dataviz():
    x =list(range(1,11))
    y = [3,4,3,5,6,6,8,7,9,8]
    plot = go.Scatter(
        x = x,y = y
    )
    plotJSON = json.dumps([plot], cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dataviz.html',plotJSON=plotJSON)

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