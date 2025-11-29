import streamlit as st
import requests

st.title("💱 Currency Converter (Day 14)")

st.write("Convert any currency to another using real-time exchange rates.")

# Fetch exchange rates from API
@st.cache_data
def get_rates(base="USD"):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)
    return response.json()

# Input Section
amount = st.number_input("Enter Amount:", min_value=0.0, value=1.0)

base_currency = st.selectbox(
    "From Currency:",
    ["USD", "EUR", "PKR", "INR", "GBP", "CAD", "AUD", "AED"]
)

target_currency = st.selectbox(
    "To Currency:",
    ["USD", "EUR", "PKR", "INR", "GBP", "CAD", "AUD", "AED"]
)

if st.button("Convert"):
    data = get_rates(base_currency)
    rates = data["rates"]

    if target_currency in rates:
        result = amount * rates[target_currency]
        st.success(f"✅ {amount} {base_currency} = {round(result, 2)} {target_currency}")
    else:
        st.error("❌ Currency not found in API!")

st.caption("Made by Shaejeel — Day 14 of 100 Days of Python 🚀")
