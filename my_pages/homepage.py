import streamlit as st
import pandas as pd
from annotated_text import annotated_text, annotation
import folium
from streamlit_folium import folium_static
import geopandas as gpd


def load_data():
    try:
        # Charger les données des régions avec un encodage spécifique
        data = pd.read_excel('./Data/Régions/InfoRegionMetro.xlsx')
        return data
    except pd.errors.ParserError as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        return None

def show():
    st.title(":blue[Données liées aux Régions]")

    data = load_data()

    if data is None:
        st.write("Les données n'ont pas pu être chargées.")
        return
    
    """
    Map Régions de France ################################################################################################################
    """

    st.write("#### :green[Map des Prix au m2 par Région]")
    
    # Charger le fichier GeoJSON
    geojson_file = "./Data/Régions/regions.geojson"  # Remplacez par le chemin de votre fichier GeoJSON
    gdf = gpd.read_file(geojson_file)

    # Charger les données de prix au m2 à partir du fichier Excel
    excel_file = "./Data/Régions/Prix au m2 régions .xlsx"  # Remplacez par le chemin de votre fichier Excel
    df = pd.read_excel(excel_file)

    # Merge GeoDataFrame with DataFrame sur la colonne 'Régions'
    gdf = gdf.merge(df, left_on='nom', right_on='Régions')  # 'nom' est la colonne des noms des régions dans le GeoJSON

    # Créer la carte Folium
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6,  tiles='Stamen Toner', attr='Stamen Toner')

    # Ajouter la couche Choropleth pour le prix moyen des appartements
    folium.Choropleth(
        geo_data=gdf,
        name='Prix moyen appartement',
        data=gdf,
        columns=['nom', 'Prix moyen appartement'],  # 'nom' est la clé et 'Prix moyen appartement' est la colonne des valeurs à afficher
        key_on='feature.properties.nom',  # 'nom' doit correspondre à une propriété du GeoJSON
        fill_color='YlGnBu',
        fill_opacity=0.7,
        line_opacity=0.2,
        highlight=True,
        legend_name='Prix moyen appartement (€ / m²)'
    ).add_to(m)

    # Ajouter la couche Choropleth pour le prix moyen des maisons
    folium.Choropleth(
        geo_data=gdf,
        name='Prix moyen maison',
        data=gdf,
        columns=['nom', 'Prix moyen maison'],  # 'nom' est la clé et 'Prix moyen maison' est la colonne des valeurs à afficher
        key_on='feature.properties.nom',  # 'nom' doit correspondre à une propriété du GeoJSON
        fill_color='BuGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        highlight=True,
        legend_name='Prix moyen maison (€ / m²)'
    ).add_to(m)

    # Fonction pour créer des popups
    def style_function(x):
        return {
            'fillColor': '#ffffff',
            'color': '#000000',
            'fillOpacity': 0.1,
            'weight': 0.1
        }

    def highlight_function(x):
        return {
            'fillColor': '#000000',
            'color': '#000000',
            'fillOpacity': 0.50,
            'weight': 0.1
        }

    folium.GeoJson(
        gdf,
        style_function=style_function,
        highlight_function=highlight_function,
        tooltip=folium.features.GeoJsonTooltip(
            fields=['nom'],
            aliases=['Région'],
            localize=True
        ),
        popup=folium.features.GeoJsonPopup(
            fields=['nom', 'Prix moyen appartement', 'Prix moyen maison'],
            aliases=['Région', 'Prix moyen appartement (€ / m²)', 'Prix moyen maison (€ / m²)'],
            localize=True
        ),
        zoom_on_click=True,
        name='Infos'
    ).add_to(m)

    # Ajouter la couche de contrôle des couches
    folium.LayerControl().add_to(m)

    # Afficher la carte dans Streamlit avec une taille personnalisée
    folium_static(m, width=1000, height=600)

    """
    Map Régions de France ################################################################################################################
    """

    # Affichage du nom de la région
    region = st.selectbox('Sélectionnez une région', data['Région'].unique())

    region_data = data[data['Région'] == region].iloc[0]

    st.divider()

    st.write(f"#### Prix immobilier à :blue[_{region}_] 🗾")

    # Affichage des prix 
    col1, col2 = st.columns(2)

    with col1:
        st.write("#### 🏢 :blue[Appartement]")
        st.write("Prix m2 moyen")
        with st.container():
            annotated_text(
                " ",
                annotation(f"""{region_data["Prix m2 moyen appartement"]}""", "€", "#faf", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )

    with col2:
        st.write("#### 🏠 :blue[Maison]")
        st.write(f"Prix m2 moyen")
        with st.container():
            annotated_text(
                " ",
                annotation(f"""{region_data["Prix m2 moyen maison"]}""", "€", "#faf", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    
    st.divider()

    st.write(f"#### Informations sur :blue[_{region}_] 🗾")

    #Affichage du nombre de population et communes 
    colA, colB, colC = st.columns(3)

    with colA:
        with st.container(border=True):
            annotated_text(
                "🌍 Population: ",
                annotation(f"""{region_data["Nombre d'habitants"]}""", "habitants", "#afa", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    
    with colB:
        with st.container(border=True):
            annotated_text(
                "🏞️ Départements: ",
                annotation(f"""{region_data["Nombre de départements"]}""", "Dprts", "#fea", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )

    with colC:
        with st.container(border=True):
            annotated_text(
                "🏙️ Communes: ",
                annotation(f"""{region_data["Nombre de communes"]}""", "Cmnes", "#8ef", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    
    st.divider()

    # Tableau des départements de la région
    st.write(f"#### Liste des départements de :blue[_{region}_] 🗾")
    departments = region_data['Noms des départements'].split(',')
    df = pd.DataFrame(departments, columns=['Départements'])
    st.table(df)