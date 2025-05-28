import streamlit as st
from utils.utils import *
import pandas as pd

st.title(":blue[Punto]2️⃣ - Pagina di Visualizzazione e Filtraggio")

if check_connection():
    col1, col2 = st.columns(2)

    with col1:
        query = "SELECT COUNT(*) AS NumeroCorsi FROM corsi"
        data = execute_query(st.session_state["connection"],query)
        df = pd.DataFrame(data)
        st.metric("Numero Corsi", df["NumeroCorsi"])
    with col2:
        query = "SELECT COUNT(DISTINCT Tipo) AS disTipi FROM corsi"
        data = execute_query(st.session_state["connection"],query)
        df = pd.DataFrame(data)
        st.metric("Tipi Distinti Disponibili", df["disTipi"])
else:
    st.write(":red[Connettiti al DB] prima di poter visualizzare il grafico!")
