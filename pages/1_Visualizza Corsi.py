import streamlit as st
from utils.utils import *
import pandas as pd

st.title(":blue[Punto]2️⃣ - Pagina di Visualizzazione e Filtraggio Corsi")


if check_connection():
    if __name__ == "__main__":
        st.title("📚 Visualizzazione Corsi")

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

    
    with st.form("form"):
        query = "SELECT DISTINCT Tipo FROM corsi"
        data = execute_query(st.session_state["connection"],query)
        df = pd.DataFrame(data)
        option = st.selectbox("Inserisci un tipo di corso da voler filtrare", df)

        range = st.slider("Inserisci il range del livello di difficoltà che vuoi filtrare", 1, 4, (1, 4))

        submitted = st.form_submit_button("Filtra")
    
    if submitted:
        #visualizzare programmi corsi + nome, cognome, email istruttore
        query = "SELECT Tipo, Livello, Giorno, OraInizio, Durata, Sala, i.Nome, Cognome, Email" \
        " FROM corsi AS c, istruttore AS i, programma AS p WHERE " \
        "c.CodC = p.CodC AND p.CodFisc = i.CodFisc AND tipo = '" + option + "' AND Livello >= "+ str(range[0]) + " AND Livello <= " + str(range[1])
        data = execute_query(st.session_state["connection"],query)
        df = pd.DataFrame(data)

        if df.empty:
            st.error("Non ci sono corsi con questi parametri", icon="❌")
        else:
            st.success("La ricerca ha prodotto risultati!", icon="✅")
            st.dataframe(df)


else:
    st.error(":red[Connettiti al DB] prima di poter utilizzare questa funzionalità!")


