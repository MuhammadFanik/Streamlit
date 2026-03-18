import streamlit as st

# Main heading at the top of the page
st.title("Tea Maker App")

# Renders a clickable button. It returns True only on the exact rerun triggered by the click
if st.button("Make tea"):
    st.success("Your tea is being brewed")

# A toggle that returns True or False
add_masala = st.checkbox("Add masala")
# This conditional block only writes a message when add_masala is checked
if add_masala:
    st.write("Masala added to your tea")

# Radio options - the selected value is stored in tea_type
tea_type = st.radio("Select your tea base: ", ["Milk", "Water", "Milk powder", "Almond milk", "Goat milk"])
st.write(f"Selected base is {tea_type}")

# The selected value goes into flavours
flavours = st.selectbox("Choose flavor: ", ["Ginger", "Kashmiri", "Simple", "Cardamom", "Vanilla Latte"])
st.write(f"Selected flavor is {flavours}")

# The result of this slider is stored in the variable "sugar"
sugar = st.slider("Sugar quantity:", min_value=0, max_value=5, value=2)

cups = st.number_input("Enter the number of cups you want to order", min_value=1, max_value=10, value=1, step=1)
st.write(f"you selected {cups} cups for the order")

name = st.text_input("Enter customer's name:")
if name:
    st.write(f"Welcome {name}. Your tea is being prepared")

dob = st.date_input("Enter your DOB:")
st.write("Your DOB is", dob)