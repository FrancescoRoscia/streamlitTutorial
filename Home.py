import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *

st.set_page_config(
    page_title="Homework 4 - Basi di Dati",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://dbdmg.polito.it/',
        'Report a bug': "https://dbdmg.polito.it/",
        'About': "# Corso di *Basi di Dati*"
    }
)

st.title("📈 :blue[Homework 4] - Basi di Dati")
st.header("Introduzione al progetto che bisogna :red[realizzare]!")
st.write("Il mio nome è **:green[Francesco Roscia]**, numero di matricola: **:green[323785]** e in questo homework" \
" ci eserciteremo per imparare ad usare Streamlit collegato ad un Database in locale!")

col1, col2 = st.columns(2)

with col1:
    st.write("Prima colonna")


with col2:
    st.write("Seconda colonna")