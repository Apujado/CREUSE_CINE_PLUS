import streamlit as st
import pandas as pd 

df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')

st.set_page_config(page_title='Creuse Ciné Plus',page_icon=':movie_camera:',layout='wide')
st.title('CREUSE CINE PLUS')
st.subheader("PROJET")
st.write("Contexte et objectifs")
st.markdown("""
Vous êtes un Data Analyst freelance. Un cinéma en perte de vitesse situé dans la Creuse vous demande de créer un moteur de recommandations de films qui à terme, enverra des notifications aux clients via Internet.
Le client vous donne une base de données de films basée sur la plateforme IMDb.
Commencez par une étude de marché sur la consommation de cinéma dans la région de la Creuse, afin de mieux comprendre les attentes et les préférences du public local. Cette étape préliminaire vous permettra de définir une orientation adaptée pour la suite de l’analyse de votre base de données.
Après cette étude, réalisez une analyse approfondie de votre base de données pour identifier des tendances et caractéristiques spécifiques. Cette analyse devrait inclure : l’identification des acteurs les plus présents et les périodes associées, l’évolution de la durée moyenne des films au fil des années ainsi que les films les mieux notés et les caractéristiques qu’ils partagent.
Sur la base des informations récoltées, vous pourrez affiner votre programmation en vous spécialisant par exemple sur les films des années 90 ou les genres d’action et d’aventure, afin de mieux répondre aux attentes du public identifié lors de l’étude de marché."""
)



