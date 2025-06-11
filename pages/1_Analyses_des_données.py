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
import matplotlib.pyplot as plt
df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')

st.markdown(""":bar_chart: Le dataset utilisé pour ce projet est un fichier Parquet issu des base IMDB et TMDB, contenant des informations sur les films, y compris les titres, les genres, les pays d'origine, les notes moyennes ainsi que d'autres attributs pertinents. Il a été nettoyé et préparé pour une analyse approfondie. Il représente un référencement de 9 269 films.""")


st.markdown(""":point_right: **Identification des acteurs les plus présents et les périodes associées**""")

df['annee de sortie'] = df['annee de sortie'].fillna(0).astype(int)



st.markdown(""":point_right: **Evolution de la durée moyenne des films au fil des années**""")

df_grouped_duree = df.groupby('annee de sortie')['duree'].mean().sort_index()

fig, ax = plt.subplots(figsize=(8, 3.5))
ax.plot(df_grouped_duree.index, df_grouped_duree.values, color='blue')
ax.set_xlabel("Année")
ax.set_ylabel("Durée moyenne (min)")

xticks = df_grouped_duree.index[::5]  # garde une année sur 5
ax.set_xticks(xticks)
ax.set_xticklabels(xticks, rotation=45)

st.pyplot(fig)

st.markdown(""":point_right: **Films les mieux notés et les caractéristiques qu’ils partagent**""")

