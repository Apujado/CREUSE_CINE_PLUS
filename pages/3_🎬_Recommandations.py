import streamlit as st

st.set_page_config(page_title="Recommandations", page_icon="🎬", layout="wide")

st.title("Movies 4 U")
st.subheader("Selection de films recommandés")
st.write("""Cette section propose une sélection de films recommandés basée sur l'analyse des données. 
    Les recommandations sont faites en tenant compte des préférences du public local et des tendances identifiées.""")

import pandas as pd 
df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')



