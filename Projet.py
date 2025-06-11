import streamlit as st
import pandas as pd 

df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')

st.set_page_config(page_title='Projet',page_icon='🏠',layout='wide')
st.title('PROJET "CREUSE CINE PLUS"')
st.subheader("Contexte et objectifs")
st.markdown(""":film_frames:
Un cinéma en perte de vitesse situé dans la Creuse vous demande de créer un moteur de recommandations de films qui à terme, enverra des notifications aux clients via Internet.
Le client vous donne une base de données de films basée sur les plateformes IMDb et TMDB.
Commencez par une étude de marché sur la consommation de cinéma dans la région de la Creuse, afin de mieux comprendre les attentes et les préférences du public local. 
Cette étape préliminaire vous permettra de définir une orientation adaptée pour la suite de l’analyse de votre base de données.

Après cette étude, réalisez une analyse approfondie de votre base de données pour identifier des tendances et caractéristiques spécifiques. 
Cette analyse devrait inclure : 
- l’identification des acteurs les plus présents et les périodes associées 
- l’évolution de la durée moyenne des films au fil des années
- les films les mieux notés et les caractéristiques qu’ils partagent

Sur la base des informations récoltées, vous pourrez affiner votre programmation en vous spécialisant par exemple sur les films des années 90 ou les genres d’action et d’aventure, afin de mieux répondre aux attentes du public identifié lors de l’étude de marché."""
)

st.subheader("Etapes du projet")
st.markdown(""":point_right:**Etude de marché** : Analyse des tendances de consommation de cinéma dans la Creuse""")

st.subheader("Personnes impliquées")

st.subheader("Outils utilisés")