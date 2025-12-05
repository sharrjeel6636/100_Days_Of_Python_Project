import streamlit as st
from datetime import datetime, date, time, timedelta
import time as tlib

st.set_page_config(page_title="Countdown Timer", page_icon="⏳", layout="centered")

st.title("⏳ Countdown Timer – Day 19 of 100 Days of Python")
st.write("Choose a duration or pick a target date & time. The timer will count down live.")

mode = st.radio("Choose mode:", ("Duration (hrs:min:sec)", "Target date & time"))

if mode == "Duration (hrs:min:sec)":
    cols = st.columns(3)
    with cols[0]:
        hours = st.number_input("Hours", min_value=0, max_value=999, value=0, step=1)
    with cols[1]:
        minutes = st.number_input("Minutes", min_value=0, max_value=59, value=1, step=1)
    with cols[2]:
        seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0, step=1)

    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    start_label = f"Start {hours}h {minutes}m {seconds}s"
else:
    # Target date & time
    today = date.today()
    now = datetime.now().time().replace(microsecond=0)
    target_date = st.date_input("Target Date", value=today)
    target_time = st.time_input("Target Time", value=now)
    target_dt = datetime.combine(target_date, target_time)

    # If target is in the past, warn and allow fixing
    if target_dt <= datetime.now():
        st.warning("Target datetime must be in the future. Please choose a future date/time.")
    total_seconds = int((target_dt - datetime.now()).total_seconds())
    start_label = f"Target: {target_dt.strftime('%Y-%m-%d %H:%M:%S')}"

start_button = st.button("Start Timer")

# Container to update countdown
count_placeholder = st.empty()

def format_time(sec):
    if sec < 0:
        sec = 0
    td = timedelta(seconds=sec)
    # Format as D:HH:MM:SS if days exist, else HH:MM:SS
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if days > 0:
        return f"{days}d {hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if start_button:
    if total_seconds <= 0:
        st.error("Please set a duration greater than 0 seconds (or a future target datetime).")
    else:
        st.info(start_label)
        try:
            remaining = int(total_seconds)
            while remaining >= 0:
                # Update UI
                count_placeholder.markdown(
                    f"<h1 style='text-align:center; font-size:48px'>{format_time(remaining)}</h1>",
                    unsafe_allow_html=True
                )
                # small helpful info
                st.caption("Press stop in the page controls to interrupt (or refresh the page).")
                if remaining == 0:
                    st.success("⏰ Time's up!")
                    try:
                        st.balloons()
                    except:
                        pass
                    break
                tlib.sleep(1)
                remaining -= 1
        except Exception as e:
            st.error(f"Timer interrupted: {e}")
