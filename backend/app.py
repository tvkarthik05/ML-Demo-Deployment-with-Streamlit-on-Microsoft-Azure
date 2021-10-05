import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

from PIL import Image
from fastai.vision.all import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from pathlib import Path

# nltk.download('vader_lexicon')

# os.environ['CONDA_DLL_SEARCH_MODIFICATION_ENABLE'] = 1
app = Flask(__name__)

# Define the function to return the label
def is_cat(x):
    if x.name[0].isupper():
        return 'Cat'
    else:
        return 'Dog'

# Load models
tabular_model = pickle.load(open('./models/tabular_rf_model.pkl', 'rb'))

cv_path = Path('/models')
cv_model = load_learner(cv_path/'pets_classifier.pkl')


@app.route('/streamtabular',methods=['POST'])
def streamtabular():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = tabular_model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(str(output))

@app.route('/batchtabular',methods=['POST'])
def batchtabular():
    '''
    For direct API calls trought request
    '''
    data = pd.read_csv(request.files['upload_file'])
    prediction = tabular_model.predict(data)
    
    return jsonify(str(prediction))

@app.route('/cv',methods=['POST'])
def cv():
    '''
    For direct API calls trought request
    '''
    data = request.files['upload_file']
    file_bytes = Image.open(data)
    im_cv = np.array(file_bytes)

    prediction = cv_model.predict(im_cv)

    output = prediction[0]
    return jsonify(output)

@app.route('/nlp',methods=['POST'])
def nlp():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)

    analyzer=SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(data)
    vs.popitem()
    prediction = max(vs, key=vs.get)

    output = prediction
    return str(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)