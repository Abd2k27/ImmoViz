import streamlit as st
from my_pages import homepage, departpage, villepage

# Configure the layout and hide the default sidebar
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Custom sidebar for navigation
st.sidebar.title("ImmoViz")
page = st.sidebar.radio("Go to", ["Homepage", "Departpage", "Villepage"])

# Load the selected page
if page == "Homepage":
    homepage.show()
elif page == "Departpage":
    departpage.show()
else:
    villepage.show()