import streamlit as st
from utils.utils import *

st.title(":blue[Punto]4️⃣ - Pagina di Inserimento Corsi")

if check_connection():
    if __name__ == "__main__":
        st.title("🧑‍🏫 Inserisci un nuovo corso")
    
    with st.form("form"):
        #serve il CodC (formato con CT e 3 cifre), Nome, Tipo, Livello (tra 1 e 4)
        CodC = st.text_input("Inserire il Codice (Deve iniziare per 'CT' ed essere seguito da 3 cifre)")
        Nome = st.text_input("Inserire il nome del corso")
        tipo = st.text_input("Inserire il tipo del corso")
        livello = st.number_input("Inserisci un livello compreso tra 1 e 4: ", min_value=1, max_value=4)

        submitted = st.form_submit_button("Inserisci corso")

    if submitted:
        if len(CodC) != 5 or CodC[0].upper() != "C" or CodC[1].upper() != "T" or not CodC[2:4].isnumeric():
            st.error("Stai provando ad inserire un :red[Codice] nel formato errato!", icon="❌")
        else:
            veroCodC = ""
            veroCodC += CodC[0:2].upper() + CodC[2:5]
            tipo = tipo.capitalize()

            query = "INSERT INTO corsi(CodC, Nome, Tipo, Livello)" \
            " VALUES ('" + veroCodC + "', '"+ Nome + "', '"+ tipo + "', '"+ str(livello) +"')"
            data = execute_query(st.session_state["connection"],query)

            st.success("Il nuovo corso è stato inserito con successo!", icon="✅")    


else:
    st.error(":red[Connettiti al DB] prima di poter utilizzare questa funzionalità!")