import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "First Col": ["Mercedes", "Toyota", "Suzuki", "Maserati", "Audi", "Volvo"],
    "Second Col": [8, 7.5, 6, 9.9, 8.5, 9]
})

st.title("This is our first attempt to make a streamlit app with dataframes")
st.table(df)


# Let's create a dataframe and change its formatting
df1 = np.random.randn(5, 7)
st.dataframe(df1)