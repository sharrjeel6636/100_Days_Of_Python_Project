import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Set page config
st.set_page_config(page_title="Gemini Code Expense Tracker", layout="wide")

# Title of the app
st.title("Gemini Code Expense Tracker")

# Initialize session state for storing expenses
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Sidebar for adding new expenses
st.sidebar.header("Add New Expense")
expense_date = st.sidebar.date_input("Date", datetime.today())
expense_category = st.sidebar.selectbox("Category", ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Health", "Other"])
expense_amount = st.sidebar.number_input("Amount", min_value=0.0, format="%.2f")
expense_description = st.sidebar.text_input("Description (Optional)")

if st.sidebar.button("Add Expense"):
    new_expense = {
        "Date": expense_date,
        "Category": expense_category,
        "Amount": expense_amount,
        "Description": expense_description
    }
    st.session_state.expenses.append(new_expense)
    st.sidebar.success("Expense added successfully!")

# Display expenses
st.header("Expenses")
if st.session_state.expenses:
    expenses_df = pd.DataFrame(st.session_state.expenses)
    expenses_df = expenses_df.sort_values(by="Date", ascending=False)
    st.dataframe(expenses_df)

    # Total expenses
    total_expenses = expenses_df["Amount"].sum()
    st.header(f"Total Expenses: ${total_expenses:,.2f}")

    # Category-wise summary
    st.header("Category-wise Summary")
    category_summary = expenses_df.groupby("Category")["Amount"].sum().reset_index()
    st.dataframe(category_summary)

    # Pie chart for expense visualization
    st.header("Expense Distribution")
    fig, ax = plt.subplots()
    ax.pie(category_summary["Amount"], labels=category_summary["Category"], autopct="%1.1f%%", startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

else:
    st.info("No expenses added yet.")

# To run this app, save it as `app.py` and run `streamlit run app.py` in your terminal.
