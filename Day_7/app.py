import random
import streamlit as st

st.set_page_config(page_title="Dice Roller", page_icon="🎲")
st.title("🎲 Dice Roller - Day 6 of 100 Days of Python")

st.write("Click the button below to roll the dice!")

# --- Dice Images ---
dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

if st.button("Roll Dice"):
    number = random.randint(1, 6)
    st.markdown(
        f"""
        <h1 style='font-size: 100px; text-align: center;'>{dice_faces[number]}</h1>
        <h3 style='text-align:center;'>You rolled: <b>{number}</b></h3>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        "<p style='text-align:center;'>Roll the dice to begin!</p>",
        unsafe_allow_html=True
    )
