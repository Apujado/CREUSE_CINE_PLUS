import streamlit as st

st.set_page_config(page_title="Data", page_icon="📊",layout="wide")

st.title("Data 4 U")
st.subheader(":one: Etude préliminaire du marché cinématographique en Creuse ")
st.subheader(":two: Analyse de la base de données")
st.write("""
Cette section présente une analyse de la base de données des films, mettant en évidence quelques tendances et caractéristiques spécifiques. 
L'objectif est d'identifier des éléments clés qui pourraient influencer la programmation du cinéma.
""")

import pandas as pd 
df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')

st.markdown(""":bar_chart: Le dataset utilisé pour ce projet est un fichier Parquet issu des base IMDB et TMDB, contenant des informations sur les films, y compris les titres, les genres, les pays d'origine, les notes moyennes ainsi que d'autres attributs pertinents. Il a été nettoyé et préparé pour une analyse approfondie. Il représente un référencement de 9 269 films.""")


st.markdown(""":point_right: **Identification des acteurs les plus présents et les périodes associées**""")
st.markdown(""":point_right: **Evolution de la durée moyenne des films au fil des années**""")
st.markdown(""":point_right: **Films les mieux notés et les caractéristiques qu’ils partagent**""")