import streamlit as st
import random
import string

# Page Config
st.set_page_config(page_title="Password Generator", page_icon="🔐")

st.title("🔐 Basic Password Generator – Day 22 of 100 Days of Python")
st.write("Generate a random secure password by selecting your preferred options.")

# Options
length = st.slider("🔢 Select Password Length:", min_value=4, max_value=32, value=12)
include_letters = st.checkbox("Include Letters (A-Z, a-z)", value=True)
include_numbers = st.checkbox("Include Numbers (0-9)", value=True)
include_symbols = st.checkbox("Include Symbols (!@#$%&*)", value=True)

# Password generation function
def generate_password(length, letters, numbers, symbols):
    characters = ""
    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += "!@#$%^&*()?"

    if characters == "":
        return "❌ Select at least one option!"

    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Generate Button
if st.button("Generate Password"):
    password = generate_password(length, include_letters, include_numbers, include_symbols)
    st.success(f"🔑 Your Password: **{password}**")

else:
    st.info("Select options and click **Generate Password**.")
