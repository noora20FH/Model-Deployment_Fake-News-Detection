import streamlit as st
from ml_app import run_ml_app
from team import team_member
from data_preprocessing import data_preprocessing
from eda import eda
from model import model

import streamlit.components.v1 as stc

html_temp = """
            <div style="background-color:#3872fb;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Fake News Detection App</h1>
		    <h4 style="color:white;text-align:center;">NEXUS SQUAD Team </h4>
		    </div>
            """

desc_temp = """

            ### Fake News Detection App
            Aplikasi ini memanfaatkan teknik-teknik pembelajaran mesin tingkat lanjut untuk mengidentifikasi artikel berita palsu secara akurat. Cukup masukkan teks dari sebuah artikel berita, dan model kami akan menganalisisnya dan memberikan keputusan: "Real" atau "Fake."
            #### Sumber Dataset
            -  https://www.kaggle.com/code/rajatkumar30/fake-news-prediction-92-5-accuracy/input
            #### Isi Streamlit App
            - Home
            - Team
            - Data Preprocessing
            - Exploratory Data Analysis
            - Model
            - Test Model
            """


def main(): #Homepage
    stc.html(html_temp)

    menu = ['Home', 'Team','Data Preprocessing','Exploratory Data Analysis','Model','Test Model']
    choice = st.sidebar.selectbox('Menu', menu)
    st.sidebar.warning("Created by Nexus Squad")
    if choice == "Home":
        st.subheader("Welcome to Home Page")
        
        st.write("# Fake News Detection")
        # st.sidebar.warning("Created by Nexus Squad")

        st.markdown(
            """
            Selamat datang di Aplikasi Fake News Detection.
            Aplikasi ini disusun sebagai Final Project pada kelas Data Science & AI Fundamental Batch 42 yang diselenggarakan oleh DigitalSkola.
            ### Pengantar
            Sebagaimana yang diketahui bahwa era digital membawa dampak yang besar pada kehidupan manusia, mulai dari penyebaran informasi dan lain sebagainya. 
            Dari segi penyebaran informasi seperti kita ketahui bersama informasi dapat diakses dengan cepat dan mudah, baik untuk mencari materi pelajaran, jurnal ilmiah, maupun sumber belajar lainnya.
            Dengan penyebaran informasi yang begitu cepat dan masif, kita sebagai penerima informasi tersebut tidak sempat melakukan pengecekan terhadap informasi tersebut.
            Sehingga berpengaruh secara tidak langsung kepada keputusan yang diambil berdasarkan informasi tersebut.
            \n
            Untuk itu diperlukan suatu upaya untuk mengecek informasi tersebut apakah merupakan informasi asli atau bukan. 
            Salah satu cara untuk mengecek informasi tersebut adalah dengan menggunakan algoritma machine learning dengan menggunakan dataset yang telah disediakan.
            \n
            Akhirnya kami selaku penyusun mengucapkan terima kasih atas semua yang telah membantu kami dalam membuat aplikasi ini, terutama dari para mentor dan anggota tim yang telah membantu penyusunan aplikasi ini dari awal hingga akhir.
            Semoga aplikasi ini bermanfaat bagi kita semua. """)

        st.markdown(desc_temp)
    elif choice == "Team":
        team_member()
    elif choice == "Data Preprocessing":
        data_preprocessing()
    elif choice == "Exploratory Data Analysis":
        eda()
    elif choice == "Model":
        model()
    elif choice == "Test Model" :
        # st.subheader("Machine Learning")
        run_ml_app()

if __name__ == '__main__' :
    main()
    