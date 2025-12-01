import streamlit as st

st.set_page_config(page_title="Tip Calculator", page_icon="💰")

st.title("💰 Tip Calculator – Day 16 of 100 Days of Python")
st.write("Easily calculate the tip and total bill per person.")

# Inputs
bill = st.number_input("Enter Total Bill Amount (Rs):", min_value=0.0, format="%.2f")
tip_percentage = st.slider("Select Tip Percentage (%):", 0, 50, 10)
people = st.number_input("Number of People Sharing the Bill:", min_value=1, step=1)

# Calculate Button
if st.button("Calculate Tip"):
    tip_amount = bill * (tip_percentage / 100)
    total_amount = bill + tip_amount
    amount_per_person = total_amount / people

    st.subheader("📊 Results")
    st.write(f"**Tip Amount:** Rs {tip_amount:.2f}")
    st.write(f"**Total Bill (with Tip):** Rs {total_amount:.2f}")
    st.write(f"**Amount Per Person:** Rs {amount_per_person:.2f}")

else:
    st.info("Enter the bill details and click **Calculate Tip**.")
