import streamlit as st

st.set_page_config(page_title="Student Grading System", page_icon="📘")

st.title("📘 Student Grading System – Day 18 of 100 Days of Python")
st.write("Enter the student's marks to calculate the grade.")

# Input
marks = st.number_input("Enter Marks (0 - 100):", min_value=0, max_value=100)

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Button
if st.button("Calculate Grade"):
    grade = calculate_grade(marks)
    st.subheader("🎓 Result")
    st.write(f"**Marks:** {marks}")
    st.write(f"**Grade:** {grade}")

    # Feedback Message
    if grade == "A+":
        st.success("🔥 Outstanding Performance!")
    elif grade in ["A", "B"]:
        st.info("👍 Good Job! Keep improving.")
    elif grade == "C":
        st.warning("⚠️ You passed, but there's room to improve.")
    elif grade == "D":
        st.error("❗ Below Average. Work harder!")
    else:
        st.error("❌ Fail – Keep studying, you can do better!")
else:
    st.info("Enter marks and click **Calculate Grade**.")
