import pickle
from joblib import dump, load 
import pandas as pd
import numpy as np


loaded_model = load("app/model/gbmodel.joblib.dat")


def predict_d(data):
    prob = list(loaded_model.predict_proba(data[0:1]))
    columns = ['label', 'proba']
    label = list(loaded_model.classes_)
    res = pd.DataFrame(list(zip(label, prob[0])), columns =columns)
    res['proba'] = round(res['proba'], 4)
    res_s= res.sort_values(by='proba', ascending=False)
    res_d = res_s[0:5]
    result = res_d.to_dict('records')
    return result
