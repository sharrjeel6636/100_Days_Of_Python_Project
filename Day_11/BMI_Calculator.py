import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("⚖️ BMI Calculator – Day 11 of 100 Days of Python")
st.write("Enter your weight and height to calculate your Body Mass Index.")

# Inputs
weight = st.number_input("Enter your Weight (kg):", min_value=0.0, format="%.2f")
height = st.number_input("Enter your Height (meters):", min_value=0.0, format="%.2f")

# BMI Function
def calculate_bmi(weight, height):
    if height == 0:
        return None
    return weight / (height ** 2)

# Button
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    
    if bmi is None:
        st.error("Height cannot be zero!")
    else:
        st.subheader("📊 Results")
        st.write(f"**Your BMI:** {bmi:.2f}")
        
        # BMI Status (Underweight, Normal, Overweight)
        if bmi < 18.5:
            st.warning("🟡 Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("🟢 Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("🟠 Overweight")
        else:
            st.info("BMI is above the overweight range.")
else:
    st.info("Enter values and click **Calculate BMI**.")
