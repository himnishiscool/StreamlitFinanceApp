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

# Sorting function
def sort_logs(logs, order="newest"):
    reverse = True if order == "newest" else False
    return sorted(logs, key=lambda x: datetime.fromisoformat(x["Time"]), reverse=reverse)

# Sidebar for sorting and view options
view_mode = st.radio("Select View Mode:", ["Mixed View", "Columns View"])
sort_order = st.selectbox("Sort Logs By:", ["Newest to Oldest", "Oldest to Newest"])
order = "newest" if sort_order == "Newest to Oldest" else "oldest"

# Sort logs based on selected order
logs = sort_logs(st.session_state["Log"], order)

# Display logs based on the selected view mode
if not logs:
    st.write("No logs available.")
else:
    if view_mode == "Mixed View":
        # Mixed view: All logs in a single column
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
    else:
        # Columns view: Split into 'Cost' and 'Earned'
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("💸 Costs")
            for log in logs:
                if log["Type"] == "Cost":
                    st.markdown(
                        f"""
                        <div style="
                            border: 2px solid #E74C3C;
                            border-radius: 10px;
                            padding: 15px;
                            margin: 10px 0;
                            background-color: #1c1c1c;
                        ">
                            <p style="font-size:18px; margin:0; color:white;">
                                <b>Amount:</b> ${log["Amount"]:.2f}
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

        with col2:
            st.subheader("💰 Earned")
            for log in logs:
                if log["Type"] == "Earned":
                    st.markdown(
                        f"""
                        <div style="
                            border: 2px solid #1DB954;
                            border-radius: 10px;
                            padding: 15px;
                            margin: 10px 0;
                            background-color: #1c1c1c;
                        ">
                            <p style="font-size:18px; margin:0; color:white;">
                                <b>Amount:</b> ${log["Amount"]:.2f}
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
