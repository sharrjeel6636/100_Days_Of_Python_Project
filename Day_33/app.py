import streamlit as st
import json
import bcrypt
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Simple Login System", page_icon="🔐")

st.title("🔐 Simple Login System – Day 33 of 100 Days of Python")

USERS_FILE = "users.json"

# ---------------- UTILS ----------------
def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- SIDEBAR ----------------
menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- LOGGED IN VIEW ----------------
if st.session_state.logged_in:
    st.success(f"✅ Welcome, {st.session_state.username}!")
    st.write("You are successfully logged in.")

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

# ---------------- REGISTER ----------------
elif choice == "Register":
    st.subheader("📝 Register")

    reg_username = st.text_input("Username")
    reg_password = st.text_input("Password", type="password")

    if st.button("Register"):
        if not reg_username or not reg_password:
            st.warning("Please fill in all fields.")
        else:
            users = load_users()
            if reg_username in users:
                st.error("Username already exists.")
            else:
                hashed_pw = bcrypt.hashpw(
                    reg_password.encode("utf-8"),
                    bcrypt.gensalt()
                ).decode("utf-8")

                users[reg_username] = {
                    "password": hashed_pw,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                save_users(users)
                st.success("🎉 Registration successful! Please login.")

# ---------------- LOGIN ----------------
elif choice == "Login":
    st.subheader("🔑 Login")

    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not login_username or not login_password:
            st.warning("Please fill in all fields.")
        else:
            users = load_users()
            if login_username not in users:
                st.error("Username not found.")
            else:
                stored_hash = users[login_username]["password"].encode("utf-8")
                if bcrypt.checkpw(login_password.encode("utf-8"), stored_hash):
                    st.session_state.logged_in = True
                    st.session_state.username = login_username
                    st.rerun()
                else:
                    st.error("Incorrect password.")
