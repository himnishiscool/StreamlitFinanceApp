import streamlit as st
import json

st.set_page_config(page_title="Finance App", page_icon="💵")

st.sidebar.success("Select a page!")
st.title("Figures")

# Initialize session state for total spent and earned if they don't exist
if "TSpent" not in st.session_state:
    st.session_state["TSpent"] = 0
if "TEarned" not in st.session_state:
    st.session_state["TEarned"] = 0

# Function to read totals from files
def read_totals():
    try:
        with open("totalSpent.txt", "r") as file:
            st.session_state["TSpent"] = float(file.read())
    except (FileNotFoundError, ValueError):
        st.session_state["TSpent"] = 0  # Reset if file not found or contains invalid data

    try:
        with open("totalEarned.txt", "r") as file:
            st.session_state["TEarned"] = float(file.read())
    except (FileNotFoundError, ValueError):
        st.session_state["TEarned"] = 0  # Reset if file not found or contains invalid data

# Read totals from files
read_totals()

# Read total spent and earned from session state
amount_spent = st.session_state.get("TSpent", 0)
amount_earned = st.session_state.get("TEarned", 0)

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
            ${amount_earned:,.2f}
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
            ${amount_spent:,.2f}
        </p>
    </div>
    """, unsafe_allow_html=True
)
