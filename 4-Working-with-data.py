import streamlit as st
import pandas as pd

st.title("Tea Sales Dashboard")

file = st.file_uploader("Upload your CSV file", type=["csv"])
df = pd.read_csv(file)

if file:
    st.subheader("Data Preview")
    st.dataframe(df.head())

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())