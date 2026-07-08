import streamlit as st
from pathlib import Path

st.title("Debug")

BASE = Path(__file__).resolve().parent

st.write("Current folder:", BASE)

st.write("Files here:")
st.write(list(BASE.iterdir()))

st.write("Data folder exists:", (BASE / "data").exists())

if (BASE / "data").exists():
    st.write("Data files:")
    st.write(list((BASE / "data").iterdir()))
