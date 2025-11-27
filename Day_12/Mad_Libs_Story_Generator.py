import streamlit as st

st.set_page_config(page_title="Mad Libs Story Generator", page_icon="📖")

st.title("📖 Mad Libs Story Generator – Day 12 of 100 Days of Python")
st.write("Fill in the blanks below and generate a fun story!")

# Inputs
noun = st.text_input("Enter a Noun:")
place = st.text_input("Enter a Place:")
adjective = st.text_input("Enter an Adjective:")
verb = st.text_input("Enter a Verb (past tense):")
animal = st.text_input("Enter an Animal:")
emotion = st.text_input("Enter an Emotion:")

# Generate Story
if st.button("Generate Story"):
    if noun and place and adjective and verb and animal and emotion:
        story = (
            f"One day, a {adjective} {noun} went to {place}. "
            f"There, it suddenly {verb} when it saw a {animal}. "
            f"The {noun} felt very {emotion} after the unexpected adventure!"
        )

        st.subheader("📚 Your Story:")
        st.write(story)
    else:
        st.error("Please fill in all fields to generate the story!")

else:
    st.info("Enter words above and click **Generate Story**.")
