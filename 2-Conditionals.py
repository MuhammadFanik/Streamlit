import streamlit as st

st.title("Tea Maker App")

if st.button("Make tea"):
    st.success("Your tea is being brewed")

add_masala = st.checkbox("Add masala")

if add_masala:
    st.write("Masala added to your tea")

tea_type = st.radio("Select your tea base: ", ["Milk", "Water", "Milk powder", "Almond milk", "Goat milk"])
st.write(f"Selected base is {tea_type}")

flavours = st.selectbox("Choose flavor: ", ["Ginger", "Kashmiri", "Simple", "Cardamom", "Vanilla Latte"])
st.write(f"Selected flavor is {flavours}")

sugar = st.slider("Sugar quantity:", min_value=0, max_value=5, value=2)

cups = st.number_input("Enter the number of cups you want to order", min_value=1, max_value=10, value=1, step=1)
st.write(f"you selected {cups} cups for the order")

name = st.text_input("Enter customer's name:")
if name:
    st.write(f"Welcome {name}. Your tea is being prepared")

dob = st.date_input("Enter your DOB:")
st.write("Your DOB is", dob)