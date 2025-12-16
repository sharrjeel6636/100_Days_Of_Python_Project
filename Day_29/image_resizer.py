import streamlit as st
from PIL import Image
from io import BytesIO

# Page config (must be first)
st.set_page_config(page_title="Image Resizer", page_icon="🖼️")

st.title("🖼️ Image Resizer – Day 29 of 100 Days of Python")
st.write("Upload an image and resize it easily.")

# Upload image
uploaded_image = st.file_uploader(
    "📤 Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image:
    image = Image.open(uploaded_image)
    st.subheader("Original Image")
    st.image(image, use_column_width=True)

    width, height = image.size

    st.subheader("Resize Settings")
    new_width = st.number_input("New Width (px)", min_value=1, value=width)
    new_height = st.number_input("New Height (px)", min_value=1, value=height)

    if st.button("🔄 Resize Image"):
        resized_image = image.resize((new_width, new_height))
        st.subheader("Resized Image")
        st.image(resized_image, use_column_width=True)

        # Save image to buffer
        buffer = BytesIO()
        resized_image.save(buffer, format="PNG")
        buffer.seek(0)

        st.download_button(
            label="📥 Download Resized Image",
            data=buffer,
            file_name="resized_image.png",
            mime="image/png"
        )
else:
    st.info("Upload an image to get started.")
