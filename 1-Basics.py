import streamlit as st
import pandas as pd

st.title("First Chai App")
st.subheader("Made with Streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your car brand")

car = st.selectbox("Your favorite car brand: ", ["Audi", "Mercedes", "BMW", "Suzuki", "Toyota", "Volvo"])
st.write(f"You have selected {car} as your favorite car brand.")

st.success("Your car brand has been noted down. Thanks!")