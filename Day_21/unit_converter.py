import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Unit Converter", page_icon="📏")

# --- TITLE ---
st.title("📏 Unit Converter – Day 21 of 100 Days of Python")
st.write("Convert units easily! Choose a category and enter your value.")

# --- Unit conversion functions ---
def length_converter(value, from_unit, to_unit):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Miles": 1609.34,
        "Yards": 0.9144,
        "Feet": 0.3048,
        "Inches": 0.0254,
    }
    return value * units[from_unit] / units[to_unit]

def weight_converter(value, from_unit, to_unit):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Milligrams": 0.000001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    return value * units[from_unit] / units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Celsius conversions
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    if from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15

    # Fahrenheit conversions
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    if from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15

    # Kelvin conversions
    if from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    if from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32


# --- CATEGORY SELECTION ---
category = st.selectbox("Select Conversion Category:", 
                        ["Length", "Weight", "Temperature"])

value = st.number_input("Enter Value:", format="%.4f")

# --- UNIT OPTIONS ---
if category == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)

elif category == "Weight":
    units = ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)

else:
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)


# --- BUTTON ---
if st.button("Convert"):
    if category == "Length":
        result = length_converter(value, from_unit, to_unit)

    elif category == "Weight":
        result = weight_converter(value, from_unit, to_unit)

    else:
        result = temperature_converter(value, from_unit, to_unit)

    st.success(f"**Converted Value:** {result:.4f}")

else:
    st.info("Enter value and click **Convert**.")
