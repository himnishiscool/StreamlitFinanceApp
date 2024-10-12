import streamlit as st
import time

st.set_page_config(
    page_title="Finance App",
    page_icon="💵"
)

st.title("Home")
st.sidebar.success("Select a page!")

amount = st.number_input(label="Amount", key="Amount", placeholder="Enter your amount")
type = st.selectbox("What type?", ["Cost", "Earned"], key="Type")

if "Amount" not in st.session_state:
    st.session_state["Amount"] = 0

if "Type" not in st.session_state:
    st.session_state["Type"] = 0

if "TEarned" not in st.session_state:
    st.session_state["TEarned"] = 0

if "TSpent" not in st.session_state:
    st.session_state["TSpent"] = 0

amount = st.session_state["Amount"]
type = st.session_state["Type"]
total_spent = st.session_state["TSpent"]
total_earned = st.session_state["TEarned"]
submit = st.button("Submit")

if submit:
    st.session_state["TEarned"] = total_earned
    st.session_state["TSpent"] = total_spent
    st.session_state["Amount"] = amount
    st.session_state["Type"] = type