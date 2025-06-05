import streamlit as st
import pandas as pd
import urllib.parse


df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')

query_params = st.query_params
film = query_params.get("film", [""])[0] 

if "film" in query_params:
    titre_film = urllib.parse.unquote_plus(query_params["film"][0])
    film = df[df["titre_intl"].str.strip().str.lower() == titre_film.strip().lower()]


    if not film.empty:
        film = film.iloc[0]
        st.title(film["titre_intl"])
        st.markdown(f"**Titre original** : *{film['original_title']}*")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f"**Année de sortie** : {film['annee de sortie']}")
            st.markdown(f"**Durée** : {film['duree']} min")
            st.markdown(f"**Genres** : {film['genres']}")
            st.markdown(f"**Pays** : {film['pays']}")
            st.markdown(f"**Production** : {film['societe_prod']}")
            st.markdown(f"**Intervenant** : {film['prenom_nom']} ({film['role']})")
        with col2:
            st.subheader("Synopsis")
            st.write(film["synopsis"])
            st.markdown(f"**Note** : ⭐ {film['noteMoyenne']:.2f} ({int(film['nbre_votes'])} votes)")
            st.markdown(f"**Popularité** : 🔥 {film['popularite']:.2f}")

        if pd.notna(film["fond_ecran"]):
            st.image(film["fond_ecran"], use_column_width=True)
    else:
        st.error("Film non trouvé.")
else:
    st.warning("Aucun film sélectionné.")
