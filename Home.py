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
        query = "SELECT Giorno, OraInizio, Durata FROM programma"
        data = execute_query(st.session_state["connection"],query)
        
        df = pd.DataFrame(data)

        # Converti le colonne temporali
        df["OraInizio"] = pd.to_datetime(df["OraInizio"]).dt.time
        df["Durata_min"] = df["Durata"]

        time_slots = generate_time_slots()

        # Creazione delle tab per ogni giorno
        giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"]
        tabs = st.tabs(giorni_settimana)

        for i, giorno in enumerate(giorni_settimana):
            with tabs[i]:
                # Filtra i dati per il giorno corrente
                day_df = df[df["Giorno"] == giorno]
                
                if not day_df.empty:
                    # Calcola i corsi per fascia oraria
                    count_per_slot = count_courses_per_slot(day_df, time_slots)
                    
                    # Crea il DataFrame per il grafico
                    chart_data = pd.DataFrame({
                        "Fascia Oraria": [t.strftime("%H:%M") for t in time_slots],
                        "Corsi Attivi": count_per_slot,
                    })
                    
                    # Mostra il grafico
                    st.subheader(f"Corsi attivi - {giorno}")
                    st.area_chart(chart_data.set_index("Fascia Oraria"))
                else:
                    st.write(f"Nessun corso programmato per {giorno}")

    else:
        st.write(":red[Connettiti al DB] prima di poter visualizzare il grafico!")


with col2:
    if st.session_state["connection"]:
        st.write("**Bar Chart** con numero di lezioni per ogni giorno della settimana")
        query2 = "SELECT Giorno, COUNT(*) AS numLezioni FROM programma GROUP BY Giorno"
        data2 = execute_query(st.session_state["connection"],query2)
        st.bar_chart(data = data2, x="Giorno", y = "numLezioni")
    else:
        st.write(":red[Connettiti al DB] prima di poter visualizzare il grafico!")