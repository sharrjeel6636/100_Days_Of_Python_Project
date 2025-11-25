import streamlit as st

st.set_page_config(page_title="Simple Interest Calculator", page_icon="💰")

st.title("💰 Simple Interest Calculator – Day 10 of 100 Days of Python")
st.write("Calculate Simple Interest using Principal, Rate, and Time.")

# Inputs
principal = st.number_input("Enter Principal Amount (P):", min_value=0.0, format="%.2f")
rate = st.number_input("Enter Rate of Interest (R %):", min_value=0.0, format="%.2f")
time = st.number_input("Enter Time (T in years):", min_value=0.0, format="%.2f")

# Calculation
def calculate_simple_interest(P, R, T):
    return (P * R * T) / 100

if st.button("Calculate Interest"):
    interest = calculate_simple_interest(principal, rate, time)
    total_amount = principal + interest

    st.subheader("📊 Results")
    st.write(f"**Simple Interest:** {interest:.2f}")
    st.write(f"**Total Amount (P + I):** {total_amount:.2f}")
else:
    st.info("Enter values and click **Calculate Interest**.")
