import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from annotated_text import annotated_text, annotation

def load_data():
    try:
        # Charger les données des régions avec un encodage spécifique
        data = pd.read_excel('./Data/Département/Depart.xlsx')
        return data
    except pd.errors.ParserError as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        return None

def load_graph():
    try:
        # Charger les données des régions avec un encodage spécifique
        data = pd.read_excel('./Data/Département/Graph_popu_dep.xlsx')
        return data
    except pd.errors.ParserError as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        return None

def show():
    st.title(":blue[Données liées aux Départements]")

    data = load_data()
    graph_data = load_graph()

    if data is None or graph_data is None:
        st.write("Les données n'ont pas pu être chargées.")
        return
    
    # Affichage du nom du département
    dep = st.selectbox('Sélectionnez un département', data['Département'].unique(), key='selectbox_dep')

    dep_data = data[data['Département'] == dep].iloc[0]

    st.divider()

    st.write(f"#### Le marché immobilier à :blue[_{dep}_] 🗾")

    # Affichage des prix 
    col1, col2 = st.columns(2)

    with col1:
        st.write("#### 🏢 :blue[Appartement]")
        st.write("Prix m2 moyen")
        with st.container():
            annotated_text(
                " ",
                annotation(f"""{dep_data["Prix m2 moyen appartement"]}""", "€", "#faf", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
        st.write("Loyer m2 moyen")
        with st.container():
            annotated_text(
                " ",
                annotation(f"""{dep_data["Loyer m2 moyen appartement"]}""", "€", "#faf", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )

    with col2:
        st.write("#### 🏠 :blue[Maison]")
        st.write(f"Prix m2 moyen")
        with st.container():
            annotated_text(
                " ",
                annotation(f"""{dep_data["Prix m2 moyen maison"]}""", "€", "#faf", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
        st.write(f"Loyer m2 moyen")
        with st.container():
            annotated_text(
                " ",
                annotation(f"""{dep_data["Loyer m2 moyen maison"]}""", "€", "#faf", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    
    st.divider()

    st.write(f"#### Informations sur :blue[_{dep}_] 🗾")

    # Affichage des informations liées au département
    colA, colB, colC = st.columns(3)

    with colA:
        with st.container(border=True):
            annotated_text(
                "🌍 Population: ",
                annotation(f"""{dep_data["Démographie "]}""", "habitants", "#afa", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    
    with colB:
        with st.container(border=True):
            annotated_text(
                "📏 Superficie: ",
                annotation(f"""{dep_data["Superficie(km2)"]}""", "km2", "#fea", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )

    with colC:
        with st.container(border=True):
            annotated_text(
                "👤 Densité: ",
                annotation(f"""{dep_data["Densité(hab./km2)"]}""", "hab./km2", "#8ef", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    
    colD, colE = st.columns(2)
    with colD:
        with st.container(border=True):
            annotated_text(
                "🏞️ Communes: ",
                annotation(f"""{dep_data["Nombre de communes"]}""", "Cmnes", "#afa", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    
    with colE:
        with st.container(border=True):
            annotated_text(
                "Myn hab/Cmnes: ",
                annotation(f"""{dep_data["Moyenne d'habitants par commune"]}""", "hab./Cmnes", "#fea", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    st.divider()

    st.write(f"Évolution de la population à :blue[_{dep}_] 🗾")

    # Convertir les colonnes en format numérique après avoir retiré les points des milliers
    for col in graph_data.columns[1:]:
        graph_data[col] = graph_data[col].str.replace('.', '').str.replace(',', '.').astype(float)

    # Transformer les données pour avoir les années comme une colonne distincte
    data_melted = pd.melt(graph_data, id_vars=["Département"], var_name="Année", value_name="Population")

    # Convertir la colonne "Année" en entier (en supprimant les notes entre crochets)
    data_melted["Année"] = data_melted["Année"].str.extract('(\d+)', expand=False).astype(int)

    # Filtrer les données pour le département sélectionné
    department_data = data_melted[data_melted['Département'] == dep]

    # Créer le graphique avec Streamlit
    st.bar_chart(department_data.set_index('Année')['Population'])



