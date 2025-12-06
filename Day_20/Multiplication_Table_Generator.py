import streamlit as st

# MUST be the first Streamlit command
st.set_page_config(page_title="Multiplication Table Generator", page_icon="📘")

st.title("📘 Multiplication Table Generator – Day 20 of 100 Days of Python")
st.write("Enter a number to generate its multiplication table.")

# Input
number = st.number_input("Enter a number:", min_value=1, step=1)

limit = st.slider("Select table range:", min_value=5, max_value=50, value=10)

# Button
if st.button("Generate Table"):
    st.subheader(f"📊 Multiplication Table of {int(number)}")
    
    # Generate Table
    for i in range(1, limit + 1):
        st.write(f"{int(number)} × {i} = {int(number) * i}")
else:
    st.info("Enter a number and click 'Generate Table'.")
