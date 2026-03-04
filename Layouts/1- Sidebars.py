import streamlit as st
from click import option

# This goes in the main center area
st.title("Main Dashboard")

# This goes in the sidebar in the left - Add a selectbox and a radio button
add_selectbox = st.sidebar.selectbox("How would you be like to contacted?", options=["Email", "LinkedIn", "Phone number"])
add_radio = st.sidebar.radio("Choose a shipping method", options=["Standard", "Urgent"])

if add_radio:
    st.write(f"You selected {add_radio} shipping method")