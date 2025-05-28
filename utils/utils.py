import streamlit as st
from sqlalchemy import create_engine, text
from datetime import datetime, time, timedelta

def connect_db(dialect,username,password,host,dbname):
    try:
        engine=create_engine(f'{dialect}://{username}:{password}@{host}/{dbname}')
        conn=engine.connect()
        return conn
    except:
        return False

def execute_query(conn,query):
    return conn.execute(text(query))


def check_connection():
    if "connection" not in st.session_state.keys():
        st.session_state["connection"]=False

    if st.sidebar.button("Connettiti al Database"):
        myconnection=connect_db(dialect="mysql+pymysql",username="root",password="",host="localhost",dbname="palestra")
        if myconnection is not False:
            st.session_state["connection"]=myconnection

        else:
            st.session_state["connection"]=False
            st.sidebar.error("Errore nella connessione al DB")

    if st.session_state["connection"]:
        st.sidebar.success("Connesso al DB")
        return True
    

# Definizione delle fasce orarie (ogni 5 minuti dalle 8:00 alle 20:00)
def generate_time_slots():
    time_slots = []
    start_time = time(8, 0)
    end_time = time(20, 0)
    delta = timedelta(minutes=5)
    
    current_time = datetime.combine(datetime.today(), start_time)
    end_datetime = datetime.combine(datetime.today(), end_time)
    
    while current_time <= end_datetime:
        time_slots.append(current_time.time())
        current_time += delta
    return time_slots

# Funzione per contare i corsi in un giorno specifico
def count_courses_per_slot(day_df, time_slots):
    count_per_slot = []
    for slot in time_slots:
        slot_start = datetime.combine(datetime.today(), slot)
        slot_end = slot_start + timedelta(minutes=5)
        count = 0
        for _, row in day_df.iterrows():
            course_start = datetime.combine(datetime.today(), row["OraInizio"])
            course_end = course_start + timedelta(minutes=row["Durata_min"])
            if course_start < slot_end and course_end > slot_start:
                count += 1
        count_per_slot.append(count)
    return count_per_slot