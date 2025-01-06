

import streamlit as st
import spacy
import pickle

# Load the saved model
with open('logistic_regression.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the spacy model
nlp = spacy.load('en_core_web_sm')

def run_ml_app():
    st.title("Fake News Detector")

    # Get the news text from the user
    news_text = st.text_area("Enter the news text here")
    
    if not news_text:
        st.warning("Please enter some text to analyze.")
        return

    # Process the news text using spaCy
    doc = nlp(news_text)
    text_vec = doc.vector

    # Make prediction using the loaded model
    prediction = model.predict([text_vec])
    # Button to submit the news for prediction
    if st.button("Submit"):
        # Display the prediction
        if prediction[0] == 0:
            st.error("The news is **FAKE**.")
        elif prediction[0] == 1:
            st.success("The news is **REAL**.")
