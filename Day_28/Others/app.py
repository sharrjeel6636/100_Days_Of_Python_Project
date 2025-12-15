import streamlit as st
import os
import shutil

# Page config (must be first)
st.set_page_config(page_title="File Organizer", page_icon="🗂️")

st.title("🗂️ File Organizer – Day 28 of 100 Days of Python")
st.write("Organize your files automatically by file type.")

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}

# Input folder
folder_path = st.text_input(
    "📁 Enter Folder Path",
    placeholder="e.g. C:/Users/Alpha-tech/Downloads"
)

def organize_files(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                target = os.path.join(folder_path, folder)
                os.makedirs(target, exist_ok=True)
                shutil.move(file_path, os.path.join(target, file))
                moved = True
                break

        if not moved:
            others = os.path.join(folder_path, "Others")
            os.makedirs(others, exist_ok=True)
            shutil.move(file_path, os.path.join(others, file))

# Button
if st.button("🚀 Organize Files"):
    if not folder_path:
        st.error("Please enter a valid folder path!")
    elif not os.path.exists(folder_path):
        st.error("Folder does not exist!")
    else:
        organize_files(folder_path)
        st.success("✅ Files organized successfully!")

st.info("⚠️ Make sure the folder path is correct and accessible.")
