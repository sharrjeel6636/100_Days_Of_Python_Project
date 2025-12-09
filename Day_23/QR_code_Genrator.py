import streamlit as st
import qrcode
from io import BytesIO

# Page config
st.set_page_config(page_title="QR Code Generator", page_icon="🔳")

st.title("🔳 QR Code Generator – Day 23 of 100 Days of Python")
st.write("Enter any text or URL to instantly generate a QR Code.")

# Input
user_text = st.text_input("Enter text or URL:")

# Button
if st.button("Generate QR Code"):
    if user_text.strip() == "":
        st.error("Please enter some text!")
    else:
        # Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )
        qr.add_data(user_text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Convert image to bytes
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        st.subheader("📌 Your QR Code:")
        st.image(buffer, width=250)

        # Download button
        st.download_button(
            label="📥 Download QR Code",
            data=buffer,
            file_name="qrcode.png",
            mime="image/png"
        )
else:
    st.info("Enter text above and click **Generate QR Code**.")
