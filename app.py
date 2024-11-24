import streamlit as st
from ml_app import run_ml_app

import streamlit.components.v1 as stc

html_temp = """
            <div style="background-color:#3872fb;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Fake News Detection App</h1>
		    <h4 style="color:white;text-align:center;">NEXUS SQUAD Team </h4>
		    </div>
            """

desc_temp = """
            ### Fake News Detection App
            This app utilizes advanced machine learning techniques to accurately identify fake news articles. Simply input the text of a news article, and our model will analyze it and provide a verdict: "Real" or "Fake."
            #### Data Source
            -  https://www.kaggle.com/code/rajatkumar30/fake-news-prediction-92-5-accuracy/input
            #### App Content
            - Machine Learning Section
            """


def main(): #Homepage
    stc.html(html_temp)

    menu = ['Home', 'Machine Learning']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == "Home":
        st.subheader("Welcome to Home Page")
        st.markdown(desc_temp)
    elif choice == "Machine Learning" :
        # st.subheader("Machine Learning")
        run_ml_app()

if __name__ == '__main__' :
    main()
    