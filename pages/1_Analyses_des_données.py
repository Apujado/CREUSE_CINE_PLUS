import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

st.set_page_config(page_title="Data", page_icon="📊",layout="wide")

st.markdown("<h1 style='text-align: center;color: black;'>ANALYSES</h1>",unsafe_allow_html=True)
st.subheader(":one: Etude préliminaire du marché cinématographique en Creuse ")

st.image("C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/MEDIA/Capture d'écran 2025-06-11 232052.png")
st.image("C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/MEDIA/Capture d'écran 2025-06-11 232125.png")
st.markdown(""":loudspeaker:**Une préférence pour le cinéma Français qui s'accentue** avec en 2022 une part qui grimpe à 52%. """)
st.image("C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION\Wild Code School/CREUSE_CINE_PLUS/MEDIA/Capture d'écran 2025-06-12 203721.png")
st.markdown(":mag_right:**Conclusions et préconnisations:  pour le filtrage des bases de données, les variables à conserver et les choix des contenus à selectionner / critères retenus**:construction:")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.subheader(":two: Analyse de la base de données")

st.markdown("""
Cette section présente une analyse de la base de données des films, mettant en évidence quelques tendances et caractéristiques spécifiques. 
L'objectif est d'identifier des éléments clés qui pourraient influencer la programmation du cinéma.
""")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')
df['medaille'] = df['noteMoyenne'].apply(lambda x:'bronze' if x<5.6 else 'argent' if x>=5.6 and x<=6.3 else 'or' if x>6.3 and x<=6.8 else 'platine' if x>6.8 else 'non classe')
df_best_film = df[df['medaille']=='platine']

st.markdown(""":bar_chart: Le dataset utilisé pour ce projet est un fichier Parquet issu des base IMDB et TMDB, contenant des informations sur les films, y compris les titres, les genres, les pays d'origine, les notes moyennes ainsi que d'autres attributs pertinents. Il a été nettoyé et préparé pour une analyse approfondie. Il représente un référencement de 9 269 films.""")
st.markdown(""":point_right: **Visualisation de la Base de Donnée**""")
st.data_editor(df)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown(""":point_right: **Représentativité de la provenance des contenus**:construction:""")
films_par_pays = df['pays'].value_counts()
top5 = films_par_pays.head(5)
autres = films_par_pays[5:]

top5_et_autres = top5.copy()
top5_et_autres['Autres'] = autres.sum()
#creer un dataframe
films_df = top5_et_autres.reset_index()
films_df.columns = ['Pays', 'Nombre de films']

# Calculer les pourcentages
total = films_df['Nombre de films'].sum()
films_df['Pourcentage'] = ((films_df['Nombre de films'] / total) * 100).round(0)

# Camembert
fig = px.pie(films_df,
             names='Pays',
             values='Pourcentage',
             title='Films par pays (Top 5 + Autres)',
            color='Pays')
        
         
st.plotly_chart(fig)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown(""":point_right: **Représentativité par genre principal**:construction:""")
df["genre_principal"] = df["genres"].str.split(",").str[0]

films_par_genre = df["genre_principal"].value_counts().reset_index()
films_par_genre.columns = ['genre_principal', 'count']

chart = alt.Chart(films_par_genre).mark_bar().encode(
    x='count:Q',
    y=alt.Y('genre_principal:N', sort='-x'),
    color='genre_principal:N'
).properties(
    width=700,
    height=400
)

st.altair_chart(chart)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown(""":point_right: **Identification des acteurs les plus présents et périodes associées**:construction:""")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown(""":point_right: **Evolution de la durée moyenne des films au fil des années**:construction:""")

df['annee de sortie'] = df['annee de sortie'].fillna(0).astype(int)
df['décennie'] = (df['annee de sortie'] // 10) * 10

df_grouped_duree = df.groupby('décennie')['duree'].mean().round(0).reset_index()

line_chart = alt.Chart(df_grouped_duree).mark_line(
    point=True,
    color='#F2C038'  
).encode(
    x=alt.X('décennie:O', title='Décennie', axis=alt.Axis(labelAngle=-45, labelOverlap=False)),
    y=alt.Y('duree:Q', title='Durée moyenne (min)'),
    tooltip=['décennie', 'duree']
).properties(
    width=700,
    height=400
).configure_title(
    fontSize=18,
    anchor='start',
    color='gray'
).interactive()

st.altair_chart(line_chart)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown(""":point_right: **Caractéristiques partagées par les films les mieux notés soit catégorisés avec une médaille de platine (2295 films ).**""")
st.markdown("""L'objectif est d'extraire des mots clés qui pourraient ensuite permettre la création d'un outil prédictif "Top ou Flop"
            sur la base d'informations fournies dans la fiche du film. Outil d'aide à la séléction en vue d'enrichir l'offre proposée aux utilisateurs-trices.""")
st.markdown(""" **Step 1:** Analyse réalisée en regroupant les synopsis, les titres originaux, les genres, noms et prénoms des acteurs-trices & réalisateurs-trices.:construction:""")
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

nltk.download('stopwords')
nltk.download('punkt')

text_columns = ['synopsis', 'original_title', 'genres', 'prenom_nom']
texte_full = ' '.join(df_best_film[text_columns].astype(str).sum())
texte_clean = texte_full.lower()
texte_clean = re.sub(r"['\"«»]", "", texte_clean)
tokens2 = word_tokenize(texte_clean)

# Mettre en minuscules, enlever la ponctuation et les stopwords 
stop_words_en = set(stopwords.words("english"))  
stop_words_fr = set(stopwords.words("french"))
stop_words = stop_words_fr.union(stop_words_en) 
tokens2_clean = [
    word for word in tokens2 
    if word.isalpha() and word not in stop_words
]

fdist = nltk.FreqDist(tokens2_clean)

# Top 20 des mots les plus fréquents --------------------------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

top20 = fdist.most_common(20)

words = [word for word, frequency in top20]
frequencies = [frequency for word, frequency in top20]
df_top20 = pd.DataFrame({
    'words': words,
    'frequencies': frequencies})

chart = alt.Chart(df_top20).mark_bar(color='#76B041').encode(
    x=alt.X('frequencies:Q', title='Fréquence'),
    y=alt.Y('words:N', sort='-x', title='Mots') 
).properties(
    title='Top 20 des mots les plus fréquents'
)

st.altair_chart(chart, use_container_width=True)
            

# Nuage des mots---------------------------------------------------------------------------------------------------------------------------------------------------------------------


st.markdown("""**Step 2: Visualisation graphique de type nuage de mots.**:construction:""")
st.markdown(""" :bulb:NB: On note ici une différence entre les données sur le Top 20  et le rendu. A explorer les raisons de l'écart.""")

from wordcloud import WordCloud
wordcloud2 = WordCloud(
    width=480, 
    height=480, 
    max_font_size=200, 
    min_font_size=10,
    background_color='white'
).generate(' '.join(tokens2_clean))  

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(wordcloud2, interpolation="bilinear")
ax.axis("off")
plt.margins(x=0, y=0)
st.pyplot(fig)

#----------------------------------------------------------------------------------------------------------------------------------------------------
st.markdown(""":point_right::bulb: **A partir des résultats construire un modèle qui prédise le top ou flop**:construction:""")

