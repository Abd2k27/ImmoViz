import streamlit as st
import pandas as pd
from annotated_text import annotated_text, annotation
import os

def load_data():
    try:
        # Charger les données des régions avec un encodage spécifique
        data = pd.read_excel('./Data/Villes/infoVilles.xlsx')
        return data
    except pd.errors.ParserError as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        return None

def show():
    st.title(":blue[Données des Villes]")

    data = load_data()

    if data is None:
        st.write("Les données n'ont pas pu être chargées.")
        return
    # Affichage du nom de la ville
    ville = st.selectbox('Sélectionnez une Ville', data['Ville'].unique(), key='selectbox_dep')

    ville_data = data[data['Ville'] == ville].iloc[0]

    # Afficher l'image correspondante à la ville sélectionnée
    image_path = f"./Data/Villes/Image/{ville}_1.png"

    if os.path.exists(image_path):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image_path, caption=f"Image de {ville}", width=1000, use_column_width=True)

    else:
        st.write(f"Image pour {ville} non trouvée.")
    
    st.divider()

    # Affichage des prix relatifs au marché de l'immobilier
    st.write(f"#### Le marché immobilier à :blue[_{ville}_] 🗾")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        col1, col2 = st.columns(2)

    with col1:
        st.write("#### 🏢 :blue[Appartement]")
        st.write("Prix m2 moyen")
        with st.container():
            annotated_text(
                " ",
                annotation(f"""{ville_data["Prix m2 moyenappartement"]}""", "€", "#faf", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
        st.write("Loyer m2 moyen")
        with st.container():
            annotated_text(
                " ",
                annotation(f"""{ville_data["Loyer m2 moyenappartement"]}""", "€", "#faf", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )

    with col2:
        st.write("#### 🏠 :blue[Maison]")
        st.write(f"Prix m2 moyen")
        with st.container():
            annotated_text(
                " ",
                annotation(f"""{ville_data["Prix m2 moyenmaison"]}""", "€", "#faf", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
        st.write(f"Loyer m2 moyen")
        with st.container():
            annotated_text(
                " ",
                annotation(f"""{ville_data["Loyer m2 moyenmaison"]}""", "€", "#faf", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    
    st.divider()

    st.write("\n")

    # Affichage des Statistiques liées à la ville
    st.write(f"#### Statistique sur la population de :blue[_{ville}_] 🗾")
    st.write("\n")
    st.write("\n")

    colA, colB, colC, colD = st.columns(4)

    with colA:
        with st.container(border=True):
            annotated_text(
                "🌍 Population:",
                annotation(f"""{ville_data["Démographie"]}""", "habitants", "#afa", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    
    with colB:
        with st.container(border=True):
            annotated_text(
                "🎂 Âge moyen:",
                annotation(f"""{ville_data["Age moyen"]}""", "ans", "#fea", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )

    with colC:
        with st.container(border=True):
            annotated_text(
                "🎓 Chômage:",
                annotation(f"""{ville_data["Taux de chômage"]}""", "%", "#8ef", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    
    with colD:
        with st.container(border=True):
            annotated_text(
                "💶 Revenu moyen:",
                annotation(f"""{ville_data["Revenu moyen €/an"]}""", "€/an", "#afa", border="2px dashed purple", font_family="Comic Sans MS", font_size="24px"),
            )
    
    st.write("\n")
    st.write("\n")

    # Afficher l'image correspondante à la ville sélectionnée
    image_path = f"./Data/Villes/Image/{ville}.png"
    
    if os.path.exists(image_path):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image_path, caption=f"Statistique de {ville}", use_column_width=True)

    else:
        st.write(f"Image pour {ville} non trouvée.")
    
    st.write("\n")
    with st.container():
        annotated_text(
            "ℹ️ Bon à savoir :",
            annotation(f"""{ville_data["Bon à savoir"]}""", "", "#ffe312", font_family="Comic Sans MS", font_size="14px"),
        )
    with st.container():
        annotated_text(
            "",
            annotation(f"""{ville_data["Sources"]}""", font_family="Comic Sans MS", font_size="14px"),
        )

    st.divider()

    st.write("\n")

    # Affichage les services et équipements liées à la ville
    st.write(f"#### Services et équipements à :blue[_{ville}_] 🗾")

    colA, colB, colC, colD = st.columns(4)

    with colA:
        with st.container(border=True):
            st.write(f"###### Commerce 🛍️")
            annotated_text(
                "🥖 Boulangerie: ",
                annotation(f"""{ville_data["Boulangerie"]}""", border="2px dashed purple", font_family="Comic Sans MS", font_size="16px"),
            )
            annotated_text(
                "⛽️ Station: ",
                annotation(f"""{ville_data["Station-service"]}""", border="2px dashed purple", font_family="Comic Sans MS", font_size="16px"),
            )
            annotated_text(
                "🛒 Supermarché: ",
                annotation(f"""{ville_data["Supermarché"]}""", border="2px dashed purple", font_family="Comic Sans MS", font_size="16px"),
            )
            annotated_text(
                "👩‍🍳 Restaurant: ",
                annotation(f"""{ville_data["Restaurant"]}""", border="2px dashed purple", font_family="Comic Sans MS", font_size="16px"),
            )
    
    with colB:
        with st.container(border=True):
            st.write(f"###### Santé 🏥")
            annotated_text(
                "👨‍⚕️ Médecin: ",
                annotation(f"""{ville_data["Médecin"]}""", border="2px dashed purple", font_family="Comic Sans MS", font_size="16px"),
            )
            annotated_text(
                "💊 Pharmacie: ",
                annotation(f"""{ville_data["Pharmacie"]}""", border="2px dashed purple", font_family="Comic Sans MS", font_size="16px"),
            )

    with colC:
        with st.container(border=True):
            st.write(f"###### Éducation 🎓")
            annotated_text(
                "🏫 Primaire: ",
                annotation(f"""{ville_data["Primaire"]}""", border="2px dashed purple", font_family="Comic Sans MS", font_size="16px"),
            )
            annotated_text(
                "🏫 Collège: ",
                annotation(f"""{ville_data["Collège"]}""", border="2px dashed purple", font_family="Comic Sans MS", font_size="16px"),
            )
            annotated_text(
                "🏫 Lycée: ",
                annotation(f"""{ville_data["Lycée"]}""", border="2px dashed purple", font_family="Comic Sans MS", font_size="16px"),
            )
    
    with colD:
        with st.container(border=True):
            st.write(f"###### Mairie 🏢")
            annotated_text(
                "📍 Adresse Mairie: ",
                annotation(f"""{ville_data["Adresse Mairie"]}""", border="2px dashed purple", font_family="Comic Sans MS", font_size="16px"),
            )
            annotated_text(
                "🤵‍♂️ Maire: ",
                annotation(f"""{ville_data["Maire"]}""", border="2px dashed purple", font_family="Comic Sans MS", font_size="16px"),
            )