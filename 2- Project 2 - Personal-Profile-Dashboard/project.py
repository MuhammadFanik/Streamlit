import streamlit as st

st.title("Portfolio for M. Fanik")
st.header("Junior Data Scientist!")

st.image("https://images.pexels.com/photos/7069406/pexels-photo-7069406.jpeg", caption="Suzuki motorbike", width=250)

st.subheader("My introduction")
st.markdown("Hi, My name is **Muhammad Fanik** and I am a final year student in a not so good university.")
st.divider(width=250)

st.subheader("Skills")
st.badge("Python", icon="🔥", color="red", help="Python is 7/10 for me")
st.badge("SQL", icon="🔥", color="red")
st.badge("Machine Learning", icon="🔥", color="red")
st.badge("Stats and Probability", icon="🔥", color="red")
st.badge("Calculus", icon="🔥", color="red")
st.badge("Linear Algebra", icon="🔥", color="red")
st.badge("Pandas and Numpy", icon="🔥", color="red")
st.badge("Matplotlib and Seaborn", icon="🔥", color="red")

st.divider()

st.subheader("Contact Me")
st.link_button("LinkedIn", url="https://www.linkedin.com/in/muhammad-fanik/", help="Linkedin profile")