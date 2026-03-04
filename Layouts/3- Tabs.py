import streamlit as st

tab1, tab2 = st.tabs(["Chart", "Data"])

with tab1:
    st.line_chart([10, 20, 30])

with tab2:
    st.write("Here is the raw data table")