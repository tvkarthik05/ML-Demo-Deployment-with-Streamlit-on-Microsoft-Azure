import streamlit as st
import os
import requests


os.environ["USERNAME"] = 'demo'
os.environ["PASSWORD"] = 'password'
url = 'http://localhost:80/'

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    </style>
    """

# UI Layout
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Sidebar options
user_name = st.sidebar.text_input("UserName:", value="", type="password")
password = st.sidebar.text_input("Password:", value="", type="password")
demo_option = st.sidebar.radio("Demo:", ['Tabular', 'Computer Vision', 'NLP'])

if (password != os.environ["PASSWORD"]) | (user_name != os.environ["USERNAME"]):
    st.error("the username or password you entered is incorrect")
else:
    st.title('Demo Platform')

    ##################################################################################################
    # Tabular Platform
    ##################################################################################################
    if demo_option=='Tabular':
        st.subheader('Tabular')
        input = (
            'Single',
            'Batch')

        option = st.selectbox("Select the algo", input)
        if option=='Single':
            Sepal_Length = st.text_input("Sepal_Length", value='')
            Sepal_Width = st.text_input("Sepal_Width", value='')
            Petal_Length = st.text_input("Petal_Length", value='')
            Petal_Width = st.text_input("Petal_Width", value='')

                        
        if option=='Batch':
            uploaded_file = st.file_uploader("Upload your File here")

        tab_button = st.button('Run')

        if tab_button:
            if option=='Single':
                route = url+'streamtabular'
                payload = { 'Sepal_Length':float(Sepal_Length), 
                            'Sepal_Width':float(Sepal_Width), 
                            'Petal_Length':float(Petal_Length), 
                            'Petal_Width':float(Petal_Width)}

                r = requests.post(route,json=payload)
                st.write('The predicted value is - ', r.text) 
            
            if option=='Batch':
                route = url+'batchtabular'
                file = uploaded_file
                r = requests.post(route,files={'upload_file':file})

                print(r.text)
                st.write('The predicted values are - ', r.text) 


    ##################################################################################################
    # CV Platform
    ##################################################################################################
    if demo_option=='Computer Vision':
        st.subheader('Computer Vision')
        
        uploaded_file = st.file_uploader("Upload your Image here")
        cv_button = st.button('Run')

        if cv_button:
            st.image(uploaded_file, use_column_width=True)

            route = url+'cv'
            r = requests.post(route,files={'upload_file': uploaded_file})
            
            print(r.text)
            st.write('The predicted value is - ', r.text) 

    ##################################################################################################
    # NLP Platform
    ##################################################################################################
    if demo_option=='NLP':
        st.subheader('NLP')
        
        user_text = st.text_input("Enter you text here", value='')

        nlp_button = st.button('Run')

        if nlp_button:
            route = url+'nlp'
            r = requests.post(route, json=user_text)
            
            print(r.text)
            sentiment = {'pos':'Positive', 'neg':'Negative', 'neu':'Neutral'}
            st.write('The Sentiment is - ', sentiment[r.text]) 
