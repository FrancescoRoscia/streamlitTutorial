import streamlit as st
from utils.utils import *
import pandas as pd
from datetime import time



st.title(":blue[Punto]5️⃣ - Pagina di Inserimento Lezione")

if check_connection():
    if __name__ == "__main__":
        st.title("🕒 Inserisci un nuova lezione")
    
    with st.form("form"):
        #campi necessari (CodFisc, Giorno, OrarioInizio, Durata, CodC, Sala)
        #CodFisc e CodC deve essere menu a tendina, Slider per OraInizio e Durata (tra 10 e 60), Giorno tra Lunedi e Venerdi
        #Inserimento valido se non ci sono altre lezioni dello stesso corso lo stesso giorno
        col1, col2 = st.columns(2)        
        with col1:
            query = "SELECT CodFisc FROM istruttore"
            data = execute_query(st.session_state["connection"],query)
            df = pd.DataFrame(data)
            CodFisc = st.selectbox("🧑Inserisci il Codice Fiscale dell'istruttore", df)
        
        with col2:
            query = "SELECT CodC FROM corsi"
            data = execute_query(st.session_state["connection"],query)
            df = pd.DataFrame(data)
            CodC = st.selectbox("🆔Inserisci il codice del corso", df)

        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            OraInizio = st.slider("🕐Inserire l'ora di inizio del corso: ", value=time(8, 0, 0), format="HH:mm:ss", 
                      min_value=time(8, 0, 0), max_value=time(20, 0, 0))
            
        with col2:
            Durata = st.slider("⏳Inserire la durata del corso: ", min_value=10, max_value=60, step=5)

        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            Giorno = st.text_input("📅Inserire il giorno della settimana (tra Lunedì e Venerdì): ")
        
        with col2:
            Sala = st.text_input("📍Inserire la sala in cui verrà svolta la lezione: ")

        submitted = st.form_submit_button("Inserisci corso")
        

    if submitted:
        Giorno = Giorno.capitalize()
        giorniValidi = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"]

        if Giorno not in giorniValidi:
            st.error("Stai provando ad inserire il corso in un :red[giorno non valido]!", icon="❌")

        elif len(Sala) == 0:
            st.error("Non hai inserito una :red[sala]!", icon="❌")
        
        elif not(Sala[0].isalpha() and Sala[1:].isnumeric()):
            st.error("Stai provando ad inserire il corso in una :red[sala non valida]!", icon="❌")
        
        else:
            query = "SELECT COUNT(*) as N FROM programma WHERE Giorno ='"+Giorno+"' AND CodC = '"+CodC+"'"
            data = execute_query(st.session_state["connection"],query)
            df = pd.DataFrame(data)
            count = df.at[0, "N"]
            if count > 0:
                st.error("Stai provando ad inserire il corso :red[nello stesso giorno] in cui c'è un'altra lezione!", icon="❌")
            else:
                Sala = Sala.capitalize()
                query = "INSERT INTO programma(CodFisc, Giorno, OraInizio, Durata, Sala, CodC)" \
                " VALUES ('"+CodFisc+"', '"+ Giorno + "', '" + str(OraInizio) + "', '"+str(Durata)+ "', '"+ Sala+"', '" + CodC + "')"
                data = execute_query(st.session_state["connection"],query)
                st.success("La nuova lezione è stato inserita con successo!", icon="✅")    


else:
    st.error(":red[Connettiti al DB] prima di poter utilizzare questa funzionalità!")