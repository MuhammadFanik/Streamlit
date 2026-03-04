import streamlit as st

# A form that captures a daily log

st.title("Interactive Personal Journal")
st.divider()

# Inputs
entry_title = st.text_input("What is your entry title?")
mood_color = st.color_picker("Which color is on your mood?")
user_date = st.date_input("Please enter today's date")
content = st.text_area("Write your journal here")
hours_slept = st.number_input("How many hours did you sleep?", min_value=0, max_value=24, step=1, value=8)

# Logic
save_data = st.button("Save entry")

if save_data and entry_title:
    st.write(f"Entry title: {entry_title}")
    st.write(f"Mood Color: {mood_color}")
    st.write(f"User date: {user_date}")
    st.write(f"Journal Content: {content}")
    st.write(f"Number of hours slept: {hours_slept}")