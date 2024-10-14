import streamlit as st
import json

st.set_page_config(page_title="Finance App", page_icon="💵")

st.sidebar.success("Select a page!")
st.title("Figures")

# Function to load logs from the JSON file
def load_logs():
    try:
        with open("logs.json", "r") as file:
            logs = json.load(file)
            return logs
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Load logs from the file or session state
logs = load_logs()

# Calculate total spent and total earned from logs
total_spent = sum(log["Amount"] for log in logs if log["Type"] == "Cost")
total_earned = sum(log["Amount"] for log in logs if log["Type"] == "Earned")

# Display the figures with decoration
st.markdown(
    f"""
    <div style="
        border: 5px solid #1DB954;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 50px;
        background-color: #1c1c1c;
    ">
        <h2 style="color: #1DB954; margin: 0;">💰 Total Earned</h2>
        <p style="font-size: 80px; font-weight: bold; color: #1DB954; margin: 10px 0;">
            ${total_earned:,.2f}
        </p>
    </div>
    """, unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="
        border: 5px solid #E74C3C;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 50px;
        background-color: #1c1c1c;
    ">
        <h2 style="color: #E74C3C; margin: 0;">💸 Total Spent</h2>
        <p style="font-size: 80px; font-weight: bold; color: #E74C3C; margin: 10px 0;">
            ${total_spent:,.2f}
        </p>
    </div>
    """, unsafe_allow_html=True
)

if total_earned-total_spent >= 0:
    st.markdown(
        f"""
        <div style="
            border: 5px solid #1DB954;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            margin-top: 50px;
            background-color: #1c1c1c;
        ">
            <h2 style="color: #1DB954; margin: 0;">🤑 Net Worth</h2>
            <p style="font-size: 80px; font-weight: bold; color: #1DB954; margin: 10px 0;">
                ${total_earned-total_spent:,.2f}
            </p>
        </div>
        """, unsafe_allow_html=True
    )
else:
    st.markdown(
        f"""
        <div style="
            border: 5px solid #E74C3C;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            margin-top: 50px;
            background-color: #1c1c1c;
        ">
            <h2 style="color: #E74C3C; margin: 0;">🥶 Net Worth</h2>
            <p style="font-size: 80px; font-weight: bold; color: #E74C3C; margin: 10px 0;">
                ${total_earned-total_spent:,.2f}
            </p>
        </div>
        """, unsafe_allow_html=True
    )