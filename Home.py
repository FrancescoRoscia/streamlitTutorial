import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *
from datetime import datetime, timedelta

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

if "connection" not in st.session_state.keys():
        st.session_state["connection"]=False

check_connection()

col1, col2 = st.columns(2)

with col1:
    st.write("**Area Chart** con numero di lezioni per ogni slot di tempo")
    if st.session_state["connection"]:
        query = "SELECT OraInizio, COUNT(*) AS NumeroLezioni FROM programma GROUP BY OraInizio"
        data = execute_query(st.session_state["connection"],query)
        st.area_chart(data=data, x = "OraInizio", y = "NumeroLezioni")
    
    else:
        st.write(":red[Connettiti al DB] prima di poter visualizzare il grafico!")


with col2:
    if st.session_state["connection"]:
        st.write("**Bar Chart** con numero di lezioni per ogni giorno della settimana")
        query2 = "SELECT Giorno, COUNT(*) AS NumeroLezioni FROM programma GROUP BY Giorno"
        data2 = execute_query(st.session_state["connection"],query2)
        st.bar_chart(data = data2, x="Giorno", y = "NumeroLezioni")
    else:
        st.write(":red[Connettiti al DB] prima di poter visualizzare il grafico!")