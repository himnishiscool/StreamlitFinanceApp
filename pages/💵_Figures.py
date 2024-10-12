import streamlit as st

st.set_page_config(
    page_title="Finance App",
    page_icon="💵"
)

st.sidebar.success("Select a page!")
st.title("Figures")

with open("totalSpent.txt", "r") as file:
    amount_spent = file.read()
    amount_spent = int(amount_spent)

with open("totalEarned.txt", "r") as file:
    amount_earned = file.read()
    amount_earned = int(amount_earned)

if st.session_state["TEarned"]:
    st.rerun()

total_earned = st.markdown(
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
    """,
    unsafe_allow_html=True
)

total_spent = st.markdown(
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
    """,
    unsafe_allow_html=True
)
