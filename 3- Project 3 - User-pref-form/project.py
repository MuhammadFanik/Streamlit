from os import write

import streamlit as st

st.header("User experience form")
st.divider()

# Inputs
full_name = st.text_input("Full Name")
age = st.number_input("Age", min_value=0, max_value=120, value=18, step=1)
favorite_color = st.color_picker("Select a color")
dob = st.date_input("Select your date of birth", min_value="1900-01-01")

# Logic
checked = st.checkbox("Show my summary")
if checked:
    st.write("Full Name", full_name)
    st.write("Age", age)
    st.write("Favorite color", favorite_color)
    st.write("Date of Birth", dob)