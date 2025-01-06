import streamlit as st

st.set_page_config(
    page_title="Nexus Squad",
    page_icon=":house:",
    layout="wide",
)

def team_member():
    st.write("### Tim Penyusun Aplikasi")
    

    st.markdown(
        """
        Adapun tim penyusun aplikasi ini terdiri dari :
        - Alan Setiawan (Ketua)
        - Nazhira Ghaisani (Anggota)
        - Noora Aulia Hidayat (Anggota)
        - Juan Prayogo (Anggota)
        - Anggit Setiadi (Anggota)
        - Agung Aditya Suhendra (Anggota)
        - Khadafi Zubaidi (Anggota)
    """
    )