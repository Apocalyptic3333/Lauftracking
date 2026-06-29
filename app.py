import streamlit as st
import pandas as pd
import os
import plotly.express as px

# Archiv-Datei Pfad
DB_FILE = "lauf_archiv.csv"

# Lädt das Archiv
def load_data():
    if os.path.exists(DB_FILE): return pd.read_csv(DB_FILE)
    return pd.DataFrame()

st.set_page_config(layout="wide")
st.title("RunAnalysis: KI-Dashboard")

# 1. Screenshot-Upload (KI-Simulations-Schnittstelle)
uploaded_file = st.file_uploader("Screenshot hochladen", type=["jpg", "png"])
if uploaded_file:
    # Hier würde der KI-Vision Teil laufen
    st.success("Screenshot analysiert! Daten extrahiert.")
    # Platzhalter für extrahierte Daten
    new_data = {"Datum": pd.Timestamp.now(), "Distanz": 9.11, "Puls": 166, "Pace": 5.45}
    df = pd.concat([load_data(), pd.DataFrame([new_data])])
    df.to_csv(DB_FILE, index=False)

# 2. UI im Excel-Stil
df = load_data()
if not df.empty:
    c1, c2, c3 = st.columns(3)
    c1.metric("Distanz", f"{df['Distanz'].iloc[-1]} km")
    c2.metric("Puls", f"{df['Puls'].iloc[-1]} bpm")
    c3.metric("Pace", f"{df['Pace'].iloc[-1]} min/km")
    
    st.subheader("Leistungsverlauf")
    fig = px.line(df, x="Datum", y="Puls", markers=True)
    st.plotly_chart(fig)