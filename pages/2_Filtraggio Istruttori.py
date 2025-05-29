import datetime
import streamlit as st
from utils.utils import *
import pandas as pd

st.title(":blue[Punto]3️⃣ - Pagina di Visualizzazione e Filtraggio Istuttori")


if check_connection():
    if __name__ == "__main__":
        st.title("🧑‍🏫 Visualizzazione Istruttori")

    #l'utente deve cercare attraverso cognome dell'istruttore e range data di nascita
    #risultato stampato su ogni riga separata. In caso di 0 risultati --> errore

    with st.form("form"):
        cognome = st.text_input("Inserire il cognome dell'istruttore: ")
        rangeDate = st.date_input("Seleziona il range della data di nascita dell'istruttore: ",
                                    value=(datetime.date(2023, 1, 1), datetime.date(2023, 1, 15)))

        submitted = st.form_submit_button("Cerca")

    if submitted:
        query = "SELECT Nome, Cognome, DataNascita, Email, Telefono FROM istruttore" \
        " WHERE Cognome LIKE  '"+ cognome + "%' AND DataNascita BETWEEN '" + str(rangeDate[0]) + "' AND '" + str(rangeDate[1]) + "'"

        data = execute_query(st.session_state["connection"],query)
        df = pd.DataFrame(data)

        if df.empty:
            st.error("Non ci sono istruttori con questi parametri", icon="❌")
        else:
            st.success("La ricerca ha prodotto risultati!", icon="✅")
            
            for _, item in df.iterrows():
                st.write("🧑 Nome: **" + item["Nome"] +" "+ item["Cognome"] + "**")
                st.write("📅 Data di Nascita: " + str(item["DataNascita"]))
                st.write("📧 Email: " + item["Email"])
                if item["Telefono"]:
                    st.write("📱 Numero di Telefono: " + item["Telefono"])
                else:
                    st.write("📱 Numero di Telefono: Non Disponibile")
                st.divider()

else:
    st.error(":red[Connettiti al DB] prima di poter utilizzare questa funzionalità!")