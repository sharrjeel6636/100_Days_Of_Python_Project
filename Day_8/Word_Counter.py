import streamlit as st

st.set_page_config(page_title="Word Counter", page_icon="📝", layout="centered")

st.title("📝 Word Counter – Day 8 of 100 Days of Python")
st.write("Enter your text below, and the app will count words and characters.")


text = st.text_area("Enter your text here:", height=200)

# Count Function
def count_text(content):
    words = content.split()
    characters = len(content)
    return len(words), characters

# Display Results
if st.button("Count"):
    word_count, char_count = count_text(text)

    st.subheader("📊 Results")
    st.write(f"**Words:** {word_count}")
    st.write(f"**Characters:** {char_count}")
else:
    st.info("Type something and click **Count**.")

