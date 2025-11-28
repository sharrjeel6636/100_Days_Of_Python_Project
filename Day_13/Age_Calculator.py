import streamlit as st
from datetime import date, datetime

st.set_page_config(page_title="Age Calculator", page_icon="🎂")

st.title("🎂 Age Calculator – Day 13 of 100 Days of Python")
st.write("Select your date of birth to calculate your exact age.")

# Input: Date of Birth
dob = st.date_input("📅 Select your Date of Birth:")

# Button
if st.button("Calculate Age"):
    today = date.today()

    # Check future dates
    if dob > today:
        st.error("Date of birth cannot be in the future!")
    else:
        # Calculate age
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        # Adjust negative values
        if days < 0:
            months -= 1
            days += 30
        if months < 0:
            years -= 1
            months += 12
        
        # Output
        st.subheader("📊 Your Age:")
        st.write(f"**{years} years, {months} months, {days} days**")
else:
    st.info("Select your birth date and click **Calculate Age**.")
