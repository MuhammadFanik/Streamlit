import streamlit as st

x = st.slider("x")
st.write(f"{x} squared is {x**2}")