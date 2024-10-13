import streamlit as st

st.set_page_config(page_title="Finance App", page_icon="💵")

st.title("Home")
st.sidebar.success("Select a page!")

# Initialize session state variables if not already present
if "Amount" not in st.session_state:
    st.session_state["Amount"] = 0
if "Type" not in st.session_state:
    st.session_state["Type"] = ""
if "Description" not in st.session_state:
    st.session_state["Description"] = ""
if "Time" not in st.session_state:
    st.session_state["Time"] = ""
if "Log" not in st.session_state:
    st.session_state["Log"] = {}
if "TSpent" not in st.session_state:
    st.session_state["TSpent"] = 0
if "TEarned" not in st.session_state:
    st.session_state["TEarned"] = 0

amount = st.number_input(label="Amount", placeholder="Enter your amount", value=st.session_state.Amount)
type_ = st.selectbox("Cost or Earned?", ["Cost", "Earned"], index=0)
description = st.text_input(label="Description", placeholder="A brief description", value=st.session_state.Description)
time_transaction = st.date_input(label="When did this happen?")

# Function to write totals to files
def write_value(file_name, value):
    with open(file_name, "w") as file:
        file.write(str(value))

# Submit Button Logic
if st.button("Submit"):
    if type_ == "Cost":
        st.session_state.TSpent += amount
    else:
        st.session_state.TEarned += amount

    log_entry = {
        "Amount": amount,
        "Type": type_,
        "Description": description,
        "Time": str(time_transaction),
    }

    st.session_state.Log[len(st.session_state.Log) + 1] = log_entry  # Add new entry to log

    # Write updated totals to files
    write_value("totalSpent.txt", st.session_state.TSpent)
    write_value("totalEarned.txt", st.session_state.TEarned)

    # Update session state
    st.session_state.update({
        "Amount": 0,  # Reset inputs
        "Type": "",
        "Description": "",
        "Time": ""
    })

st.write("Current Log:", st.session_state.Log)
