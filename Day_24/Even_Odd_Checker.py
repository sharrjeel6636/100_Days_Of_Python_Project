import streamlit as st


st.set_page_config(page_title="Even-Odd Checker", page_icon="🔢")

st.title("🔢 Even-Odd Checker – Day 24 of 100 Days of Python")
st.write("Enter any number to check whether it is **Even** or **Odd**.")

# Input
number = st.number_input("Enter a number:", step=1, format="%d")

# Button
if st.button("Check"):
    if number % 2 == 0:
        st.success(f"✅ {int(number)} is **Even**")
    else:
        st.warning(f"⚠️ {int(number)} is **Odd**")
else:
    st.info("Enter a number and click **Check**.")
