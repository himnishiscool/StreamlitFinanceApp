import streamlit as st
import json

st.set_page_config(page_title="Finance App", page_icon="💵")

st.sidebar.success("Select a page!")
st.title("Logs")

# Initialize session state for logs
if "Log" not in st.session_state:
    st.session_state["Log"] = []  # Default to an empty list

try:
    # Try to load logs from the JSON file if it's not already in session state
    if not st.session_state["Log"]:
        with open("logs.json", "r") as file:
            logs = json.load(file)
            st.session_state["Log"] = logs
except (FileNotFoundError, json.JSONDecodeError) as e:
    st.session_state["Log"] = []  # Reset to empty if error occurs
    st.error(f"Error loading logs: {str(e)}")  # Display the error message

logs = st.session_state["Log"]

# Check if there are any logs to display
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
