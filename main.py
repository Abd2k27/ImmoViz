import streamlit as st
from pages import homepage, departpage, villepage

st.set_page_config(layout="wide")

# Sidebar for navigation
st.sidebar.title("DAT-ImmoViz")
page = st.sidebar.radio("Go to", ["Homepage", "Departpage", "Villepage"])

# Load the selected page
if page == "Homepage":
    homepage.show()
elif page == "Departpage":
    departpage.show()
else:
    villepage.show()