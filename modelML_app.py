import streamlit as st
import pandas as pd
import pickle
import re
import string

# Load the trained model and vectorizer
with open('logistic_regression_model.pkl', 'rb') as model_file:
    LR = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorization = pickle.load(vectorizer_file)

# Function to preprocess text
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# Function to output label
def output_label(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"

# Function for manual testing
def manual_testing(news):
    testing_news = {"text": [news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt)
    new_x_test = new_def_test["text"] 
        # Fit the vectorizer with the single sample
    vectorization.fit(new_x_test)
    new_xv_test = vectorization.transform(new_x_test)

    pred_LR = LR.predict(new_xv_test)
    return output_label(pred_LR[0])


# def manual_testing(news):
#     testing_news = {"text": [news]}
#     new_def_test = pd.DataFrame(testing_news)
#     new_def_test["text"] = new_def_test["text"].apply(wordopt)
#     new_x_test = new_def_test["text"]
#     new_xv_test = vectorization.transform(new_x_test)
#     pred_LR = LR.predict(new_xv_test)
#     return output_label(pred_LR[0])

def run_ml_app():
    # Streamlit app layout
    st.title("Fake News Prediction App")
    st.write("Enter the news article below:")

    # User input for news article
    news_input = st.text_area("News Article")

    # Button to submit the news for prediction
    if st.button("Submit"):
        if news_input:
            prediction = manual_testing(news_input)
            st.success(f"Prediction: {prediction}")
        else:
            st.error("Please enter a news article.")

