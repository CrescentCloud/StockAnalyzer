from flask import Flask, render_template,request
import pandas as pd
import random

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get_price",methods = ['POST', 'GET'])
def get_price():
	dt1 = request.form['dt1']
	dt2 = request.form['dt2']

	df = pd.read_csv("database/AABA_2006-01-01_to_2018-01-01.csv")

	mask = (df['Date'] >= dt1) & (df['Date'] <= dt2)
	df1=df.loc[mask];
	
	df1=df1[df1['Close']==df1['Close'].max()];
	
	return df1.to_json();

	
if __name__=="__main__":
    app.run(debug=True)
