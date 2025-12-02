import streamlit as st
import random

st.set_page_config(page_title="Random Quote Generator", page_icon="💬")

st.title("💬 Random Quote Generator – Day 17 of 100 Days of Python")
st.write("Click the button to get a random inspirational quote!")

# List of Quotes
quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
    "It always seems impossible until it's done. – Nelson Mandela",
    "Hard work beats talent when talent doesn’t work hard. – Tim Notke",
    "Dream big and dare to fail. – Norman Vaughan",
    "Don’t wait for opportunity. Create it.",
    "The future depends on what you do today. – Mahatma Gandhi",
]

# Button
if st.button("Generate Quote"):
    st.success(random.choice(quotes))
else:
    st.info("Click the button to get an inspirational quote!")
