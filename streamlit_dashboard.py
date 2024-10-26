import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def load_data():
    return pd.read_csv('your_dataset.csv')