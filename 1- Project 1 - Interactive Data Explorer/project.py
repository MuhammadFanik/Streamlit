import streamlit as st
import pandas as pd

st.title("Interactive Data Explorer")
st.divider()

# Doesn't return a dataframe, it returns a file-like object. To turn those bytes into a table, you need to pass that object
# into a library like pandas. Also, since Streamlit runs from top to bottom, you need to check if a file has actually been
# uploaded before trying to read it, otherwise your app will throw an error immediately.

# The uploader returns a file object
uploaded_file = st.file_uploader("Upload a CSV or an Excel file", type=["csv"])

# Check if a file was actually uploaded
if uploaded_file is not None:
    # Use pandas to read the file object
    df = pd.read_csv(uploaded_file)

    if df.empty:
        st.warning("The uploaded file is empty")
    else:
        # Display the data section
        st.header("DataFrame")
        st.dataframe(df.head())
        # Add caption
        st.caption(f"This Dataframe has {df.shape[0]} rows and {df.shape[1]} columns")

        st.divider()

        # Column Identification
        num_cols = df.select_dtypes(include=['number']).columns.tolist()
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        all_cols = df.columns.tolist()

        # Visualization Logic
        st.header("2. Interactive Visualization")

        if all_cols:
            selected_col = st.selectbox("Select a column to visualize:", all_cols)

            if selected_col in num_cols:
                st.subheader(f"Line Chart of {selected_col}")
                st.line_chart(df[selected_col])
                st.write(f"**Mean Value:** {df[selected_col].mean():.2f}")

            elif selected_col in cat_cols:
                st.subheader(f"Distribution of {selected_col}")
                # Count occurrences for categorical data
                counts = df[selected_col].value_counts()
                st.bar_chart(counts)

            st.divider()
