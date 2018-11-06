#%%
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    basket = request.json['basket']
    zipCode = request.json['zipCode']
    totalAmount = request.json['totalAmount']
    p = probability(basket, zipCode, totalAmount)
    return jsonify({'probability': p}), 201


def probability(basket, zipCode, totalAmount):
    
    import pandas as pd
    import pickle
    
    print("Processing request: {},{},{}".format(basket, zipCode, totalAmount))
    
    datalist = pd.DataFrame({'basket':[basket]})
    dataint = pd.DataFrame({'zipCode':zipCode,'totalAmount':totalAmount},index=[0],dtype=int)
    data = pd.concat([datalist,dataint],axis=1)
    
    data['c_0'] = data.basket.map(lambda x: x.count(0))
    data['c_1'] = data.basket.map(lambda x: x.count(1))
    data['c_2'] = data.basket.map(lambda x: x.count(2))
    data['c_3'] = data.basket.map(lambda x: x.count(3))
    data['c_4'] = data.basket.map(lambda x: x.count(4))
    data['c_5'] = data.basket.map(lambda x: x.count(5))
    
    data["zipCode"] = data["zipCode"].astype('category',categories=list(range(1000,10000)))
    dummies = pd.get_dummies(data.zipCode)
    
    data2 = pd.concat([data, dummies], axis=1)
    data3 = data2.drop(["basket", "zipCode"], axis=1)   
    
    filepath = '/Users/garethjones/Documents/Data Science/Data Science Retreat/15. Practical Data Science - Patrick/models/'
    gbt = pickle.load(open(filepath+'gbt_model.pickle','rb'))
    prediction = gbt.predict_proba(data3)
    prediction_fraud = round(prediction[0][1],3)
    
    return prediction_fraud
