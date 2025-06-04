import streamlit as st
import pandas as pd 
df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')
st.set_page_config(page_title="Analyse data", page_icon="📊",layout="wide")

st.title("Data 4 U")
st.subheader("Analyse de la base de données")
st.write("""
Cette section présente une analyse approfondie de la base de données des films, mettant en évidence les tendances et caractéristiques spécifiques. 
L'objectif est d'identifier des éléments clés qui peuvent influencer la programmation du cinéma.
""")
st.dataframe(df.head(10)) 


