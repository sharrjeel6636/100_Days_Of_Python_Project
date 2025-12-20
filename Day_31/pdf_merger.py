import streamlit as st
from pypdf import PdfWriter, PdfReader
from io import BytesIO

# Page config (must be first)
st.set_page_config(page_title="PDF Merger", page_icon="📄")

st.title("📄 PDF Merger – Day 31 of 100 Days of Python")
st.write("Upload multiple PDF files and merge them into one.")

uploaded_files = st.file_uploader(
    "📤 Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("🔗 Merge PDFs"):
        writer = PdfWriter()

        for pdf in uploaded_files:
            reader = PdfReader(pdf)
            for page in reader.pages:
                writer.add_page(page)

        buffer = BytesIO()
        writer.write(buffer)
        buffer.seek(0)

        st.success("✅ PDFs merged successfully!")

        st.download_button(
            label="📥 Download Merged PDF",
            data=buffer,
            file_name="merged.pdf",
            mime="application/pdf"
        )
else:
    st.info("Upload at least two PDF files to merge.")
