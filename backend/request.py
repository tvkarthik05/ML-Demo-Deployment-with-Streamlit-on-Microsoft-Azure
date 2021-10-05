import requests

url = 'http://localhost:8000/'
action='NLP'

if action=='Streamtabular':
    # Streamtabular
    route = url+'streamtabular'
    payload = {'Sepal_Length':2, 'Sepal_Width':2, 'Petal_Length':1, 'Petal_Width':1.5}
    r = requests.post(route,json=payload)

    print(r.text)

if action=='Batchtabular':
    # Batchtabular
    route = url+'batchtabular'
    file = '../data/scoring_tabular_data.csv'
    r = requests.post(route,files={'upload_file':open(file, 'r')})

    print(r.text)

if action=='CV':
    # Batchtabular
    route = url+'cv'
    file = '../data/Abyssinian_1.jpg'
    r = requests.post(route,files={'upload_file':open(file, 'rb')})

    print(r.text)

if action=='NLP':
    # Streamtabular
    route = url+'nlp'
    payload = 'He is smart, handsome, and funny'
    r = requests.post(route,json=payload)
    sentiment = {'pos':'Positive', 'neg':'Negative', 'neu':'Neutral'}
    print(sentiment[r.text])





