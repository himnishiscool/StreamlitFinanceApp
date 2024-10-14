import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="Finance App", page_icon="💵")

st.sidebar.success("Select a page!")
st.title("Logs")

# Initialize session state for logs if it doesn't exist
if "Log" not in st.session_state:
    st.session_state["Log"] = []  # Start with an empty list

# Function to load logs from the JSON file
def load_logs():
    try:
        with open("logs.json", "r") as file:
            logs = json.load(file)
            st.session_state["Log"] = logs  # Update session state
    except (FileNotFoundError, json.JSONDecodeError):
        st.session_state["Log"] = []  # Default to an empty list if error occurs

# Load logs if not already loaded into session state
if not st.session_state["Log"]:
    load_logs()

# Sort logs by time (newest to oldest)
logs = sorted(
    st.session_state["Log"],
    key=lambda x: datetime.fromisoformat(x["Time"]),
    reverse=True
)

if not logs:
    st.write("No logs available.")
else:
    for log in logs:
        color = "#1DB954" if log["Type"] == "Earned" else "#E74C3C"

        st.markdown(
            f"""
            <div style="
                border: 2px solid {color};
                border-radius: 10px;
                padding: 15px;
                margin: 10px 0;
                background-color: #1c1c1c;
            ">
                <p style="font-size:18px; margin:0; color:white;">
                    <b>Amount:</b> ${log["Amount"]:.2f}
                </p>
                <p style="font-size:18px; margin:0; color:{color};">
                    <b>Type:</b> {log["Type"]}
                </p>
                <p style="font-size:18px; margin:0; color:gray;">
                    <b>Description:</b> {log["Description"]}
                </p>
                <p style="font-size:14px; margin:0; color:#aaaaaa;">
                    <b>Time:</b> {log["Time"]}
                </p>
            </div>
            """, unsafe_allow_html=True
        )