import streamlit as st
import datetime

st.title("Age Calculator")
dob = st.date_input("Enter your Date of Birth:", min_value=datetime.date(1900, 1, 1))

def calc_age(dob):
    dob_year = dob.year
    current_year = 2026
    return current_year - dob_year

if st.button("Calculate Age"):
    user_age = calc_age(dob)
    st.title(f"Your Age is {user_age}")
    st.success("Your Age is calculated ")