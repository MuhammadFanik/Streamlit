import streamlit as st

# Q --> Display the text "Welcome to Streamlit!" as a title, followed by a subtitle saying "A beginner's guide" as a subheader.
st.title("Welcome to streamlit")
st.subheader("A beginners guide")
st.divider()

# Q --> Show the following dictionary as formatted JSON on the page
st.subheader("Working with JSON")
st.json({"name": "Alice", "age": 25, "city": "NYC"})
st.divider()

# Q --> Display a metric showing Total Sales with a value of $5,200 and a delta of +12%.
st.subheader("Working with metric")
st.metric(label="Total Sales", value="$5,200", delta="+12%")
st.divider()

# Q --> Create a line chart from this data:
st.subheader("Line Charts")
st.line_chart({"Jan": 10, "Feb": 25, "Mar": 15, "Apr": 40})
st.divider()

# Q --> Show a checkbox that says "Show secret message", and only display the message "You found it!" when it's checked.
st.subheader("Checkboxes")
check = st.checkbox(label="Show Secret message")
if check:
    st.write("You found it!")
st.divider()

# Q --> Build a form where the user enters their name and age, and on submit, display "Hello [name], you are [age] years old!".
name = st.text_input(label="Enter your name", max_chars=70)
age = st.number_input(label="Enter your age")
submit = st.button(label="Submit")
if submit:
    st.write(f"Hello {name}, you are {age} years old")
st.divider()

# Q --> Display a DataFrame of 5 students with columns Name, Grade, and Score, and make it editable using the appropriate Streamlit function.
st.data_editor(data={
    "Name": ["Ali", "Umar", "Usman", "Sam", "Simon"],
    "Grade": ["B", "A", "B", "C", "F"],
    "Score": [75, 87, 77, 62, 35]
})
st.divider()

# Q --> Create a file uploader that accepts only CSVs, and once uploaded, reads and displays the file as a DataFrame.
file_upload = st.file_uploader(label="Upload a CSV File", type="csv")
st.dataframe(file_upload)