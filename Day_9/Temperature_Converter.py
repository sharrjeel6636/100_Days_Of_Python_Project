import streamlit as st

st.set_page_config(page_title="Temperature Converter", page_icon="🌡️")

st.title("🌡️ Temperature Converter")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin.")

# Input temperature value
value = st.number_input("Enter Temperature", format="%.2f")

# Select Input Unit
input_unit = st.selectbox("From Unit", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])

# Select Output Unit
output_unit = st.selectbox("To Unit", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])

# Conversion functions
def to_celsius(val, unit):
    if unit == "Celsius (°C)":
        return val
    elif unit == "Fahrenheit (°F)":
        return (val - 32) * 5/9
    elif unit == "Kelvin (K)":
        return val - 273.15

def from_celsius(val, unit):
    if unit == "Celsius (°C)":
        return val
    elif unit == "Fahrenheit (°F)":
        return (val * 9/5) + 32
    elif unit == "Kelvin (K)":
        return val + 273.15

if st.button("Convert"):
    celsius_value = to_celsius(value, input_unit)
    final_value = from_celsius(celsius_value, output_unit)

    st.success(f"Converted Temperature: **{final_value:.2f}**")

    # Extra Info
    st.info(
        f"📌 **{value} {input_unit} = {final_value:.2f} {output_unit}**"
    )
