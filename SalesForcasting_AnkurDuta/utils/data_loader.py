import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    df = pd.read_csv("data/train.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        format="mixed",
        dayfirst=True
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        format="mixed",
        dayfirst=True
    )

    return df