import streamlit as st

st.title("Layouts in Streamlit")

col1, col2 =st.columns(2)
with col1:
    st.header("Toyota")
    vote1 = st.button("Vote Toyota")
with col2:
    st.header("Honda")
    vote2 = st.button("Vote Honda")

if vote1:
    st.success("Thanks for voting Toyota")
if vote2:
    st.success("Thanks for voting Honda")