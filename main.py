import streamlit as st
import pandas as pd 
df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')
st.set_page_config(page_title='Creuse Ciné Plus',page_icon=':movie_camera:',layout='wide')
st.title('CREUSE CINE PLUS')

def page1():
    st.title("PROJET")
    st.write("Contexte et objectifs")
def page2():
    st.title("Data 4 U")
    st.write("Tout ce que vous avez toujours voulu savoir sans oser le demander.")
def page3():
    st.title("Movies 4 U")
    st.write("Selectionne un film et découvre en d'autres que tu pourrais bien aimer!")

pg=st.navigation([
    st.Page(page1, title="Projet", icon="🔥"),
    st.Page(page2, title="Analyse Data", icon="📊"),
    st.Page(page3, title="Recommandations Films", icon="🎬"),
])
pg.run()