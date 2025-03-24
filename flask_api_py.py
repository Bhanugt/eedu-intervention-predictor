# -*- coding: utf-8 -*-
"""flask_api.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kOwFpBRBZBlKpE7CYP2YxVFW_zOQ4JoE
"""

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('edu_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)