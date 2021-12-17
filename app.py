from flask import Flask, request, render_template, jsonify,url_for,redirect, session, Markup
import json
import os
from numpy import product
import pandas as pd
import urllib.request
# url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
# response = urllib.request.urlopen(url)
# data_json = json.loads(response.read())
# df = pd.DataFrame.from_dict(data_json['products'],orient ='index')
# df["popularity"] = pd.to_numeric(df["popularity"])
# df = df.sort_values('popularity', ascending=[False])
# result = Markup(df.to_html(classes="table table-striped table-class",table_id='table-id'))
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/",methods=["POST","GET"])
def login():
        columns=""
        if request.method == 'POST':
        
                uploaded_file = request.files['file']
                if uploaded_file.filename != '':
                        data = json.load(uploaded_file)
                        df = pd.DataFrame.from_dict(data['products'],orient ='index')
                        
                        for col in df.columns:
                                col = "<option>"+col
                                columns = columns+col
                        return redirect(url_for("column",columns = columns))                
        return render_template('insert.html')        

@app.route("/col",methods=["POST","GET"])
def column():
        columns=""
        columns = str(request.args.get('columns', None))
        columns = Markup(columns)
        if request.method == 'POST':
                multiselect= request.form.getlist("lstBox2")
                print(multiselect)
                return redirect(url_for("display",multiselect = multiselect))  
        return render_template('insert.html',columns=columns)

@app.route("/disp",methods=["POST","GET"])
def display():
        multiselect=""
        multiselect = str(request.args.get('multiselect', None))
        print(multiselect)
        return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)