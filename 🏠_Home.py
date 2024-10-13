import streamlit as st
import json

st.set_page_config(page_title="Finance App", page_icon="💵")

st.title("Home")
st.sidebar.success("Select a page!")

# Initialize session state variables if not already present
if "Amount" not in st.session_state:
    st.session_state["Amount"] = 0.0
if "Type" not in st.session_state:
    st.session_state["Type"] = "Cost"
if "Description" not in st.session_state:
    st.session_state["Description"] = ""
if "Time" not in st.session_state:
    st.session_state["Time"] = ""
if "Log" not in st.session_state:
    st.session_state["Log"] = []  # Use a list to store multiple logs
if "TSpent" not in st.session_state:
    st.session_state["TSpent"] = 0.0
if "TEarned" not in st.session_state:
    st.session_state["TEarned"] = 0.0

# Helper function to save logs to the JSON file
def save_logs():
    with open("logs.json", "w") as file:
        json.dump(st.session_state["Log"], file, indent=4)

# Helper function to write totals to files
def write_value(file_name, value):
    with open(file_name, "w") as file:
        file.write(str(value))

# Input fields for new transactions
amount = st.number_input(label="Amount", value=st.session_state["Amount"])
type_ = st.selectbox("Cost or Earned?", ["Cost", "Earned"], index=0)
description = st.text_input(label="Description", value=st.session_state["Description"])
time_transaction = st.date_input(label="When did this happen?")

# Submit Button Logic
if st.button("Submit"):
    if type_ == "Cost":
        st.session_state["TSpent"] += amount
    else:
        st.session_state["TEarned"] += amount

    # Create a new log entry
    log = {
        "Amount": amount,
        "Type": type_,
        "Description": description,
        "Time": str(time_transaction),
    }

    # Add the new log to session state and save to file
    st.session_state["Log"].append(log)
    save_logs()

    # Save the updated totals to text files
    write_value("totalSpent.txt", st.session_state["TSpent"])
    write_value("totalEarned.txt", st.session_state["TEarned"])

    # Clear the input fields
    st.session_state["Amount"] = 0.0
    st.session_state["Description"] = ""
    st.session_state["Time"] = ""

    st.success("Transaction added successfully!")

# Debugging option to display current session state (optional)
if st.checkbox("Show Current Session State"):
    st.write(st.session_state)