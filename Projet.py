import streamlit as st
import pandas as pd 
import os
st.write(os.listdir())

df = pd.read_parquet('C:/Users/pujado/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')

st.set_page_config(page_title='Projet',page_icon='🚧',layout='wide')
st.markdown("<h1 style='text-align: center;color: black;'>CREUSE CINE PLUS</h1>",unsafe_allow_html=True)
st.subheader("**WORK IN PROGRESS**:construction:")
st.subheader("Contexte et objectifs")
st.markdown(""":cinema:
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

st.subheader("Etapes")
st.markdown(""":point_right:**Etudier le marché cible** : Analyse des tendances de consommation de cinéma dans la Creuse""")
st.markdown(""":point_right: **Créer une base de données** """)
st.markdown("""**Step 1**: Nettoyer, analyser et trier la base de donnée IMDB""")
st.markdown("""**Step 2**: Joindre la base de données TMDB en fonction des éléments nécessaires à la suite du projet pour garantir son évolutivité.""")
st.markdown(""":point_right: **Maquetter et définir l'architecture de l'app sur Streamlit** """)
st.markdown(""":point_right: **Exploiter les données collectées et procéder au remplissage des pages** """)
st.markdown("""**Step 1**: Rediger et tester certains codes complexes dans un Notebook externe ainsi que les visualisations avant intégration à Streamlit. """)
st.markdown("""**Step 2**: Tester différents formats de NLP et de tokenization pour la partie Machine Learning puis selectionner les modèles les plus pertinents. """)

st.subheader("Gestion du projet")
st.markdown("""Plannification des sprints et outils de brainstorming avec Trello et Miro""")
st.image("C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/MEDIA/Capture d'écran 2025-06-12 145101.png")

st.subheader("Parties prenantes")
st.markdown("<h5 style='text-align: left; color: brown;'>Etude de Marché</h>: <h6 style='text-align: left; color:black;'>Yrayou Yeo, Asah Ade, Georges Epee et Aurélie Pujado</h>",unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left; color: brown;'>Nettoyage de la bdd IMDB et assemblage avec la bdd TMDB</h>: <h6 style='text-align: left; color: black;'>Georges Epee et Aurélie Pujado</h>",unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left; color: brown;'>Reste du projet:</h> <h6 style='text-align: left; color: black;'>Aurélie Pujado</h>",unsafe_allow_html=True)
st.markdown("""**Remerciements** à Teddy Da Silva, notre formateur, pour son aide précieuse concernant les nombreux blocages techniques rencontrés mais aussi pour ses feedbacks nous ayant permis de délivrer ce 2ème projet.""")
st.subheader("Principaux Software utilisés")
col1, col2 = st.columns(2, border=True,vertical_alignment="top")
with col1:
    st.markdown("<h2 style='text-align: center; color: grey;'>Collecte, tri et exploitation des données pour l'étude</h2>",unsafe_allow_html=True)
    st.image("C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/MEDIA/th.jpeg")

with col2:
    st.markdown(":snake::panda_face:<h2 style='text-align: center; color: grey;'> Collecte, nettoyage, création et exploitation de la base de données</h2>",unsafe_allow_html=True)
    st.image("C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/MEDIA/th (1).jpeg")

col3,col4=st.columns(2, border=True,vertical_alignment="top")   
with col3:
    st.markdown("<h2 style='text-align: center; color: grey;'>Intégration à Streamlit</h2>",unsafe_allow_html=True)
    st.image("C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/MEDIA/deepnote.jpeg")

with col4:
    st.markdown("<h2 style='text-align: center; color: grey;'>Hébergement du projet</h2>",unsafe_allow_html=True)
    st.image("C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/MEDIA/github.jpeg")




st.markdown('''🐈 :rainbow[Accès au repository]: https://github.com/Apujado/CREUSE_CINE_PLUS''')