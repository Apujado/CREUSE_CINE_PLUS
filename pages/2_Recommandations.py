import streamlit as st
import pandas as pd 
import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')
df['medaille'] = df['noteMoyenne'].apply(lambda x:'bronze' if x<5.6 else 'argent' if x>=5.6 and x<=6.3 else 'or' if x>6.3 and x<=6.8 else 'platine' if x>6.8 else 'non classe')

#ML pour la recommandation de films 
nltk.download('punkt')
nltk.download('stopwords')

stem_en = SnowballStemmer("english")
stop_words = set(stopwords.words('english'))

def clean(synopsis):
    tokens = word_tokenize(synopsis.lower(), language='english')
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    stemmed_tokens = [stem_en.stem(word) for word in tokens]
    return " ".join(stemmed_tokens)

# Fonction de recommandation
def recommander_films(titre_film, df, n=5):
    if titre_film not in df['original_title'].values:
        st.warning("Film non trouvé.")

    df_temp = df.copy()
    df_temp['synopsis_clean'] = df_temp['synopsis'].apply(clean)

    # Vectorisation TF-IDF sur les synopsis nettoyés
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df_temp['synopsis_clean'])

    # Trouver l'index du film
    idx = df[df['original_title'] == titre_film].index[0]

    # Calcul de similarité cosine
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Récupérer les scores de similarité
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Exclure le film lui-même et récupérer les n plus similaires
    top_indices = [i for i, score in sim_scores[1:n+1]]
    
    return df_temp.iloc[top_indices]

#Remplissage de la page ------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title="Recommandations", page_icon="🎬", layout="wide")

st.markdown("<h1 style='text-align: center;color: black;'>RECOMMANDATIONS</h1>",unsafe_allow_html=True)

st.write("""Cette rubrique vous propose une selection de films basée sur l'analyse des données précédentes.
Veuillez choisir un genre puis un pays d'origine pour filtrer la liste des 9 269 films disponibles.

Tous les contenus proposés sont soit en langue française soit doublés, ou en version originale sous-titrés français. 
L'affichage des films se fait pas ordre de popularité décroissant et est limité au Top 10.
La fiche du film apparaitra en dessous après avoir cliqué sur le bouton "Voir fiche". Un retour en arrière est possible.
Une suggestion de 5 autres films que vous pourriez aussi apprécier vous sera également faite. Soyez patients le temps que le petit robot travaille et trouve la solution.:female-detective:""")



#creation des 2 filtres sur le genre et le pays car il y un choix de 9600 films dans la base de données -------------------------------------------------------------------------------------

df["genre_principal"] = df["genres"].str.split(",").str[0]
genre_choisi = st.selectbox("**Veuillez choisir le genre souhaité**", sorted(df["genre_principal"].unique()))
df_filtre = df[df["genre_principal"] == genre_choisi]
st.write(f"Nombre de films disponibles pour le genre {genre_choisi} : {len(df_filtre)}")

pays_disponibles=sorted(df_filtre['pays'].unique())
pays_choisi= st.selectbox("**Veuillez choisir l'origine du film souhaité**",pays_disponibles)
df_filtre2 = df_filtre[df_filtre["pays"] == pays_choisi]
st.write(f"Nombre de films disponibles pour le pays {pays_choisi} : {len(df_filtre2)}")

# affichage des films filtrés sous forme de vignettes avec l'affiche du film et un bouton qui inclue le titre et qui envoie vers la fiche du film ------------------------------------------------

base_url = "https://image.tmdb.org/t/p/w500"
if "film_selectionne" not in st.session_state:
    st.session_state.film_selectionne = None

st.markdown("### Résultats correspondants :")
df_filtre2 = df_filtre2.sort_values(by='popularite', ascending=False) .head(10)

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

            if st.button(f"Voir fiche : {ligne['titre_intl']}", key=f"voir_{index}"):
                st.session_state.film_selectionne = ligne


if st.session_state.film_selectionne is not None:
    film = st.session_state.film_selectionne
    emoji_medaille = {
        'platine': '💖',
        'or': '🥇',
        'argent': '🥈',
        'bronze': '🥉'
    }
    medaille = film['medaille']
    emoji = emoji_medaille.get(medaille, '')

    with st.expander(f"🎞️ Fiche : {film['titre_intl']}", expanded=True):
        st.markdown(f"**Titre original** : *{film['original_title']}*")

        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f"**Année de sortie** : {film['annee de sortie']}")
            st.markdown(f"**Durée** : {film['duree']} min")
            st.markdown(f"**Genres** : {film['genres']}")
            st.markdown(f"**Pays** : {film['pays']}")
            st.markdown(f"**Production** : {film['societe_prod']}")
            st.markdown(f"**Casting** : {film['prenom_nom']} ({film['role']})")
        with col2:
            st.subheader("Synopsis")
            st.write(film["synopsis"])
            st.markdown(f"**Popularité** : 🔥 {film['popularite']:.2f}")
            st.markdown(f"**Médaille** : {emoji}")
            st.markdown(f"**Nombre de votes** : {int(film['nbre_votes'])}")

        if st.button("Fermer la fiche", key="fermer_fiche"):
            st.session_state.film_selectionne = None
            st.rerun()          

        recommandations = recommander_films(film['original_title'], df)

        if not recommandations.empty:
            st.markdown("### 🎁 Voici des suggestions qui pourraient vous intéresser:")

            nb_par_ligne = 5
            lignes_reco = [recommandations.iloc[i:i+nb_par_ligne] for i in range(0, len(recommandations), nb_par_ligne)]

            for bloc in lignes_reco:
                colonnes = st.columns(nb_par_ligne)
                for i, (index, ligne) in enumerate(bloc.iterrows()):
                    with colonnes[i]:
                        if pd.notna(ligne['affiche']):
                            image_url = base_url + ligne['affiche']
                            st.image(image_url, width=300)

                        emoji_medaille = {
                            'platine': '💖',
                            'or': '🥇',
                            'argent': '🥈',
                            'bronze': '🥉'
                        }
                        medal_emoji = emoji_medaille.get(str(ligne['medaille']).lower(), '')
                        st.caption(f"{ligne['titre_intl']} {medal_emoji}")

                       
