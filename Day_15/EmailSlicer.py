import streamlit as st

st.set_page_config(page_title="Email Slicer", page_icon="✂️")

st.title("✂️ Email Slicer – Day 15 of 100 Days of Python")
st.write("Enter an email address to extract Username and Domain.")

# Input
email = st.text_input("📧 Enter your Email Address:")

# Button
if st.button("Slice Email"):
    if "@" not in email:
        st.error("Invalid email! Please include '@' in the email address.")
    else:
        try:
            username, domain = email.split("@")
            st.subheader("📊 Results")
            st.write(f"**Username:** {username}")
            st.write(f"**Domain:** {domain}")
        except:
            st.error("Something went wrong! Please enter a valid email.")
else:
    st.info("Type your email and click **Slice Email**.")
