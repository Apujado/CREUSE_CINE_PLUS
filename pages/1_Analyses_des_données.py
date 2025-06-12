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
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.subheader(":two: Analyse de la base de données")

st.markdown("""
Cette section présente une analyse de la base de données des films, mettant en évidence quelques tendances et caractéristiques spécifiques. 
L'objectif est d'identifier des éléments clés qui pourraient influencer la programmation du cinéma.
""")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

df = pd.read_parquet('C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/CREUSE_CINE_PLUS/films_groupes.parquet')
df['medaille'] = df['noteMoyenne'].apply(lambda x:'bronze' if x<5.6 else 'argent' if x>=5.6 and x<=6.3 else 'or' if x>6.3 and x<=6.8 else 'platine' if x>6.8 else 'non classe')


st.markdown(""":bar_chart: Le dataset utilisé pour ce projet est un fichier Parquet issu des base IMDB et TMDB, contenant des informations sur les films, y compris les titres, les genres, les pays d'origine, les notes moyennes ainsi que d'autres attributs pertinents. Il a été nettoyé et préparé pour une analyse approfondie. Il représente un référencement de 9 269 films.""")
st.markdown(""":point_right: **Visualisation de la Base de Donnée**""")
st.data_editor(df)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown(""":point_right: **Représentativité de la provenance des contenus**""")
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

st.markdown(""":point_right: **Représentativité par genre principal**""")
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

st.markdown(""":point_right: **Identification des acteurs les plus présents et périodes associées**""")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown(""":point_right: **Evolution de la durée moyenne des films au fil des années**""")

df['annee de sortie'] = df['annee de sortie'].fillna(0).astype(int)
df['décennie'] = (df['annee de sortie'] // 10) * 10

df_grouped_duree = df.groupby('décennie')['duree'].mean().round(0).reset_index()

line_chart = alt.Chart(df_grouped_duree).mark_line(point=True).encode(
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

st.markdown(""":point_right: **Films les mieux notés (médaille platine soit dans la bdd 2295 films ) et caractéristiques qu’ils partagent**""")
df_best_film = df[df['medaille']=='platine']

#----------------------------------------------------------------------------------------------------------------------------------------------------
st.markdown(""":point_right: **A partir des résultats construire un modèle qui prédise le top ou flop**""")

