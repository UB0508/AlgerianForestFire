from flask import Flask, render_template, request,jsonify
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

app = application

ridge_model = pickle.load(open('models/ridge_cv_model.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler_algerian_forest.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST',"GET"])
def predict():
    if request.method == "POST":
        Temperature = float(request.form['Temperature'])
        RH = float(request.form['RH'])
        Ws = float(request.form['Ws'])
        Rain = float(request.form['Rain'])
        FFMC = float(request.form['FFMC'])
        DMC = float(request.form['DMC'])
        ISI = float(request.form['ISI'])
        Classes = float(request.form['Classes'])
        Region = float(request.form['Region'])

        input_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
        input_data_scaled = standard_scaler.transform(input_data)
        prediction = ridge_model.predict(input_data_scaled)
        return render_template('home.html', result=round(prediction[0], 2))
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5050)
