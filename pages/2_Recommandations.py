import streamlit as st
from urllib.parse import urlencode, quote_plus
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Recommandations", page_icon="🎬", layout="wide")

st.title("Movies 4 U")
st.subheader("Recommandations")
st.write("""Cette rubrique vous propose une selection de films basé sur l'analyse des données précédentes.
Veuillez choisir un genre puis un pays d'origine.
Les recommandations sont faites en tenant compte des préférences des utilisateurs.trices.
Tous les contenus proposés sont soit en langue française soit doublés ou en version originale sous-titrés en français. 
L'affichage des films se fait par ordre de note moyenne décroissante.
Vous pouvez consulter la fiche du film en le sélectionnant grâce au bouton "Voir" situé sous l'affiche.
Vous accéderez ainsi également à une suggestion de 5 autres films que vous pourriez aussi apprécier.""")

import pandas as pd 
df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')

#creation des 2 filtres sur le genre et le pays car il y un choix de 9600 films dans la base de données 

df["genre_principal"] = df["genres"].str.split(",").str[0]
genre_choisi = st.selectbox("**Veuillez choisir le genre souhaité**", sorted(df["genre_principal"].unique()))
df_filtre = df[df["genre_principal"] == genre_choisi]
st.write(f"Nombre de films disponibles pour le genre {genre_choisi} : {len(df_filtre)}")

pays_disponibles=sorted(df_filtre['pays'].unique())
pays_choisi= st.selectbox("**Veuillez choisir l'origine du film souhaité**",pays_disponibles)
df_filtre2 = df_filtre[df_filtre["pays"] == pays_choisi]
st.write(f"Nombre de films disponibles pour le pays {pays_choisi} : {len(df_filtre2)}")

# affichage des films filtrés sous forme de vignettes avec l'affiche du film et un bouton qui inclue le titre et qui renvoie vers la fiche du film 

base_url = "https://image.tmdb.org/t/p/w500"

st.markdown("### Résultats correspondants :")
df_filtre2 = df_filtre2.sort_values(by='popularite', limit = 10, ascending=False) 

nb_par_ligne = 5 
lignes = [df_filtre2.iloc[i:i+nb_par_ligne] for i in range(0, len(df_filtre2), nb_par_ligne)]

for bloc in lignes:
    colonnes = st.columns(nb_par_ligne)
    for i, (index, ligne) in enumerate(bloc.iterrows()):
        with colonnes[i]:
            if pd.notna(ligne['affiche']):
                image_url = base_url + ligne['affiche']
                st.image(image_url, width=300)
            st.caption(ligne['titre_intl']) 

            if st.button(f"Voir fiche : {ligne['titre_intl']}", key=index):
                st.experimental_set_query_params(film=quote_plus(ligne["titre_intl"]))
                switch_page("4_Fiche_Films")
    

