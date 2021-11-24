#@app.route('/predict', methods=['GET'])
#def predict():
#    print('letal')
    #return jsonify(predict_single(request.files['image']))

#import sys
#from flask import render_template, redirect, url_for, request, abort

from model.RoadSign import RoadSign
from model.PredictionModelObject import PredictionModelObject

def test():
    return "MVC en Flask exitoso"