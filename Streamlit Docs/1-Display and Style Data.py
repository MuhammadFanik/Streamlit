import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})

# Magic command - Just writing the variable name
df

"x", 10


# Writing a Dataframe
st.write("Here is our first attempt at making a table using some synthetic data")
st.write(pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
}))