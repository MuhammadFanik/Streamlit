import streamlit as st

# Create 3 equal columns
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("Click col 1")

with col2:
    st.header("Column 2")
    st.write("Click col 2")

with col3:
    st.header("Column 3")
    st.write("Click col 3")