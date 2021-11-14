from flask import Flask, request, jsonify, Response
from flask import render_template, url_for, redirect, flash
import pandas as pd
import numpy as np
#from spacy import displacy
from app.model import predict_d
from flask_cors import CORS, cross_origin
import json



app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def home():
    return("welcome to huggle care api")

@app.route("/d_predict", methods=['POST'])
def pred():
    data = request.get_json()
    dataframe = pd.DataFrame.from_dict(data, orient="index")
    df = dataframe.transpose()
    result = predict_d(df)
    return jsonify(result)
    